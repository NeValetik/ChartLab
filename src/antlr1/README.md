# ANTLR Guide for ChartLab

## Overview
This directory contains the ANTLR grammar files used to generate the lexer 
and the parser for our DSL -  ChartLab. Below are the instructions on how to:
* Generate the lexer and parser
* Test input using parser
* Visualize the AST (Abstract Syntax Tree)

# Setting up ANTLR
After installing ANTLR, make sure you are in the ```src/antlr/``` directory and run:
  
  ```
  antlr4 -Dlanguage=Python3 ChartLexer.g4
  antlr4 -Dlanguage=Python3 ChartParser.g4
  ```

This will generate:
* ChartLexer.interp
* ChartLexer.py
* ChartLexer.tokens
* ChartParser.interp
* ChartParser.py
* ChartParser.tokens
* ChartParserListener.py

# Testing Input using the Lexer and Parser
To test tokenization, use ```src/antlr/test.py```. 
Feel free to test any possible command as the input string or run the test script manually:

```
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
```

# Accessing the AST 
ANTLR automatically constructs a parse tree. 
The ```visualize.py``` script provides utilities to print and visualize it
It defines two functions:

```
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
```

This allows you to:
* Print the tokens extracted by the lexer.
* See a hierarchical parse tree structure.
