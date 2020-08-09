class Laptop():
    discount = 10
    def __init__(self, brand_name, model_name, price):
        #initializing instance varaibles
        self.bn = brand_name
        self.mn = model_name
        self.p = price

    def apply_disc(self):
        after_disc = self.p - (self.p * (Laptop.discount/100))
        return after_disc

    def apply_special_disc(self, disc):
        after_spcl_disc = self.p - (self.p * (disc/100))
        return after_spcl_disc
    @classmethod
    def from_string(cls, string):
        brand, model, price = string.split(',')
        return cls(brand, model, price)
    
    def full_brand(self):
        return f"The name of the brand is {self.bn} {self.mn}"
    
    @staticmethod
    def intro():
        print("Welcome to Laptop Shop")

L1 = Laptop('Lenovo', 'ABCD', 40000)
L2 = Laptop('Dell', 'EFGH', 50000 )
L3 = Laptop('HP', 'IJKL', 60000)
L4 = Laptop.from_string('HP,MNOP,70000')

Laptop.intro()
print(L4.full_brand())