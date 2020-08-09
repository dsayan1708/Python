def common_letters():
    str1 = input("Enter the first string : ")
    str2 = input("Enter the second string : ")
    set1 = set(str1)
    set2 = set(str2)
    common = set1 & set2
    print(common)

common_letters()