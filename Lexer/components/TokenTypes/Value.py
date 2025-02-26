from TokenType import *

class Value(TokenType):

  def __init__(self, token):
    super.__init__(token)

  def interpret(self):
    print("I'm value " + self._token )