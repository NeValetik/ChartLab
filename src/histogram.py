import pandas as pd
import matplotlib.pyplot as plt
from antlr4 import *

from src.antlr2.ChartParser import ChartParser
import seaborn as sns

from src.antlr2.ChartLexer import ChartLexer


def read_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path,  delimiter=',')
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

def plot_histogram(df, column, buckets=10):
    sns.set(style="whitegrid")

    # Bin the data using equal-width intervals and extract edges
    bins = pd.cut(df[column], bins=buckets)

    # Count values in each bin
    bin_counts = bins.value_counts().sort_index()

    # Use bin edges for x-axis
    bin_edges = [interval.right for interval in bin_counts.index]
    bin_starts = [interval.left for interval in bin_counts.index]
    bin_labels = [f"{int(start)}–{int(end)}" for start, end in zip(bin_starts, bin_edges)]

    # Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=bin_labels, y=bin_counts.values, palette="viridis")

    # Label adjustments
    plt.xlabel(f"{column.title()} Range")
    plt.ylabel("Frequency")
    plt.title(f'Histogram of {column} with {buckets} bins')
    plt.xticks(rotation=0)  # Straight labels
    plt.tight_layout()
    plt.show()





class ParseTreeData(ParseTreeVisitor):
    def extract_data(self, tree):
        command = ""
        dataset = None
        x_value = None
        step = None

        for child in tree.getChildren():
            if isinstance(child, ChartParser.ChartFunctionContext):
                # Build full command string
                command = child.getText()
                print(f"Full command: {command}")

            if isinstance(child, ChartParser.TableContext):
                for grandchild in child.getChildren():
                    dataset = grandchild.getText()

            elif isinstance(child, ChartParser.ChartFunctionContext):
                grandchild_list = list(child.getChildren())
                for i in range(len(grandchild_list)):
                    if isinstance(grandchild_list[i], ChartParser.VarContext):
                        if x_value is None:
                            x_value = grandchild_list[i].getText()  # column to plot
                    if isinstance(grandchild_list[i], ChartParser.ValueContext):
                        if step is None:
                            step = grandchild_list[i].getText()
        return command, dataset, x_value, step


def interpret_command(parse_tree):
    # Initialize data and extract information from the tree
    data = ParseTreeData()
    command, dataset, columns, step = data.extract_data(parse_tree)
    print(command)



    is_histogram_command = (
            ("show frequency of" in command) or
            ("show distribution of" in command and "by" in command) or
            ("show frequency in" in command)
    )

    if not is_histogram_command:
        print(f"Command '{command}' is not recognized for grouped bar charts.")
        return

    if not dataset or not columns:
        print("Error: Missing one of the required columns or dataset.")
        return

    # Read the data
    file_path = rf"data/statistic_data/{dataset}.csv"


    try:
        df = read_data(file_path)
    except FileNotFoundError:
        print(f"Error: The dataset file {dataset}.csv was not found.")
        return

    df.columns = [c.lower() for c in df.columns]
    column = columns.lower()
    df[column] = pd.to_numeric(df[column], errors='coerce')
    min_val = df[column].min()
    max_val = df[column].max()
    buckets = int((max_val - min_val)/float(step))

    if column not in df.columns:
        print(f"Error: Column '{column}' not found in dataset.")
        return
    # Plot

    plot_histogram(df, column, buckets)



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
    test_input = "with data from scores chart: show frequency of score step 10"
    parse_tree = parseTree(test_input)
    interpret_command(parse_tree)


