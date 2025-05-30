from antlr4 import *
from antlr2.ChartLexer import ChartLexer
from antlr2.ChartParser import ChartParser
from components.interpretor import *

def create_chart(content):
    input_stream = InputStream(content)

    lexer = ChartLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = ChartParser(token_stream)
    tree = parser.command()

    interpretor = Interpretor()
    json_list = interpretor.walk_tree(tree)
    return json_list