def freq_of_words():
    string = input("Enter the string : "). split()
    d = {}
    for i in string:
        if i not in d:
            d[i] = 0
        d[i]+=1
    print(d)

freq_of_words()