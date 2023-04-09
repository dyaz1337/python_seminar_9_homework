# 2) реализовать метакласс. позволяющий создавать всегда один и
# тот же объект класса

from time import sleep


class MetaTraffic(type):
    TrafficLight = None

    def __call__(cls):
        if cls.TrafficLight is None:
            cls.TrafficLight = super().__call__()
            return cls.TrafficLight
        else:
            return cls.TrafficLight


class TrafficLight(metaclass=MetaTraffic):
    __color = {"красный": 7, "желтый": 2, "зелёный": 8}

    def running(self):
        print("красный")
        sleep(self.__color["красный"])
        print("желтый")
        sleep(self.__color["желтый"])
        print("зелёный")
        sleep(self.__color["зелёный"])


traffic_light = TrafficLight()
traffic_light_1 = TrafficLight()
traffic_light_2 = TrafficLight()

print(traffic_light is traffic_light_1)
print(traffic_light_1 is traffic_light_2)
print(traffic_light_2 is traffic_light)
