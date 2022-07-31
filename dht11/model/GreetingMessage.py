class GreetingMessage:
    __message = ''

    def __init__(self):  # constructor
        self._message = ''  # instance attribute

    def setmessage(self, message):
        self.__message = message

    def getmessage(self):
         return self.__message
