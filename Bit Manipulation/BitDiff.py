def bitDiff(a, b):
    a = format(a, 'b')
    b = format(b, 'b')
    n = max(len(a), len(b))
    diff = 0
    if len(a) > len(b):
        b = '0' * (n - len(b)) + b
    else:
        a = '0' * (n - len(a)) + a
    for i in range(n):
        if a[i] != b[i]:
            diff += 1
    return diff

print(bitDiff(10, 20))
print(bitDiff(20, 25))