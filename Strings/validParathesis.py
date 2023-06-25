def validParent(string):
    stack = []
    for bracket in string:
        match bracket:
            case'(': 
                stack.append(bracket)
            case '[':
                stack.append(bracket)
            case '{':
                stack.append(bracket)
            case ')':
                if stack.pop() == '(':
                    continue
                else:
                    return False
            case ']':
                if stack.pop() == '[':
                    continue
                else:
                    return False
            case '}':
                if stack.pop() == '{':
                    continue
                else:
                    return False
    if len(stack) > 0:
        return False
    return True

print(validParent("([]{})"))