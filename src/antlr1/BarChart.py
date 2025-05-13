import pandas as pd
import matplotlib.pyplot as plt
from antlr4 import *
from ChartLexer import ChartLexer
from ChartParser import ChartParser
import seaborn as sns


def read_csv(file_path):
    # Reads the CSV file and returns a DataFrame
    return pd.read_csv(file_path)


def plot_comparison(df, value_col, category_col):
    plt.figure(figsize=(12, 7))

    # Sort and aggregate data
    grouped_data = df.groupby(category_col)[value_col].sum().sort_values(ascending=False)

    # Use a better colormap
    colors = sns.color_palette("viridis", len(grouped_data))

    # Create bar plot
    bars = plt.bar(grouped_data.index, grouped_data.values, color=colors, alpha=0.85)

    # Add labels on bars
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2,
                 bar.get_height() + max(grouped_data.values) * 0.02,  # Offset for visibility
                 f"{bar.get_height():,.0f}",
                 ha='center', fontsize=11, fontweight='bold', color='black')

    # Improve aesthetics
    plt.xlabel(category_col, fontsize=12, fontweight='bold')
    plt.ylabel(value_col, fontsize=12, fontweight='bold')
    plt.title(f"Comparison of {value_col} across {category_col}", fontsize=14, fontweight='bold', pad=15)
    plt.xticks(rotation=45, ha="right", fontsize=11)

    # Light grid
    plt.grid(axis="y", linestyle="--", alpha=0.5)

    # Remove top and right spines for a cleaner look
    sns.despine()

    # Show plot
    plt.show()


class ParseTreeData(ParseTreeVisitor):
    def extract_data(self, tree):
        command = None
        dataset = None
        x_col = None
        y_col = None

        for child in tree.getChildren():
            if isinstance(child, ChartParser.ChartFunctionContext):
                for grandchild in child.getChildren():
                    if isinstance(grandchild, TerminalNode):
                        command = grandchild.getText()
                        print(f"First word of command: {command}")
                        break
            if isinstance(child, ChartParser.TableContext):
                for grandchild in child.getChildren():
                    dataset = grandchild.getText()

            elif isinstance(child, ChartParser.ChartFunctionContext):
                for grandchild in child.getChildren():
                    if isinstance(grandchild, ChartParser.CasesContext):
                        x_col = grandchild.getText()
                    elif isinstance(grandchild, ChartParser.VarContext):
                        y_col = grandchild.getText()

        return command, dataset, x_col, y_col


def interpret_command(parse_tree):
    # Initialize data and extract information from the tree
    data = ParseTreeData()
    command, dataset, x_col, y_col = data.extract_data(parse_tree)

    if command != "compare":
        print("Not compare")
        return

    # Ensure all necessary values are extracted
    if dataset is None or x_col is None or y_col is None:
        print("Error: Could not extract dataset, x_col, or y_col from the command.")
        return

    # Read the data
    try:
        df = read_csv(f"{dataset}.csv")
    except FileNotFoundError:
        print(f"Error: The dataset file {dataset}.csv was not found.")
        return

    # Check if required columns exist
    if x_col not in df.columns or y_col not in df.columns:
        print(f"Error: Columns '{x_col}' or '{y_col}' not found in the dataset {dataset}.")
        return

    # Plot the chart
    plot_comparison(df, y_col, x_col)


def parseTree(input_text):
    input_stream = InputStream(input_text)

    # Create lexer
    lexer = ChartLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Create parser
    parser = ChartParser(token_stream)
    tree = parser.command()

    return tree


if __name__ == "__main__":
    test_input = "with sales from orders chart:\n   show revenue for regions"
    parse_tree = parseTree(test_input)
    interpret_command(parse_tree)
