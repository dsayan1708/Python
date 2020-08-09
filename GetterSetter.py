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
        return 
    #using_getter
    @property    
    def price(self):
        return self.p
    #using_setter
    @price.setter
    def price(self, new_price):
        self.p = max(new_price, 0)

L1 = Laptop('Lenovo', 'ABCD', 40000)
L2 = Laptop('Dell', 'EFGH', 50000 )
L3 = Laptop('HP', 'IJKL', 60000)

L1.price = -40000
print(L1.price)