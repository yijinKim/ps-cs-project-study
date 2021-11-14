arr = [4,2,5,6,1,3]

for i in range(len(arr)-1):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)

#[1, 2, 5, 6, 4, 3]
#[1, 2, 5, 6, 4, 3]
#[1, 2, 3, 6, 4, 5]
#[1, 2, 3, 4, 6, 5]
#[1, 2, 3, 4, 5, 6]