# import Adafruit_DHT
import random
class dht_sensor:
    def __init__(self):
        # self.dht_sensor22 = Adafruit_DHT.DHT22
        # self.dht_pin = 4
        self.temperature = 32
        self.humidity = 89

    def get_t(self):
        self.temperature = random.randint(0,40)
        return self.temperature
        # humidity, temperature = Adafruit_DHT.read_retry(self.dht_sensor22, self.dht_pin)
        # if humidity is not None and temperature is not None:
        #     return str(round(temperature, 2))
        # else:
        #     print("Failed to retreive data from temperature sensor")

    def get_h(self):
        self.humidity = random.randint(40,99)
        return self.humidity
        # humidity, temperature= Adafruit_DHT.read_retry(self.dht_sensor22, self.dht_pin)
        # if humidity is not None and temperature is not None:
        #     return int(round(humidity, 2))
        # else:
        #     print("Failed to retreive data from humidity sensor")