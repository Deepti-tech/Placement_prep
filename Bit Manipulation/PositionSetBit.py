def posSetBits(num):
    num = format(num, 'b')
    pos = -1
    if num.count('1') == 1:
        pos = len(num) - num.index("1")
    return pos

print(posSetBits(2))
print(posSetBits(8))
print(posSetBits(5))