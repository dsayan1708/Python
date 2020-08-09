from math import sqrt
def sieve_prime(num):
    prime_arr = [1] * (num+1) #makes a list of 1
    prime_arr[0] = 0 #initialize first index with 0
    prime_arr[1] = 0
    for i in range(2, int(sqrt(num))+1):
        if prime_arr[i] == 1:
            j=2
            while i*j<num+1:
                prime_arr[j*i] = 0
                j+=1
    return prime_arr

print(sieve_prime(15))