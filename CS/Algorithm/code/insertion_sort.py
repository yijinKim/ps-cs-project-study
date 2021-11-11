arr = [4,2,5,6,1,3]

# Solution 1
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
        else:  # 추가된 부분
            break
    print(arr)

#[2, 4, 5, 6, 1, 3]
#[2, 4, 5, 6, 1, 3]
#[2, 4, 5, 6, 1, 3]
#[1, 2, 4, 5, 6, 3]
#[1, 2, 3, 4, 5, 6]

# Solution 2
for i in range(1, len(arr)):
    j = i
    while j>0 and arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j -= 1
    print(arr)