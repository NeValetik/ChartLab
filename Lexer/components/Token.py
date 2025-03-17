from Lexer.components.TokenType import *

class Token:
  
  def __init__(self, **args):
    print(args)
    self._value = args.get("value")
    self._tokenType = args.get("tokenType")(self._value)