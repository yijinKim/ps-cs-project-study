arr = [4,2,5,6,1,3]

# Solution 1
a = [3,1,2,5,4,6]

def heap_sort(a):
    for i in range(1, len(a)):
        c = i
        while c!=0:
            r = (c-1) // 2
            if a[r] < a[c]:
                a[r], a[c] = a[c], a[r]
            c = r
    for j in range(len(a)-1, -1, -1):
        a[0], a[j] = a[j], a[0]
        r = 0
        c = 1
        
        while c<j:
            c = 2 * r + 1
            if c < j-1 and a[c] < a[c+1]:
                c += 1
            if c< j and a[r] < a[c]:
                a[r], a[c] = a[c], a[r]
            
            r=c
heap_sort(a)
print(a)

# Solution 2
a = [3,1,2,5,4,6]

def heapify(arr, index, heap_size):
    largest = index 
    left_index = 2 * index + 1 
    right_index = 2 * index + 2 
    if left_index < heap_size and arr[left_index] > arr[largest]: 
        largest = left_index 
    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index 
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest] 
        heapify(arr, largest, heap_size) 
                
def heap_sort(arr): 
    length = len(arr) 
    for i in range(length // 2 - 1, -1, -1):
        heapify(arr, i, length) 
    for i in range(length - 1, 0 , -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i) 
    return arr

heap_sort(a)
print(a)