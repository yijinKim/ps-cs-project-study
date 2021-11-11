arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# Solution 1
def quick(arr, start, end):
    if start >= end:
        return
    pivot, left, right = start, start+1, end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quick(arr, start, right-1)
    quick(arr, right+1, end)
    

quick(arr, 0, len(arr)-1)
print(arr)

# Solution 2
def quick(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    tail = arr[1:]
    
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    return quick(left_side) + [pivot] + quick(right_side)
    

# quick(arr, 0, len(arr)-1)
print(quick(arr))