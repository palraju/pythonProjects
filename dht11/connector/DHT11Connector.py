from dht11.model.TemparetureHumiditySensor import TemparetureHumiditySensor
from dht11.message.KafkaMessageConnector import send

#import Adafruit_DHT
import time


class DHT11Connector:
    def __init__(self):
        self.running = False

    def start(self):

        # DHT11 sensor selected
        # sensor = Adafruit_DHT.DHT11

        # DHT sensor pin connected to GPIO 4
        sensor_pin = 18

        # loop forever
        while self.running:
            print(self.running)
            try:
                # read the humidity and temperature
                humidity, temperature = (10, 30)  # Adafruit_DHT.read_retry(sensor, sensor_pin)

                if humidity is not None and temperature is not None:
                    sensorObject = TemparetureHumiditySensor()
                    sensorObject.sethumidity(humidity)
                    sensorObject.settempareture(temperature)
                    send(sensorObject)
                else:
                    print('Failed to get reading. Try again!')
            finally:
                time.sleep(2)


connector = DHT11Connector()


def startconnector():
    connector.running = True
    connector.start()


def stopconnector():
    connector.running = False
    print('setting running value to false')
