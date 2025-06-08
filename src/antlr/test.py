from antlr4 import *
from ChartLexer import ChartLexer
from ChartParser import ChartParser
from antlr4.tree.Trees import Trees
import graphviz

def visualize_tree(tree, parser):
    def walk(node):
        if isinstance(node, TerminalNode):
            label = str(node.getText())
        else:
            label = parser.ruleNames[node.getRuleIndex()]
        
        this_id = str(id(node))
        dot.node(this_id, label)

        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_id = str(id(child))
            dot.edge(this_id, child_id)
            walk(child)

    dot = graphviz.Digraph(comment='AST', format='png')
    walk(tree)
    dot.render('ast_tree', view=True)  # Renders and opens as PNG

def main():
    input_code = """
with sales from orders chart:
    compare revenue for regions

with sales from orders chart:
    compare revenue for regions

while ( x < b ) {
    with sales from orders chart:
        compare revenue for regions
}    
""".strip()

    # Initialize input stream and lexer
    input_stream = InputStream(input_code)
    lexer = ChartLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ChartParser(stream)

    # Parse the input code and generate the AST tree
    tree = parser.program()

    # Print the tree as a string for terminal output
    print("AST Tree (Text Representation):")
    print(tree.toStringTree(recog=parser))

    # Visualize the AST
    visualize_tree(tree, parser)

if __name__ == '__main__':
    main()
