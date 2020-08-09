def list_to_dict():
    list1 = [1, 2, 3]
    list2 = ['one', 'two', 'three']
    result = dict(zip(list1, list2))
    print(result)

list_to_dict()

def dict_to_tuple():
    x = {1: 'one', 2: 'two', 3: 'three'}
    for item in x.items():
        print(item)

dict_to_tuple()