#finding max element in an array of random numbers

def max_inarr(arr):
    max = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
            
    return max

arr = [3, 6, 2, 8, 4, 10, 9, 15, 12, 7]
print("The max element in the array is: ", max_inarr(arr))
    