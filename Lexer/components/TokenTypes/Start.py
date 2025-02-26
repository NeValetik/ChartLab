from TokenType import *

class Start(TokenType):

  def __init__(self, token):
    super.__init__(token)

  def interpret(self):
    print("I'm start " + self._token )