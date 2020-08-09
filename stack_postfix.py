def postfix(arr):
    stack = []
    operators = ['+', '-', '*', '/', '%']
    for item in arr:
        if item not in operators:
            stack.append(item)
        else:
            first = int(stack.pop())
            second = int(stack.pop())

            if(item == '+'):
                stack.append(second + first)
            elif(item == '-'):
                stack.append(second - first)
            elif(item == '*'):
                stack.append(second * first)
            elif(item == '/'):
                stack.append(second / first)
            elif(item == '%'):
                stack.append(second % first)
    return stack[-1]

arr = ['2', '1', '+', '3', '5', '+', '*']
print(postfix(arr))