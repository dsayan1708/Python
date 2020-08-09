while True:
    try:
        age = int(input("Enter the age to check eligibility : "))
        break
    except ValueError:
        print("Please enter an integer")
    except:
        print("Unexpected error")
    else:
        print(f"User has entered {age}")
    finally:
        print("This is a program to verify age")

if age>18:
    print("You are eligible to play")
else:
    print("You aren't eligible to play")