def is_palindrome(n):
    reversed = n[::-1]
    if n == reversed:
        return "Palindrome"
    else:
        return "Not Palindrome"

s = input("Enter the string you want to check : ")
print(is_palindrome(s))