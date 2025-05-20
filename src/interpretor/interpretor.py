import pandas as pd
from reader.reader import *
from interpretor import plotter2
import sys, os

from antlr4 import *

from antlr2.ChartLexer import ChartLexer
from antlr2.ChartParser import ChartParser

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

class Interpretor(ParseTreeVisitor):
    img_path = None

    def walk_tree(self, tree):
        if tree is None:
            return
        
        self.interpret_node(tree)
        if Interpretor.img_path is not None:
            img_path = Interpretor.img_path
            Interpretor.img_path = None
            return img_path

        for i in range(tree.getChildCount()):
            self.walk_tree(tree.getChild(i))
        
        return

    def interpret_node(self, node):
        if isinstance(node, ChartParser.CommandContext):
            self.interpret_command(node)
        elif isinstance(node, ChartParser.ChartFunctionContext):
            pass  # Handled within interpret_command

    def interpret_command(self, node):
        dataset = None
        chart_func_ctx = None

        # Extract dataset (table) and chart function context
        for child in node.getChildren():
            if isinstance(child, ChartParser.TableContext):
                dataset = child.getText()
            elif isinstance(child, ChartParser.ChartFunctionContext):
                chart_func_ctx = child

        if not dataset or not chart_func_ctx:
            print("Error: Incomplete command - missing dataset or chart function.")
            return

        # Read dataset and validate columns
        df = Reader.read(f"{dataset}.csv")

        # Determine the type of chart function
        command_type = None
        for child in chart_func_ctx.getChildren():
            if isinstance(child, TerminalNode):
                token_type = child.getSymbol().type
                if token_type == ChartLexer.COMPARE:
                    command_type = 'COMPARE'
                elif token_type == ChartLexer.CORRELATION:
                    command_type = 'CORRELATION'
                elif token_type == ChartLexer.DIFFERENCES:
                    command_type = 'DIFFERENCES'
                elif token_type == ChartLexer.SHOW:
                    command_type = 'SHOW'
                elif token_type == ChartLexer.SCATTER_PLOT or token_type == ChartLexer.PATTERN:
                    command_type = 'SCATTER'
                elif token_type == ChartLexer.SHOW_PROPORTION or token_type == ChartLexer.SHOW_SHARE or token_type == ChartLexer.SHOW_PERCENTAGE:
                    command_type = 'PROPORTION'
                elif token_type == ChartLexer.SHOW_FREQUENCY or token_type == ChartLexer.SHOW_FREQUENCY_BUCKETS or token_type == ChartLexer.SHOW_DISTRIBUTION:
                    command_type = 'FREQUENCY'
                # Add other command types here as needed
                break  # Assume first terminal defines the command
        x_col, y_col = None, None
        group_col = None
        step = None

        # Extract parameters based on command type
        if command_type == 'COMPARE':
            var, cases = None, None
            for child in chart_func_ctx.getChildren():
                if isinstance(child, ChartParser.VarContext):
                    var = child.getText()
                elif isinstance(child, ChartParser.CasesContext):
                    cases = child.getText()
                elif isinstance(child, ChartParser.SubgroupContext):
                    group_col = child.getText()
            x_col, y_col = cases, var

        elif command_type == 'CORRELATION':
            continuous_vars = []
            for child in chart_func_ctx.getChildren():
                if isinstance(child, ChartParser.ContinuousVarContext):
                    continuous_vars.append(child.getText())
            if len(continuous_vars) >= 2:
                x_col, y_col = continuous_vars[0], continuous_vars[1]

        elif command_type == 'DIFFERENCES':
            #sa presupunem ca acest tip de comanda pt BAR CHART GROUPED/SPLIT merge doar cand tabelul are 3 coloane
            #daca tabelul are mai multe, va aleg pe prima numerica. pe viitor rezolvam.
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


        elif command_type == 'SHOW':
            ##pt bar chart stacked
            var, cases = None, None
            for child in chart_func_ctx.getChildren():
                if isinstance(child, ChartParser.VarContext):
                    var = child.getText()
                elif isinstance(child, ChartParser.CasesContext):
                    cases = child.getText()
                elif isinstance(child, ChartParser.SubgroupContext):
                    group_col = child.getText()
            x_col, y_col = cases, var

        elif command_type == 'SCATTER':
            var_context = []
            for child in chart_func_ctx.getChildren():
                if isinstance(child, ChartParser.VarContext):
                    var_context.append(child.getText())
            if len(var_context) >= 2:
                x_col = var_context[0].lower()
                y_col = var_context[1].lower()
        
        elif command_type == 'PROPORTION':  # Pie chart
            for child in chart_func_ctx.getChildren():
                if isinstance(child, ChartParser.VarContext):
                    y_col = child.getText()
                elif isinstance(child, ChartParser.CasesContext):
                    x_col = child.getText()
        elif command_type == 'FREQUENCY': # histogram
            for child in chart_func_ctx.getChildren():
                if isinstance(child, ChartParser.VarContext):
                    x_col = child.getText()
                if isinstance(child, ChartParser.ValueContext):
                    step = child.getText()

        # Handle other command types here...

        df.columns = df.columns.str.strip().str.lower()

        if x_col not in df.columns or (y_col and y_col not in df.columns) or (group_col and group_col not in df.columns):
            print(f"Error: One or more columns ({x_col, y_col}) not found not found in dataset '{dataset}'.")
            return

        # Invoke appropriate plotter function
        if command_type == 'COMPARE' or command_type == 'DIFFERENCES':
            if group_col:
                Interpretor.img_path = plotter2.plot_grouped_bar_chart(df, y_col, x_col, group_col)
            else:
                Interpretor.img_path = plotter2.plot_comaprison_daniela_version(df, y_col, x_col)
        elif command_type == 'CORRELATION':
            Interpretor.img_path = plotter2.plot_line_graph(df, x_col, y_col)
        elif command_type == 'SHOW':
            if group_col:
                Interpretor.img_path = plotter2.plot_stacked_bar_chart(df, y_col, x_col, group_col)
            else:
                pass
                #other show commands
        elif command_type == 'SCATTER':
            Interpretor.img_path = plotter2.plot_scatter_plot(df, x_col, y_col)
        elif command_type == 'PROPORTION':
            Interpretor.img_path = plotter2.plot_pie_chart(df, x_col, y_col)
        elif command_type == 'FREQUENCY':
            Interpretor.img_path = plotter2.plot_histogram(df, x_col, step)
        # Add other plotting calls as needed

        return