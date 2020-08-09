class Person:
    def __init__(self, first_name, last_name, age):
        print("Init method / constructor gets called here.")
        self.fn = first_name
        self.ln = last_name
        self.a = age

p1 = Person('Sayan', 'Dey', 21)
p2 = Person('Dey', 'Sayan', 21)
print(p1.fn)
print(p2.ln)