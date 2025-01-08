#below is the code to reverse an array in python
def rev_arr(arr): #define a function and assign a parameter(arr)
    return arr[::-1] #return the reversed array

arr = [3, 6, 2, 8, 4, 10, 9, 15, 12, 7] #sample array to be reversed
print("The reversed array is: ", rev_arr(arr)) #print the reversed array