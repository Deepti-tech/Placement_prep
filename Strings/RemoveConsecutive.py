def remove(string):
    stack = []
    for ch in string :
        if len(stack) == 0 :
            stack.append(ch)
        else :
            if stack[-1] != ch :
                stack.append(ch)
    return "".join(map(str,stack))
print(remove('aabbaac'))