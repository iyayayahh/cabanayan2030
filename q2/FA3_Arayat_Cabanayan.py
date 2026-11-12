from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod

    def __init__ (self, name):
        self.name = name
        
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def __init__(self):
        super().__init__("pH Sensor")
        
    def get_reading(self):
        return "7.2 pH (Neutral)"

class TempSensor(Sensor):
    def __init__(self):
        super().__init__("Temperature Sensor")
        
    def get_reading(self):
        return "24.5°C"

if __name__ == "__main__":
    print ("--- Lab Inventory System ---")

    pH_sensor=PHSensor()
    temp_sensor = TempSensor()

    print (f"[{pH_sensor.name}] Reading: {pH_sensor.get_reading()}")
    print (f"[{temp_sensor.name}] Reading: {temp_sensor.get_reading()}")
    print ("\n----------------------------")

    # my_sensor = Sensor()
        
