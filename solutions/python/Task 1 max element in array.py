#finding max element in an array of random numbers

arr = [3, 6, 2, 8, 4, 10, 9, 15, 12, 7]
max = arr[0]

for i in range(1, len(arr)):
    if arr[i] > max:
        max = arr[i]
        
print("The max element in the array is: ", max)