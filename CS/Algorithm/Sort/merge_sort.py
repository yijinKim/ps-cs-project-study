arr = [6, 5, 3, 1, 8, 7, 2, 4]

# Solution 1
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    
    merged = []    
    left = right = 0
    
    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] < right_arr[right]:
            merged.append(left_arr[left])
            left += 1
        else:
            merged.append(right_arr[right])
            right += 1
    merged += left_arr[left:]
    merged += right_arr[right:]
    return merged
print(merge_sort(arr))

# Solution 2
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    left1 = merge_sort(left)
    right1 = merge_sort(right)
    return merge(left1, right1)

def merge(left, right):
    l, r = 0, 0
    answer = []
    
    while (l < len(left)) & (r < len(right)):
        if left[l] < right[r]:
            answer.append(left[l])
            l += 1
        else:
            answer.append(right[r])
            r += 1
    
    while l < len(left):
        answer.append(left[l])
        l += 1
    while r < len(right):
        answer.append(right[r])
        r += 1
    return answer

print(merge_sort(arr))

# Solution 3 - 인덱스 이용해 in-place로 최대한 활용해 최적화
arr = [6, 5, 3, 1, 8, 7, 2, 4]

def merge_sort(arr):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if arr[l] < arr[h]:
                temp.append(arr[l])
                l += 1
            else:
                temp.append(arr[h])
                h += 1

        while l < mid:
            temp.append(arr[l])
            l += 1
        while h < high:
            temp.append(arr[h])
            h += 1

        for i in range(low, high):
            arr[i] = temp[i - low]

    return sort(0, len(arr))

merge_sort(arr)