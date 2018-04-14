class Patient(object):
    def __init__(self, id_no, name, allergies, bed_no):
        self.id_no = id_no
        self.name = name
        self.allergies = allergies 
        self.bed_no = None

class Hospital(object):
    def __init__(self, name, capacity):
        self.patients = []
        self.name = name
        self.capacity = capacity


