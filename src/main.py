# Custom components (even if we are not using lexer and parser)
from lexer.Lexer import *
from parser.Parser import *
from interpretor.Interpretor import *

# ANTLR components
from antlr4 import *
from antlr.ChartLexer import ChartLexer
from antlr.ChartParser import ChartParser
from antlr.visualize import *

from PIL import Image  # To open the image

def create_chart(content):
    # This function basically repeates the antlr/test.py

    input_stream = InputStream(content)
    lexer = ChartLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    token_stream.fill()

    print_tokens(token_stream.tokens)

    parser = ChartParser(token_stream)
    tree = parser.command()

    print("\n\033[1;32mParse Tree:\033[0m")
    print_parse_tree(tree, parser)

    # Temporar solution: our interpreter will return path of the generated image
    # img_path = Interpretor.interpret(tree)
    img_path = "data/img/example1.png"
    return img_path


if __name__ == '__main__':
    with open("data/templates/example1.ch" "r", encoding="utf-8") as file:
        content = file.read()
    
    image_path = create_chart(content)
    image = Image.open(image_path)
    image.show()

