import pandas as pd
from components.reader import *
from components.plotter import *
import sys, os

from antlr4 import *
from antlr.ChartLexer import ChartLexer
from antlr.ChartParser import ChartParser

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

class Interpretor(ParseTreeVisitor):
    def __init__(self):
        super().__init__()
        self.json_list = []

    def walk_tree(self, tree):
        if tree is None:
            return self.json_list
        
        if isinstance(tree, ChartParser.CommandContext):
            self.interpret_command(tree)
        
        for i in range(tree.getChildCount()):
            self.walk_tree(tree.getChild(i))
        
        return self.json_list

    def interpret_command(self, node):
        dataset, chart_func_ctx = None, None
        x_col, y_col, group_col = None, None, None

        # Extract dataset (table) and chart function context
        for child in node.getChildren():
            if isinstance(child, ChartParser.TableContext):
                dataset = child.getText()
            elif isinstance(child, ChartParser.ChartFunctionContext):
                chart_func_ctx = child

        if not dataset or not chart_func_ctx:
            print("Error: Incomplete command - missing dataset or chart function.")
            return

        df = Reader().read(f"{dataset}.csv")

        for child in chart_func_ctx.getChildren():
            if isinstance(child, TerminalNode):
                token_type = child.getSymbol().type

                if token_type == ChartLexer.COMPARE:  # Bar chart
                    for child in chart_func_ctx.getChildren():
                        if isinstance(child, ChartParser.VarContext):
                            y_col = child.getText()
                        elif isinstance(child, ChartParser.CasesContext):
                            x_col = child.getText()
                        elif isinstance(child, ChartParser.SubgroupContext):
                            group_col = child.getText()
                    self.check_and_normalize_data(df, dataset, x_col, y_col, group_col)
                    self.json_list.append(get_comaprison(df, y_col, x_col))
                
                elif token_type == ChartLexer.DIFFERENCES:  # Grouped bar chart
                    # Sa presupunem ca acest tip de comanda pt BAR CHART GROUPED/SPLIT merge doar cand tabelul are 3 coloane
                    # daca tabelul are mai multe, va aleg pe prima numerica. pe viitor rezolvam.
                    var, cases = None, None
                    for child in chart_func_ctx.getChildren():
                        if isinstance(child, ChartParser.CasesContext):
                            cases = child.getText()
                        elif isinstance(child, ChartParser.SubgroupContext):
                            group_col = child.getText()
                    x_col = cases
                    if var is None:
                        excluded = {group_col.lower(), x_col.lower()}
                        possible_value_cols = [col for col in df.columns if
                                            col not in excluded and pd.api.types.is_numeric_dtype(df[col])]
                        if not possible_value_cols:
                            print("Error: Could not determine a suitable numeric column for plotting.")
                            return
                        var = possible_value_cols[0]
                    y_col = var.lower()
                    self.check_and_normalize_data(df, dataset, x_col, y_col, group_col)
                    self.json_list.append(get_grouped_bar_chart(df, y_col, x_col, group_col))
                
                elif token_type == ChartLexer.SHOW:  # Stacked bar chart
                    for child in chart_func_ctx.getChildren():
                        if isinstance(child, ChartParser.VarContext):
                            y_col = child.getText()
                        elif isinstance(child, ChartParser.CasesContext):
                            x_col = child.getText()
                        elif isinstance(child, ChartParser.SubgroupContext):
                            group_col = child.getText()
                    self.check_and_normalize_data(df, dataset, x_col, y_col, group_col)
                    self.json_list.append(get_stacked_bar_chart(df, y_col, x_col, group_col))

                elif token_type == ChartLexer.CORRELATION:  # Line chart
                    continuous_vars = []
                    for child in chart_func_ctx.getChildren():
                        if isinstance(child, ChartParser.ContinuousVarContext):
                            continuous_vars.append(child.getText())
                    if len(continuous_vars) >= 2:
                        x_col, y_col = continuous_vars[0], continuous_vars[1]
                    self.check_and_normalize_data(df, dataset, x_col, y_col, group_col)
                    self.json_list.append(get_line_graph(df, x_col, y_col))

                elif token_type == ChartLexer.SCATTER_PLOT or token_type == ChartLexer.PATTERN:  # Scatter plot
                    var_context = []
                    for child in chart_func_ctx.getChildren():
                        if isinstance(child, ChartParser.VarContext):
                            var_context.append(child.getText())
                    if len(var_context) >= 2:
                        x_col = var_context[0].lower()
                        y_col = var_context[1].lower()
                    self.check_and_normalize_data(df, dataset, x_col, y_col, group_col)
                    self.json_list.append(get_scatter_plot(df, x_col, y_col))

                elif token_type == ChartLexer.SHOW_PROPORTION or token_type == ChartLexer.SHOW_SHARE or token_type == ChartLexer.SHOW_PERCENTAGE: # Pie chart
                    for child in chart_func_ctx.getChildren():
                        if isinstance(child, ChartParser.VarContext):
                            y_col = child.getText()
                        elif isinstance(child, ChartParser.CasesContext):
                            x_col = child.getText()
                    self.check_and_normalize_data(df, dataset, x_col, y_col, group_col)
                    self.json_list.append(get_pie_chart(df, x_col, y_col))

                elif token_type == ChartLexer.SHOW_FREQUENCY or token_type == ChartLexer.SHOW_FREQUENCY_BUCKETS or token_type == ChartLexer.SHOW_DISTRIBUTION:  # Histogram chart
                    step = None
                    for child in chart_func_ctx.getChildren():
                        if isinstance(child, ChartParser.VarContext):
                            x_col = child.getText()
                        if isinstance(child, ChartParser.ValueContext):
                            step = child.getText()
                    self.check_and_normalize_data(df, dataset, x_col, y_col, group_col)
                    self.json_list.append(get_histogram(df, x_col, step))

                elif token_type == ChartLexer.ACCUMULATION or token_type == ChartLexer.STACKED_TREND:  # Area chart
                    for child in chart_func_ctx.getChildren():
                        if isinstance(child, ChartParser.VarContext):
                            categories_column = child.getText()
                        elif isinstance(child, ChartParser.CasesContext):
                            y_col = child.getText()
                        elif isinstance(child, ChartParser.ContinuousVarContext):
                            x_col = child.getText()
                    self.check_and_normalize_data(df, dataset, x_col, y_col, group_col)
                    self.json_list.append(get_area_chart(df, x_col, y_col, categories_column))

                elif token_type == ChartLexer.BUBBLE:  # Bubble chart
                    columns_list = []
                    for child in chart_func_ctx.getChildren():
                        if isinstance(child, ChartParser.VarContext):
                            columns_list.append(child.getText().lower())
                        elif isinstance(child, ChartParser.CasesContext):
                            bubble_data = child.getText().lower()
                    x_col = columns_list[0]
                    y_col = columns_list[1]
                    bubble_size = columns_list[2]
                    self.check_and_normalize_data(df, dataset, x_col, y_col, group_col)
                    self.json_list.append(get_bubble(df, x_col, y_col, bubble_size, bubble_data))


    def check_and_normalize_data(self, df, dataset, x_col, y_col, group_col):
        df.columns = df.columns.str.strip().str.lower()

        if x_col:
            x_col = x_col.lower()
        if y_col:
            y_col = y_col.lower()
        if group_col:
            group_col = group_col.lower()

        if x_col not in df.columns:
            print(f"Error: Column {x_col} not found not found in the dataset: {dataset}")
            return
        if y_col and y_col not in df.columns:
            print(f"Error: Column {y_col} not found not found in the dataset: {dataset}")
            return
        if group_col and group_col not in df.columns:
            print(f"Error: Column {group_col} not found not found in the dataset: {dataset}")
            return