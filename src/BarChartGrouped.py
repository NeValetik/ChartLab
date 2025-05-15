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

def plot_grouped_bar_chart(df, value_col, group_col, category_col):
    """
       value_col = 'Salary'
       group_col = 'Gender'
       category_col = 'Company'
       """
    # Set Seaborn style for better aesthetics
    sns.set(style="whitegrid")

    sns.barplot(data=df, x=category_col, y=value_col, hue=group_col)

    plt.xlabel(category_col)
    plt.ylabel(value_col)
    plt.title(f'{value_col} by {group_col} for each {category_col}')
    plt.xticks(rotation=45)
    plt.legend(title=group_col)
    plt.tight_layout()
    plt.show()



class ParseTreeData(ParseTreeVisitor):
    def extract_data(self, tree):
        command = ""
        dataset = None
        col_value = None
        col_group = None
        col_categ = None

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
                        if col_value is None:
                            col_value = grandchild_list[i].getText()  # e.g., Salary
                    elif isinstance(grandchild_list[i], ChartParser.SubgroupContext):
                        if col_group is None:
                            col_group = grandchild_list[i].getText()  # e.g., Gender
                    elif isinstance(grandchild_list[i], ChartParser.CasesContext):
                        if col_categ is None:
                            col_categ = grandchild_list[i].getText()


        return command, dataset, col_value, col_group, col_categ


def interpret_command(parse_tree):
    # Initialize data and extract information from the tree
    data = ParseTreeData()
    command, dataset, value_col, group_col, category_col = data.extract_data(parse_tree)



    is_grouped_command = (
            ("compare" in command and ("splitby" in command or "split by" in command)  and "for" in command) or
            ("compare" in command and ("groupedby" in command or "grouped by" in command) and "for" in command) or
            ("differenceswithin" in command and "for" in command)
    )

    if not is_grouped_command:
        print(f"Command '{command}' is not recognized for grouped bar charts.")
        return

    if not dataset or not group_col or not category_col:
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

    if value_col is None:
        excluded = {group_col.lower(), category_col.lower()}
        possible_value_cols = [col for col in df.columns if
                               col not in excluded and pd.api.types.is_numeric_dtype(df[col])]
        if not possible_value_cols:
            print("Error: Could not determine a suitable numeric column for plotting.")
            return
        value_col = possible_value_cols[0]
        print(f"📊 Auto-selected value column: {value_col}")


    missing_cols = [col for col in [value_col, group_col, category_col] if col not in df.columns]
    if missing_cols:
        print(f"Error: Missing columns in dataset: {missing_cols}")
        return

    # Plot
    plot_grouped_bar_chart(df, value_col, group_col, category_col)



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
    test_input = "with data from industry chart: compare salary split by gender for company"
    test_input2 = "with data from industry chart: compare salary grouped by gender for company"
    test_input3 = "with data from industry chart: differences within gender for company"
    parse_tree = parseTree(test_input3)
    interpret_command(parse_tree)


