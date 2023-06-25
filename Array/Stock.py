#  Best Time to Buy and Sell Stock

def profit(arr):
    costPrice = arr[0]
    for i in range(len(arr)):
        if arr[i] < costPrice:
            buyDay = i
            costPrice = arr[i]
    sellingPrice = costPrice
    for i in range(buyDay, len(arr)):
        if arr[i] > sellingPrice:
            sellingPrice = arr[i]
    profitValue = sellingPrice - costPrice
    return profitValue

arr=[7,1,5,3,6,4]
print(profit(arr))