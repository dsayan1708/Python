class Laptop():
    def __init__(self, brand_name, model_name, price):
        #initializing instance varaibles
        self.bn = brand_name
        self.mn = model_name
        self.p = price

    def apply_disc(self, disc):
        after_disc = self.p - (self.p * (disc/100))
        return after_disc

L1 = Laptop('Lenovo', 'ABCD', 40000)
L2 = Laptop('Dell', 'EFGH', 50000 )
L3 = Laptop('HP', 'IJKL', 60000)

print(L1.apply_disc(20))

# print(L1.bn, L1.mn, L1.p)
# print(L2.bn, L2.mn, L2.p)
# print(L3.bn, L3.mn, L3.p)