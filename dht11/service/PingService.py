from dht11.helper.Utility import getgreetingmessage
from dht11.model.GreetingMessage import GreetingMessage


def greeting(person):
    greetingmessage = getgreetingmessage(person)
    greetingmessageobject = GreetingMessage()
    greetingmessageobject.setmessage(greetingmessage);
    return greetingmessageobject
