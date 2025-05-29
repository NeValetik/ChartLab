from antlr4 import *
from antlr2.ChartLexer import ChartLexer
from antlr2.ChartParser import ChartParser
from components.interpretor import *

from PIL import Image

def create_chart(content):
    input_stream = InputStream(content)

    lexer = ChartLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = ChartParser(token_stream)
    tree = parser.command()

    interpretor = Interpretor()
    json_list = interpretor.walk_tree(tree)
    return json_list

if __name__ == '__main__':
    with open("data/templates/example1.ch" "r", encoding="utf-8") as file:
        content = file.read()
    
    image_path = create_chart(content)
    image = Image.open(image_path)
    image.show()

