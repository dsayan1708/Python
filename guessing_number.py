import random
number = random.randint(1,100)
i = 1

while True:
    n = int(input("Guess your number : "))
    if(n<number):
        print("Too low")
    elif(n>number):
        print("Too high")
    else:
        print(f"You guess the correct number in {i} guesses!!")
    i+=1

# print(f"You guessed the number in {i} guesses")
