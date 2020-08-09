def first_non_repeating(string):
    dict = {}
    for items in range(len(string)):
        key = string[items]
        if key not in dict:
            dict[key] = 1
        else:
            dict[key]+=1
    counter = 0
    for i in range(len(string)):
        if dict[string[i]] == 1:
            return string[i], counter
        counter += 1
    # for key, value in dict.items():
    #     if value == 1:
    #         return(key)
    #         break   

s = 'ABCDEFGHABCDE'
print(first_non_repeating(s))