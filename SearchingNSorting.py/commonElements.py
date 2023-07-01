def commonElements(x, y, z):
    common = []
    n1, n2, n3 = len(x), len(y), len(z)
    i = j = k =0
    while (i<n1 and j<n2 and k<n3):
        if (x[i] == y[j] and y[j] == z[k]):
            common.append(x[i])
            i += 1
            j += 1
            k += 1
        elif x[i] > y[j]:
            j += 1
        elif y[j] > z[k]:
            k += 1
        else:
            i += 1
            
    return common

ar1 = [1, 5, 10, 20, 40, 80, 80]
ar2 = [6, 7, 20, 80, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 80, 120]
print(commonElements(ar1, ar2, ar3))