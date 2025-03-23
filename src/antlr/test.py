from antlr4 import *
from ChartLexer import ChartLexer
from ChartParser import ChartParser
from visualize import *

def tokenize_and_parse(input_text):
    input_stream = InputStream(input_text)

    # Create lexer
    lexer = ChartLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    # Print tokens
    token_stream.fill()
    print_tokens(token_stream.tokens)

    # Create parser
    parser = ChartParser(token_stream)
    tree = parser.command()

    # Print parse tree
    print("\n\033[1;32mParse Tree:\033[0m")
    print_parse_tree(tree, parser)


if __name__ == "__main__":
    # Bar Chart example
    test_input1 = "with sales from BarChartExamples chart: compare sales for months"
    tokenize_and_parse(test_input1)

    # Line Chart example
    test_input2 = "with data from spotify chart: show correlation between ShapeOfYou and Despacito"
    tokenize_and_parse(test_input2)
