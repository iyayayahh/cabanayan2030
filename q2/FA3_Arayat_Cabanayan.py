from abc import ABC, abstractmethod

class Sensor(ABC):
    @abstractmethod
    def get_reading(self):
        pass

class PHSensor(Sensor):
    def get_reading(self):
        return "7.2 pH (Neutral)"

class TempSensor(Sensor):
    def get_reading(self):
        return "24.5°C"
    
pH_sensor=PHSensor()
temp_sensor = TempSensor()

print ("--- Lab Inventory System ---")
print (f"[pH Sensor] Reading: {pH_sensor.get_reading()}")
print (f"[Temperature Sensor] Reading: {temp_sensor.get_reading()}")
print ("\n----------------------------")

#  my_sensor = Sensor()



    
        
