from abc import ABC, abstractmethod

class TokenType(ABC):

  def __init__(self, token):
    self._token = token

  @abstractmethod
  def interpret(self):
    pass