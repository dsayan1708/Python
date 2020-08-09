from math import sqrt
def check_Prime(num):
    if num>1:
        for i in range(2, int(sqrt(num/2))):
            if(num%i==0):
                return(f"{num} is Not Prime")
            return(f"{num} is Prime")
    
print(check_Prime(18))