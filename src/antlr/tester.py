from antlr4 import *
from ChartDSLLexer import ChartDSLLexer
from ChartDSLParser import ChartDSLParser
from ChartDSLListener import ChartDSLListener

input_code = 'BEGIN with info from table1 chart: show proportion of var1 by var2 END'

# Set up the input stream
input_stream = InputStream(input_code)

# Create the lexer
lexer = ChartDSLLexer(input_stream)

# Create a token stream
token_stream = CommonTokenStream(lexer)

# Create the parser
parser = ChartDSLParser(token_stream)

# Parse the input code
tree = parser.command()  # Replace 'command' with the top-level rule for your DSL


def print_tree(tree, level=0):
    if tree is None:
        return

    # Indent to show the depth of the node
    indent = "  " * level

    # Print the text of the current node
    print(f"{indent}{tree.getText()}")

    # If the node has children, print them recursively
    if hasattr(tree, 'getChildren'):
        for child in tree.getChildren():
            print_tree(child, level + 1)


# Print the formatted parse tree
print("Formatted Parse Tree:")
print_tree(tree)

