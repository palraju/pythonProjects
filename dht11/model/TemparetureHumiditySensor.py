from dht11.model.JsonSerializable import JsonSerializable


class TemparetureHumiditySensor(JsonSerializable):
    tempareture: int = 0
    humidity: int = 0

    def __init__(self):  # constructor
        self.tempareture = 0  # instance attribute
        self.humidity = 0

    def settempareture(self, tempareture: int):
        self.tempareture = tempareture

    def gettempareture(self):
        return self.tempareture

    def sethumidity(self, humidity: int):
        self.humidity = humidity

    def gethumidity(self):
        return self.humidity
