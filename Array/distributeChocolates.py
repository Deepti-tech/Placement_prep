# Given an array of N integers where each value represents the number of chocolates in a packet. 
# Each packet can have a variable number of chocolates. 
# There are m students, the task is to distribute chocolate packets such that: 
# Each student gets one packet.
# The difference between the number of chocolates in the packet with maximum chocolates 
# and the packet with minimum chocolates given to the students is minimum.

def distributeChoco(arr, m):
    arr.sort()
    n = len(arr)-1
    diff = arr[n] - arr[0]
    for i in range(n):
        if i+m-1 <= n:
            tempDiff = arr[i+m-1] - arr[i]
            if tempDiff < diff:
                diff = tempDiff
    return diff
            
if __name__ == "__main__":
    try:
        m = int(input("Enter number of children: "))
        print("Enter elements:")
        arr = []
        while True:
            arr.append(int(input()))
    except:
        print(distributeChoco(arr, m))
# 7 3 2 4 9 12 56