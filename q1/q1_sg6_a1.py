class Technician:
    def __init__ (self, name):
        self.name=name
        self.assigned_lab=None
    def assign_lab (self, lab_obj):
        self.assigned_lab=lab_obj
class Lab:
    def __init__ (self, room_number):
        self.room_number=room_number

mr_cruz=Technician("Mr. Cruz")
chem_lab=Lab("216")
mr_cruz.assign_lab(chem_lab)

print(mr_cruz.assigned_lab.room_number)
