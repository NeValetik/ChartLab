from reader.reader import *
from interpretor import plotter2
import sys, os

from antlr4 import *

from src.antlr2.ChartLexer import ChartLexer
from src.antlr2.ChartParser import ChartParser

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

        # Determine the type of chart function
        command_type = None
        for child in chart_func_ctx.getChildren():
            if isinstance(child, TerminalNode):
                token_type = child.getSymbol().type
                if token_type == ChartLexer.COMPARE:
                    command_type = 'COMPARE'
                elif token_type == ChartLexer.CORRELATION:
                    command_type = 'CORRELATION'
                # Add other command types here as needed
                break  # Assume first terminal defines the command

        x_col, y_col = None, None
        group_col = None

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

        # Handle other command types here...

        # Validate extracted parameters
        if not x_col or not y_col:
            print(f"Error: Missing parameters for {command_type} command.")
            return


        # Read dataset and validate columns
        df = Reader.read(f"{dataset}.csv")

        df.columns = df.columns.str.strip().str.lower()

        if x_col not in df.columns or y_col not in df.columns or (group_col and group_col not in df.columns):
            print(f"Error: One or more columns not found not found in dataset '{dataset}'.")
            return

        # Invoke appropriate plotter function
        if command_type == 'COMPARE':
            if group_col:
                Interpretor.img_path = plotter2.plot_grouped_bar_chart(df, y_col, x_col, group_col)
            else:
                Interpretor.img_path = plotter2.plot_comaprison_daniela_version(df, y_col, x_col)
        elif command_type == 'CORRELATION':
            Interpretor.img_path = plotter2.plot_line_graph(df, x_col, y_col)
        # Add other plotting calls as needed

        return