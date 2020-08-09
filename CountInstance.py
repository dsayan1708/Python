class Laptop():
    count_instance = 0
    def __init__(self, brand_name, model_name, price):
        #initializing instance varaibles
        self.bn = brand_name
        self.mn = model_name
        self.p = price
        Laptop.count_instance+=1 #counting the number of instances

    def apply_disc(self, disc):
        after_disc = self.p - (self.p * (disc/100))
        return after_disc

L1 = Laptop('Lenovo', 'ABCD', 40000)
L2 = Laptop('Dell', 'EFGH', 50000 )
L3 = Laptop('HP', 'IJKL', 60000)

print(L1.apply_disc(20))
print(f"Number of instances called = {Laptop.count_instance}")
