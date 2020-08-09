while True:
    try:
        age = int(input("Enter the number to check eligibility : "))
        break
    except ValueError:
        print("You might have entered string. Try integer value. Try again please...")
    except:
        print("Unexpected error")

if(age>18):
    print("You are eligibile to play the game!!")
else:
    print("You are not eligible to play the game!!")