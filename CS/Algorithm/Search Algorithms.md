## 이분탐색(Binary Search)

- **개념** : __정렬되어있는__ 리스트에서 탐색 범위 좁히며 탐색
- **특징**
    - 정렬됐을때 사용가능
    - 전체에서 중간값 선택, 크면 중간값 이후, 작으면 이전에서 값 탐색 반복
    - $O(logn)$

- **장점**
    - 선형탐색($O(n)$)보다 빠르게 탐색 가능
- **단점**
    - 정렬되어 있어야함.

```python
def binary_search(target, lst):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return None

def binary_srch(arr, target, start, end):
    if start > end:
        return None    
    mid = (start + end) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_srch(arr, target, start, mid - 1)
    else:
        return binary_srch(arr, target, mid + 1, end)
```

### 이진탐색 라이브러리 - **bisect**
bisect_left(arr, x) : 정렬된 순서 유지, arr에 데이터 x 삽입할 가장 왼쪽 인덱스 리턴
bisect_right(arr, x) : 정렬된 순서 유지, arr에 데이터 x 삽입할 가장 오른쪽 인덱스 리턴

```python
from bisect import bisect_left, bisect_right
arr = [1,2,4,4,8]
x = 4

print(bisect_left(arr, x)) # 2
print(bisect_right(arr, x)) # 4
```

arr  [1]   [2]   [4]   [4]   [8]
idx  (0)   (1)   (2)   (3)   (4)
               |           |
bisect_left(arr, 4) (2)    |
                    bisect_right(arr, 4) (4)




-------------
###Reference
https://velog.io/@kimdukbae/%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89-%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-Binary-Search
                    