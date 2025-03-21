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
    tree = parser.command()  # Change to your top-level rule if needed

    # Print parse tree
    print("\n\033[1;32mParse Tree:\033[0m")
    print_parse_tree(tree, parser)


if __name__ == "__main__":
    test_input = "with sales from orders chart:\n   compare revenue for regions"
    tokenize_and_parse(test_input)
