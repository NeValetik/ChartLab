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

def plot_scatter(df, x_col, y_col):
    """
       value_col = 'Salary'
       group_col = 'Gender'
       category_col = 'Company'
       """
    # Set Seaborn style for better aesthetics
    sns.set(style="whitegrid")
    sns.scatterplot(data=df, x=x_col, y=y_col)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'Area chart of {x_col} with {y_col} bins')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



class ParseTreeData(ParseTreeVisitor):
    def extract_data(self, tree):
        command = ""
        dataset = None
        first_value = None
        second_value = None

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
                var_context = [v for v in grandchild_list if isinstance(v, ChartParser.VarContext)]
                if len(var_context) >= 2:
                    first_value = var_context[0].getText()
                    second_value = var_context[1].getText()


        return command, dataset, first_value, second_value


def interpret_command(parse_tree):
    # Initialize data and extract information from the tree
    data = ParseTreeData()
    command, dataset, first, second = data.extract_data(parse_tree)


    is_scatter_command = (
            ("scatter plot of" in command and "and" in command) or
            ("pattern of" in command and "and" in command)
    )

    if not is_scatter_command:
        print(f"Command '{command}' is not recognized for grouped bar charts.")
        return

    if not dataset or not first or not second:
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
    first = first.lower()
    second = second.lower()

    if first not in df.columns or second not in df.columns:
        print(f"Error: Column '{first}' and/or column {second} not found in dataset.")
        return

    plot_scatter(df, first, second)



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
    test_input = "with data from studentexam chart: pattern of StudyHours and ExamScore"
    parse_tree = parseTree(test_input)
    interpret_command(parse_tree)


