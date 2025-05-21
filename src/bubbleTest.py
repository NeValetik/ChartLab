import pandas as pd
import matplotlib.pyplot as plt
from antlr4 import *

from src.antlr2.ChartParser import ChartParser
import seaborn as sns

from src.antlr2.ChartLexer import ChartLexer


def read_data(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Use .csv or .xlsx")


def plot_bubble(df, x_value, y_value, bubble_size, bubble_data, scale=30000):
    size_scaled = df[bubble_size] / df[bubble_size].max() * scale

    plt.figure(figsize=(12, 6))
    scatter = plt.scatter(
        x=df[x_value],
        y=df[y_value],
        s=size_scaled,
        c=pd.factorize(df[bubble_data])[0],
        cmap='viridis',
        alpha=0.6,
        edgecolors='w',
        linewidth=0.5
    )

    plt.xlabel(x_value)
    plt.ylabel(y_value)
    plt.title(f"{bubble_size} Bubble Chart: {x_value} vs {y_value}")
    for i, label in enumerate(df[bubble_data]):
        plt.annotate(label, (df[x_value][i], df[y_value][i]), fontsize=8)

    plt.colorbar(scatter, label=bubble_data)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


class ParseTreeData(ParseTreeVisitor):
    def extract_data(self, tree):
        command = ""
        dataset = None
        x_value = None
        y_value = None
        bubble_size = None
        bubble_data = None

        for child in tree.getChildren():
            if isinstance(child, ChartParser.ChartFunctionContext):
                command = child.getText()

            if isinstance(child, ChartParser.TableContext):
                for grandchild in child.getChildren():
                    dataset = grandchild.getText()

            elif isinstance(child, ChartParser.ChartFunctionContext):
                grandchild_list = list(child.getChildren())
                columns_list = []
                for i in range(len(grandchild_list)):
                    print(grandchild_list[i].getText())
                    if isinstance(grandchild_list[i], ChartParser.VarContext):
                        columns_list.append(grandchild_list[i].getText())
                    elif isinstance(grandchild_list[i], ChartParser.CasesContext):
                        bubble_data = grandchild_list[i].getText()
                x_value = columns_list[0]
                y_value = columns_list[1]
                bubble_size = columns_list[2]


        return command, dataset, x_value, y_value, bubble_size, bubble_data


def interpret_command(parse_tree):
    # Initialize data and extract information from the tree
    data = ParseTreeData()
    command, dataset, x_value, y_value, bubble_size, bubble_data = data.extract_data(parse_tree)
    print(command)
    if not dataset:
        print("Error: Missing one of the required columns or dataset.")
        return

    # Read the data
    file_path = rf"data/statistic_data/{dataset}.csv"


    try:
        df = read_data(file_path)
    except FileNotFoundError:
        print(f"Error: The dataset file {dataset}.csv was not found.")
        return


    # df.columns = [col.lower() for col in df.columns]
    print(df.columns)
    if x_value not in df.columns:
        print(f"Error: Columns '{x_value}' not found in the dataset {dataset}.")
        return
    elif y_value not in df.columns:
        print(f"Error: Columns '{y_value}' not found in the dataset {dataset}.")
        return
    elif bubble_size not in df.columns:
        print(f"Error: Columns '{bubble_size}' not found in the dataset {dataset}.")
        return
    elif bubble_data not in df.columns:
        print(f"Error: Columns '{bubble_data}' not found in the dataset {dataset}.")
        return


    plot_bubble(df, x_value, y_value, bubble_size, bubble_data)



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
    test_input = "with data from economy chart: bubble of GDP, LifeExpectancy, Population for Country"
    parse_tree = parseTree(test_input)
    interpret_command(parse_tree)

