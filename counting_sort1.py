def countingSort(arr):
    # Write your code here
    res = [0] * 100
    
    for i in range(len(arr)):
        res[arr[i]] += 1
    
    return res
