def gen(l):
    for items in range(1, l+1):
        if items % 2 == 0:
            yield(items)

even_gen = gen(10)

for i in even_gen:
    print(i)
    