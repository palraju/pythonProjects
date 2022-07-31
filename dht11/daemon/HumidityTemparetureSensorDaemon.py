from dht11.connector.DHT11Connector import startconnector, stopconnector


def startdaemon():
    startconnector()


def stopdaemon():
    stopconnector()