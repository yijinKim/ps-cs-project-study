# Search Algorithms


## 이분탐색(Binary Search)

- **개념** : __정렬되어있는__ 리스트에서 탐색 범위 좁히며 탐색
- **특징**
    - 정렬됐을때 사용가능
    - 전체에서 중간값 선택, 크면 중간값 이후, 작으면 이전에서 값 탐색 반복
    - O(logn)

- **장점**
    - 선형탐색(O(n))보다 빠르게 탐색 가능
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

- 이진탐색 라이브러리 -> **bisect**
bisect_left(arr, x) : 정렬된 순서 유지, arr에 데이터 x 삽입할 가장 왼쪽 인덱스 리턴
bisect_right(arr, x) : 정렬된 순서 유지, arr에 데이터 x 삽입할 가장 오른쪽 인덱스 리턴

```python
from bisect import bisect_left, bisect_right
arr = [1,2,4,4,8]
x = 4

print(bisect_left(arr, x)) # 2
print(bisect_right(arr, x)) # 4
```




-------------
###Reference
https://velog.io/@kimdukbae/%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89-%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-Binary-Search
                    




## 해시테이블

- 해시(Hash) : (Key, Value)로 저장하는 자료구조

- 해시함수를 사용해 키를 해시값으로 매핑하고 해시값으로 데이터를 저장

- ex) 원하는 크기의 배열(0-99)생성 → (711, "김해시")를 해시함수로 변환 → 711 = 30 → 인덱스 30에 (711, "김해시")저장

- 해시함수 : 특정값을 원하는 범위의 자연수로 바꿔주는 함수
	h(x) = x mod m (x : 입력값, m: 해시테이블 크기)
	
- **장점**
	- key-value가 1:1 -> 삽입,삭제,검색 : O(1)
	
- **단점**
	- 해시충돌
	- 공간효율 낮음

- **해시충돌**
  h(a) = 2, h(b) = 2인 경우, O(n)

- Solution

  1. Chaining

     기존값과 새로운 값을 연결리스트로 연결 ->추가적인 메모리 사용

     - 공간 잡아놓을 필요없음.
     - 손쉽게 삭제 가능.
     - 많이 연결되면 효율 떨어짐.

  2. Open Addressing

     충돌 발생 시 탐사로 빈공간 찾는 방식 -> 빈 공간 활용

     고정폭식 이동하는 방법, 폭을 제곱으로 저장하는 방법(2^2, 3^2,...), 해시값 한번 더 해싱해서 할당방법




## DFS 깊이 우선 탐색(Depth-First Search)
- 모든 노드 방문하고자 할 때 사용
- 현 경로상 노드를 기억하므로 적은 메모리 사용
- deep한 단계에서 빠름

- 해가 없으면 단계 끝날 때까지 탐색 -> 미리 정한 임의의 깊이까짐나 탐색 후 빠져나와 다른 경로 탐색하도록 효율성 높여야함.
- 최단 경로라는 보장 없음.

**작동 원리**

1. using Stack

   ```tex
   방문 표시 후 스택에 push
   스택에 아무 노드가 없을 때까지:
   스택 가장 위 노드 pop
   방문 표시
   인접 노드 보면서:
   	아직 방문 안했으면:
   		방문 표시
   		스택 push
   ```

```python
def dfs(start):
	visited = []
	stack = [start]
	while stack:
		node = stack.pop()
		if node not in visited:
			visited.append(node)
			for w in graph[node]:
				stack.append(w)
			# stack.extend(graph[node])  # for문(2줄) 대신
	return visited
```

2. using Recursion

   ```tex
   방문 처리
   현재 노드와 연결된 다른 노드
   방문 안했으면
   재귀적 방문
   ```

```python
def dfs(graph, node, visited):
	visited[node] = True
	for i in graph[node]:
		if not visited[i]:
			dfs(graph, i, visited)
```

##  BFS 너비 우선 탐색(Dreadth-First Search)
- 재귀적으로 동작 X
- 최단거리 문제
- queue/deque 활용

- 답 경로가 여러개이면 최단경로 보장.
- 최단경로 존재하면 무한히 깊어져도 답 가능.

- 기억공간 많이 필요
- 모든 그래프 탐색 후 실패 가능
- 무한 그래프이면 해 못찾고 종료도 불가능.

**작동 원리**

```tex
시작 노드 방문 표시, 큐에 넣기
큐에 아무 노드 없을 때까지:
큐 가장 앞 노드 꺼내기
인접 노드 돌면서
	처음 방문이면
		방문 표시
		큐에 넣기
```

```python
def bfs(graph, start, visited):
	queue = deque([start])
	visited[start] = True
	while queue:
		v = queue.popleft()
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True
```