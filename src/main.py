# Even if we don't use some of them, lasa sa fie
from lexer.Lexer import *
from parser.Parser import *
from interpretor.Interpretor import *

from PIL import Image  # To open the image

def create_chart(content):
    # This function will be called by our server
    # Here we'll call all of the components

    # Calling lexer and parser, in our case ANTLR, which return AST
    # Calling interperter on AST

    # Need to look smth like these:
    # ast = Antlr.get_ast(conetnt)
    # Interpreter.interpret(ast)

    # Saving the image (in img directory) and returing the path to it
    # (last comment is a temporar solution)
    pass


if __name__ == '__main__':
    with open("data/templates/example1.ch" "r", encoding="utf-8") as file:
        content = file.read()
    
    image_path = create_chart(content)
    image = Image.open(image_path)
    image.show()

