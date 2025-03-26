from reader.reader import *
from interpretor import plotter
import sys, os

from antlr4 import *
# To import outer packages
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))
from antlr.ChartParser import ChartParser

class Interpretor(ParseTreeVisitor):
    img_path = None

    def walk_tree(self, tree):
        if tree is None:
            return
        
        # Interpret the node
        self.interpret_node(tree)
        if Interpretor.img_path is not None:
            # Because it is class field, it is not reseted
            img_path = Interpretor.img_path
            Interpretor.img_path = None
            return img_path

        # Recursively walk through children
        # For now this solution will not scale to more/another code, but for now it will plot our chart
        for i in range(tree.getChildCount()):
            self.walk_tree(tree.getChild(i))
        
        # This condition will be reached only if after entire program, there was not a single plotting action
        return

    def interpret_node(self, node):

        if isinstance(node, ChartParser.CommandContext):
            print(f"Node: {node.getText()}")
            self.interpret_command(node)

        elif isinstance(node, ChartParser.TableContext):
            pass
        elif isinstance(node, ChartParser.ChartFunctionContext):
            pass

    def interpret_command(self, node):
        command = None
        dataset = None
        x_col = None
        y_col = None

        for child in node.getChildren():
            if isinstance(child, ChartParser.ChartFunctionContext):
                print(child.getText())
                for grandchild in child.getChildren():
                    if isinstance(grandchild, TerminalNode):
                        command = grandchild.getText()
                        print(f"First word of command: {command}")
                        break
        if command in ["compare"]:
            for child in node.getChildren():
                if isinstance(child, ChartParser.TableContext):
                    for grandchild in child.getChildren():
                        dataset = grandchild.getText()

                elif isinstance(child, ChartParser.ChartFunctionContext):
                    for grandchild in child.getChildren():
                        if isinstance(grandchild, ChartParser.CasesContext):
                            x_col = grandchild.getText()
                        elif isinstance(grandchild, ChartParser.VarContext):
                            y_col = grandchild.getText()
        elif command in ["show correlation between"]:
            for child in node.getChildren():
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

        # Ensure all necessary values are extracted
        if dataset is None or x_col is None or y_col is None:
            print("Error: Could not extract dataset, x_col, or y_col from the command.")
            print(f"Parsed values: dataset={dataset}, x_col={x_col}, y_col={y_col}")  # Debug
            return

        df = Reader.read(f"{dataset}.csv")

        # Check if required columns exist
        if x_col not in df.columns or y_col not in df.columns:
            print(f"Error: Columns '{x_col}' or '{y_col}' not found in the dataset {dataset}.")
            return

        if command in ["compare"]:
            Interpretor.img_path = plotter.plot_comparison(df, y_col, x_col)
        elif command in ["show correlation between"]:
            Interpretor.img_path = plotter.plot_line_graph(df, x_col, y_col)





