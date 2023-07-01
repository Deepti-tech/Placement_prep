def power(num):
    pow = 1
    while (pow<=num):
        if pow == num:
            return True
        pow*=2
    return False

print(power(256))
print(power(1))