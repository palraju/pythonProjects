from dht11.daemon.HumidityTemparetureSensorDaemon import startdaemon, stopdaemon


def startservice():
    startdaemon()


def stopservice():
    stopdaemon()