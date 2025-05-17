import pandas as pd
import matplotlib.pyplot as plt
from antlr4 import *

from src.antlr2.ChartParser import ChartParser
import seaborn as sns

from src.antlr2.ChartLexer import ChartLexer


def read_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path,  delimiter=';')
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")

def plot_histogram(df, col, bins):
    """
       value_col = 'Salary'
       group_col = 'Gender'
       category_col = 'Company'
       """
    # Set Seaborn style for better aesthetics
    sns.set(style="whitegrid")
    sns.histplot(df[col], bins=bins, kde=False)
    plt.xlabel(col)
    plt.ylabel("Frequency")
    plt.title(f'Histogram of {col} with {bins} bins')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



class ParseTreeData(ParseTreeVisitor):
    def extract_data(self, tree):
        command = ""
        dataset = None
        x_value = None
        y_value = None

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
                    elif isinstance(grandchild_list[i], ChartParser.RangeContext):
                        if y_value is None:
                            y_value = grandchild_list[i].getText()  # range of bins


        return command, dataset, x_value, y_value


def interpret_command(parse_tree):
    # Initialize data and extract information from the tree
    data = ParseTreeData()
    command, dataset, column, bins = data.extract_data(parse_tree)
    print(command)
    print(bins)



    is_histogram_command = (
            ("show frequency of" in command and "by" in command) or
            ("show distribution of" in command and "by" in command) or
            ("show frequency in" in command)
    )

    if not is_histogram_command:
        print(f"Command '{command}' is not recognized for grouped bar charts.")
        return

    if not dataset or not bins:
        print("Error: Missing one of the required columns or dataset.")
        return

    # Read the data
    file_path = rf"data/statistic_data/{dataset}.csv"


    try:
        df = read_data(file_path)
    except FileNotFoundError:
        print(f"Error: The dataset file {dataset}.csv was not found.")
        return

    df.columns = [col.lower() for col in df.columns]
    column = column.lower()

    if column not in df.columns:
        print(f"Error: Column '{column}' not found in dataset.")
        return

    try:
        buckets = int(bins) if bins else 10
    except ValueError:
        print(f"Error: Invalid bin value '{bins}'. Using default of 10.")
        buckets = 10
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
    test_input = "with data from scores chart: show frequency of score by studentID"
    parse_tree = parseTree(test_input)
    interpret_command(parse_tree)


