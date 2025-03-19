from lexer.components.TokenType import *


class Token:
    def __init__(self, **args):
        self.value = args.get("value")
        self.tokenType = args.get("tokenType")
        self.index = args.get("index")

    def __str__(self):
        return f"Token value: { self.value } \t type: {str(self.tokenType)}"
