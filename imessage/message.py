class Message:
  """Model class for Message"""
  def __init__(self, message, chat):
    self._message = message
    self._chat = chat

  def getMessage(self):
    """Returns: str"""
    return self._message

  def getChat(self):
    """
    Returns: Chat
    """
    return self._chat

  def __str__(self):
    return "Message: {0}\nChat: {1}".format(self._message, str(self._chat))