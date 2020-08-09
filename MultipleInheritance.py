class A:
    def class_a_method(self):
        return "This is a method of Class A"
    
    def hello(self):
        return "Returning from Class A"

class B:
    def class_a_method(self):
        return "This is a method of Class A"
    
    def hello(self):
        return "Returning from Class B"

class C(A, B):
    pass

objC = C()

print(objC.hello())
print(help(C))