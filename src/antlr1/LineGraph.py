import pandas as pd
import matplotlib.pyplot as plt
from antlr4 import *
from ChartLexer import ChartLexer
from ChartParser import ChartParser
import seaborn as sns


def read_csv(file_path):
    # Reads the CSV file and returns a DataFrame
    return pd.read_csv(file_path)


def plot_line_graph(df, x_col, y_col):
    # Convert the y_col to datetime if it's not already
    df[y_col] = pd.to_datetime(df[y_col])  # Ensure y_col is datetime

    # Set Seaborn style for better aesthetics
    sns.set(style="whitegrid")

    # Create the plot
    plt.figure(figsize=(12, 6))  # Larger figure size for better clarity
    plt.plot(df[y_col], df[x_col], linestyle='-', color='b', label=f'{x_col} over time', linewidth=2)

    # Improve plot labels, title, and legend
    plt.xlabel(f'{y_col}', fontsize=12, labelpad=15)
    plt.ylabel(f'{x_col}', fontsize=12, labelpad=15)
    plt.title(f'Line Graph of {x_col} Over {y_col}', fontsize=14, fontweight='bold', pad=20)
    plt.legend(loc='upper left', fontsize=11)

    # Rotate x-tick labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Set gridlines and customize them
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()




class ParseTreeData(ParseTreeVisitor):
    def extract_data(self, tree):
        command = None
        dataset = None
        x_col = None
        y_col = None

        for child in tree.getChildren():
            if isinstance(child, ChartParser.ChartFunctionContext):
                print(child.getText())
                for grandchild in child.getChildren():
                    if isinstance(grandchild, TerminalNode):
                        command = grandchild.getText()
                        print(f"First word of command: {command}")
                        break
            if isinstance(child, ChartParser.TableContext):
                for grandchild in child.getChildren():
                    dataset = grandchild.getText()

            elif isinstance(child, ChartParser.ChartFunctionContext):
                grandchild_list = list(child.getChildren())
                for i in range(len(grandchild_list)):
                    if isinstance(grandchild_list[i], ChartParser.ContinuousVarContext):
                        if x_col is None:
                            x_col = grandchild_list[i].getText()  # First variable
                        elif y_col is None:
                            y_col = grandchild_list[i].getText()  # Second variable
                            break

        print(f"Dataset: {dataset}")
        print(f"X: {x_col}")
        print(f"Y: {y_col}")
        return command, dataset, x_col, y_col


def interpret_command(parse_tree):
    # Initialize data and extract information from the tree
    data = ParseTreeData()
    command, dataset, x_col, y_col = data.extract_data(parse_tree)

    if command not in ["compare", "show correlation between"]:
        print(f"Command '{command}' is not supported for line graphs.")
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
    plot_line_graph(df, x_col, y_col)


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
    test_input = "with data from spotify chart: show correlation between Despacito and Date"
    parse_tree = parseTree(test_input)
    interpret_command(parse_tree)
