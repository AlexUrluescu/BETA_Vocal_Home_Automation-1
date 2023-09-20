from senzor import *

x = dht_sensor()

while True:
    y = x.get_t()
    print(y)
    y = x.get_h()
    print(y)
    print(type(y))