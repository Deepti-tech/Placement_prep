def countSetBits(num):
    num = format(num, 'b')
    count = num.count('1')
    return count

n = int(input("number: "))
print(countSetBits(n))