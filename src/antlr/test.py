
from antlr4 import *
from ChartLexer import ChartLexer
from ChartParser import ChartParser
from antlr4.tree.Tree import TerminalNode


def print_tokens(tokens):
    """ Print tokens in a formatted table """
    print("\n\033[1;34mTokens:\033[0m")
    print("=" * 40)
    print(f"{'Index':<6} {'Text':<15} {'Type':<10} {'Line:Col'}")
    print("=" * 40)
    for token in tokens:
        token_text = token.text.replace("\n", "\\n")  # Escape newlines
        print(f"{token.tokenIndex:<6} {token_text:<15} {token.type:<10} {token.line}:{token.column}")
    print("=" * 40)


def print_parse_tree(tree, parser, level=0):
    """ Print parse tree with indentation for readability """
    indent = "  " * level
    if isinstance(tree, TerminalNode):
        print(f"{indent}🟢 {tree.getText()}")
    else:
        print(f"{indent}🔷 {parser.ruleNames[tree.getRuleIndex()]}")
        for child in tree.children:
            print_parse_tree(child, parser, level + 1)


def main(input_text):
    """ Run the lexer and parser on the given input text """
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
    # Example input (modify as needed)
    test_input = "with sales from orders chart: compare revenue for regions"
    main(test_input)
