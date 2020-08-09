class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        
    @property
    def full_name(self):
        return f"This phone is {self.brand} {self.model_name}"
    
    def make_a_call(self, number):
        return f"Dialling {number}..."

class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, rear_camera):
        super().__init__(brand, model_name, price)
        # Phone.__init__(self, brand, model_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera
    
S1 = Smartphone("OnePlus", "8 Pro", "75000", "8GB", "256GB", "64MP")

print(S1.full_name)