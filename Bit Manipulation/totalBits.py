def totalSetBits(N):
    total = 0
    for i in range(1, N+1):
        n = format(i, 'b')
        count = n.count('1')
        total += count
    return total

print(totalSetBits(4))
print(totalSetBits(17))