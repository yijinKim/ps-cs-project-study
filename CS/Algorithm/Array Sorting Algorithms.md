# Array Sorting Algorithms


### 버블정렬

- **개념** : 서로 인접한 두 원소를 비교해 교환하며 정렬하는 알고리즘.
- **특징**
    - 1회전 후에는 가장 큰 원소가 맨 뒤로 이동
    - Stable sort
    - ~~swap이 move보다 더 복잡해 쓰이지 않음.~~
    - 비효율적
- **장점**
    - 간단한 구현 ( 간단한 데이터 정렬에는 사용되기도 함.)
- **단점**
    - ~~순서 안맞는 요소를 인접요소와 교환~~
    - 가장 왼쪽에서 가장 오른쪽으로 이동하려면 모든 요소들과 교환되야함.
    - 최종 위치에 이미 있는 경우에도 교환되는 일 발생 → 불필요한 연산
- **시간 복잡도** : $O(n^2)$ (최선, 평균, 최악 모두 동일)
- **공간복잡도** : $O(1)$ (주어진 배열안에서 교환으로 정렬하는 제자리 정렬)
- 🔨 **개선** 🔨
    - 특정 회차에서 정렬이 완료됐음에도 마지막 회차까지 비교 연산 불필요하게 진행함.
    - 중간 회차에서 데이터 swap이 진행되지 않으면 정렬 완료된 것이므로 연산 종료
    
    ```python
    a = [6,5,3,1,8,7,2,4]
    
    # Solution 1
    for i in range(len(a)-1, 0, -1):
        flag = False
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                flag = True
        if not flag:
            break
    #    print(a)
    
    # Result #
    #[5, 3, 1, 6, 7, 2, 4, 8]
    #[3, 1, 5, 6, 2, 4, 7, 8]
    #[1, 3, 5, 2, 4, 6, 7, 8]
    #[1, 3, 2, 4, 5, 6, 7, 8]
    #[1, 2, 3, 4, 5, 6, 7, 8]
    
    # Solution 2
    end = len(a) -1
    while end > 0:
        last = 0
        for i in range(end):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                last = i
        end = last
    #    print(a)
    
    # Result #
    #[5, 3, 1, 6, 7, 2, 4, 8]
    #[3, 1, 5, 6, 2, 4, 7, 8]
    #[1, 3, 5, 2, 4, 6, 7, 8]
    #[1, 3, 2, 4, 5, 6, 7, 8]
    #[1, 2, 3, 4, 5, 6, 7, 8]
    #[1, 2, 3, 4, 5, 6, 7, 8]
    ```
    

### 선택정렬

- **개념** : 현재 선택된 데이터 이후의 정렬 되지 않은 데이터 중에서 가장 작은(혹은 가장 큰) 데이터를 선택해 현재의 데이터와 위치를 교환하는 방식으로 정렬되는 방식.
- **특징**
    - unstable sort
    - 제자리 정렬
- **시간 복잡도** : $O(n^2)$ (최선, 평균, 최악 모두 동일)
- **공간복잡도** : $O(1)$
- **장점**
    - 자료 이동 횟수가 미리 결정됨.
- **단점**
    - 안정성 x
    - 같은 값의 상대적인 위치가 바뀔 수 있다. ex) [2,1,2,1] - 위치가 역전될수도 있음.

```python
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

```

### 삽입정렬

- **개념** : 자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교 하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘
- **특징**
    - 현재 선택된 데이터의 앞 부분은 이미 정렬됨.
- **장점**
    - 안정한 정렬 방법
    - 레코드 수 적으면 간단해서 유리
    - 대부분 이미 정렬되어있으면 효율적일수도 있다.
- **단점**
    - 비교적 많은 레코드의 이동을 포함
    - 레코드 수 많고 크면 부적합
- **시간복잡도** : $O(n)$ (이동 없이 한 번의 비교만 이뤄지는 최선의 경우) / $O(n^2)$ (역순일 경우)
- **공간복잡도** : $O(1)$

```python
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
```

### 퀵정렬

- **개념** : 리스트를 피벗을 기준으로 분할하고 분할한 리스트를 재귀로 정렬한 후 결합하는 알고리즘.
- **특징**
    - 비교 정렬(다른원소와의 비교만으로 정렬 수행)
    - 분할 정복 알고리즘의 하나
    - 매우 빠른 수행 속도
    - 분할, 정복, 결합
    - 리스트를 비균등하게 분할
- **시간복잡도**
    - $O(nlog_2n)$ : n * 순환호출의 깊이 / 횟수 : $O(log_2n)$ 균등하게 분할
    - $O(n^2)$ : 리스트가 불균형하게 나누어지는 경우(특히, 이미 정렬된 리스트)
- **공간복잡도** : $O(log n)$
- **장점**
    - 빠른 속도
    - 추가 메모리 필요 x
- **단점**
    - 정렬된 리스트라면 수행시간 더 걸림

```python
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
```

> 💡 **선택정렬과 삽입 정렬의 유사한 점과 차이점**
유사점 :k번째 반복 이후, 첫번째 k 요소가 정렬된 순서로 온다는 점
차이점 :Selection Sort는 k+1번째 요소를 찾기 위해 나머지 모든 요소들을 탐색하지만 Insertion Sort는 k+1번째 요소를 배치하는 데 필요한 만큼의 요소만 탐색하기 때문에 훨씬 효율적으로 실행된다.

> **퀵정렬 피벗값 선정 방법**
리스트 맨 앞의 값 or 중앙값 or 랜덤값 하나 or 랜덤값 3개 중 중앙값


### 병합정렬

- **개념** :  리스트를 두개의 균등 크기로 분할하고 부분 리스트를 정렬 후, 두 개의 정렬된 부분 리스트를 합해 전체가 정렬되도록 함.
- **특징**
    - 안정 정렬
    - 분할 정복 알고리즘의 하나
    - 제자리 정렬 x
- **장점**
    - $O(nlog_2n)$ 을 보장함 (균등하게 분할하기 때문 - 데이터 분포에 영향 적게 받음)
- **단점**
    - 추가 배열 공간 필요
    - 레코드 크기 크면 이동횟수 많아져 시간 낭비 큼
- **시간복잡도** : $O(nlog_2n)$ (모두 동일)
- **공간복잡도** : $O(n)$

> **퀵정렬, 병합정렬 차이점**
균등한 분할 여부, 추가배열공간 여부, 공간복잡도


```python
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
```

### 힙정렬

- **개념** :  최대 힙 트리나 최소 힙 트리를 구성해 정렬 하는 방법, 내림차순-최대힙/오름차순-최소힙
- **특징**
    - 힙(heap) : 완전 이진 트리, 우선순위 큐를 위해 만들어진 자료구조
    - heapify
- **장점**
    - 시간복잡도 좋음. -  $O(nlog_2n)$  보장
    - 전체 레코드 정렬 없이 가장 큰 레코드 몇개만 필요할 때 가장 유용함.
- **단점**
    - 조금 느린 편 ( swap이 많아서 시간연산 커짐)
    - unstable
    
- **시간복잡도** : $O(nlog_2n)$ (모두 동일) , 삽입/삭제 : $O(logn)$
- **공간복잡도** : $O(1)$

> **힙소트 vs 퀵소트**
힙소트는 unstable, swap이 많아 연산 시간 많이 걸림, heapify도 해야하므로 퀵소트 is better.

```python
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
```

### 기수정렬

- **개념** : 낮은 자리수부터 비교 정렬.
- **특징**
    - 비교연산 x
    - stable
- **장점**
    - 정렬 속도 빠름.
- **단점**
    - 기수 테이블 크기만한 메모리 필요함. - 중간결과 저장 bucket공간 필요
- **시간복잡도** : $O(nK)$ (K : 원소의 최대값)
- **공간복잡도** : $O(n+K)$

```python
def countingSort(arr, digit):
    n = len(arr)
  
    # 배열의 크기에 맞는 output 배열을 생성하고 10개의 0을 가진 count란 배열을 생성한다. 
    output = [0] * (n)
    count = [0] * (10)
    
    #digit, 자릿수에 맞는 count에 += 1을 한다. 
    for i in range(0, n):
        index = int(arr[i]/digit) 
        count[ (index)%10 ] += 1
 
    # count 배열을 수정해 digit으로 잡은 포지션을 설정한다.  
    for i in range(1,10):
        count[i] += count[i-1]  
        print(i, count[i])
    # 결과 배열, output을 설정한다. 설정된 count 배열에 맞는 부분에 arr원소를 담는다.   
    i = n - 1
    while i >= 0:
        index = int(arr[i]/digit)
        output[ count[ (index)%10 ] - 1] = arr[i]
        count[ (index)%10 ] -= 1
        i -= 1

    #arr를 결과물에 다시 재할당한다.  
    for i in range(0,len(arr)): 
        arr[i] = output[i]
 
# Method to do Radix Sort
def radixSort(arr):
    # arr 배열중에서 maxValue를 잡아서 어느 digit, 자릿수까지 반복하면 될지를 정한다. 
    maxValue = max(arr)  
    #자릿수마다 countingSorting을 시작한다. 
    digit = 1
    while int(maxValue/digit) > 0: 
        countingSort(arr,digit)
        digit *= 10
 
arr = [ 170, 45, 75, 90, 802, 24, 2, 66]
#arr = [4, 2, 1, 5, 7, 2]
radixSort(arr)
 
for i in range(len(arr)):
    print(arr[i], end=" ")
```

### 계수정렬(Counting Sort)

- **개념** : 주어진 배열의 값 범위가 작은 경우 빠른 속도를 갖는 정렬 알고리즘. 최댓값과 입력 배열의 원소 값 개수를 누적합으로 구성한 배열로 정렬을 수행한다.
- **작동 원리**
    1. 리스트의 개수를 인덱스마다 저장
    2. 누적합을 구함
    3. 리스트 거꾸로 탐색 시작
    4. 리스트의 원소를 인덱스로서 계수리스트에서의 값을 해당 위치에 표현함
- **특징**
    - 누적합 구하기 위해 입력 배열의 최대값 필요함
    - stable sort
- **장점**
    - 매우 빠르게 정렬 가능 - 비교 하지 않기 때문
- **단점**
    - 배열 인덱스 사용하기 때문에 정해진 범위에 한정한 정렬
    - 결과 저장할 추가적 메모리 필요
- **시간복잡도** : $O(n+K)$ (K : 원소의 최대값)
- **공간복잡도** : $O(K)$

```python
a = [2,0,1,2,3,0,2]

def counting_sort(list, s_list):
    cnt = [0] * (max(list) + 1)
    
    for i in list:
        cnt[i] += 1
        
    for idx in range(1, len(cnt)):
        cnt[idx] += cnt[idx-1]

    for j in range(len(a)-1, -1, -1):
        s_list[cnt[a[j]] - 1] = a[j]
        cnt[list[j]] -= 1
        
sorted_list = [0] * len(a)        
counting_sort(a, sorted_list)
print(sorted_list)
```
