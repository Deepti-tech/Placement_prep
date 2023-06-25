def minMax(arr):
    arr.sort()
    n = len(arr)
    min = arr[0]
    max = arr[n-1]
    print (min, max)
    
if __name__ == "__main__":
    try:
        arr = []
        print ("Enter the elements:\n")
        while True:
            arr.append(int(input()))
    except: 
        minMax(arr)