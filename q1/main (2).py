class Glassware: 
    def __init__(self, material, capacity):
        self.material = material
        self.capacity = capacity
        
    def info(self):
        print ("Material:", self.material)
        print ("Capacity:", self.capacity, "mL")
        
class Beaker(Glassware):
    def __init__(self, material, capacity):
        Glassware.__init__(self, material, capacity)
        
class Tray:
    def __init__(self):
        self.beakers = []
        
        for i in range(5):
            beaker = Beaker("Glass", 250)
            self.beakers.append(beaker)
            
    def display_beaker(self):
        for i, beaker in enumerate (self.beakers, 1):
            print ("Beaker", i)
            beaker.info()
            
tray = Tray()
tray.display_beaker()

del tray

        