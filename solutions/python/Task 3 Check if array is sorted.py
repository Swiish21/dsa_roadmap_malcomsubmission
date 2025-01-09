def checkif_arraysorted(arr):
    if arr == sorted(arr):
        return True
    else:
        return False
    
arr = [3, 6, 2, 8, 4, 10, 9, 15, 12, 7]
print(f"{arr} is sorted: {checkif_arraysorted(arr)}")