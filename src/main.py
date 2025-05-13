# Custom components (even if we are not using lexer and parser)
from lexer.lexer import *
from parser.parser import *
from interpretor.interpretor import *

# ANTLR components
from antlr4 import *
from antlr2.ChartLexer import ChartLexer
from antlr2.ChartParser import ChartParser

from PIL import Image

def create_chart(content):
    input_stream = InputStream(content)

    lexer = ChartLexer(input_stream)
    token_stream = CommonTokenStream(lexer)

    parser = ChartParser(token_stream)
    tree = parser.command()

    # Temporar solution: our interpreter will return the PATH of the generated image, instead of actual IMAGE
    interpretor = Interpretor()
    img_path = interpretor.walk_tree(tree)
    return img_path

if __name__ == '__main__':
    with open("data/templates/example1.ch" "r", encoding="utf-8") as file:
        content = file.read()
    
    image_path = create_chart(content)
    image = Image.open(image_path)
    image.show()

