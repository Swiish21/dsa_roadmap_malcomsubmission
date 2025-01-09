def checkif_arraysorted(arr):
    if arr == sorted(arr):
        return True # if the array is sorted
    else:
        return False # if the array is not sorted
    
arr = [3, 6, 2, 8, 4, 10, 9, 15, 12, 7] # array to check if it is sorted
print(f"{arr} is sorted: {checkif_arraysorted(arr)}") # print the result