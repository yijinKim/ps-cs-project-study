## 해시테이블

- 해시(Hash) : (Key, Value)로 저장하는 자료구조
- 해시함수를 사용해 키를 해시값으로 매핑하고 해시값으로 데이터를 저장
- ex) 원하는 크기의 배열(0-99)생성 → (711, "김해시")를 해시함수로 변환 → 711 = 30 → 인덱스 30에 (711, "김해시")저장
- 해시함수 : 특정값을 원하는 범위의 자연수로 바꿔주는 함수
	$h(x) = x mod m$ (x : 입력값, m: 해시테이블 크기)
- **장점**
	- key-value가 1:1 -> 삽입,삭제,검색 : $O(1)$
- **단점**
	- 해시충돌
	- 공간효율 낮음

### 해시충돌
h(a) = 2, h(b) = 2인 경우, $O(n)$

해결방법1: Chaining
기존값과 새로운 값을 연결리스트로 연결 ->추가적인 메모리 사용
- 공간 잡아놓을 필요없음.
- 손쉽게 삭제 가능.
- 많이 연결되면 효율 떨어짐.

해결방법2: Open Addressing
충돌 발생 시 탐사로 빈공간 찾는 방식 -> 빈 공간 활용
- 고정폭식 이동하는 방법, 폭을 제곱으로 저장하는 방법(2^2, 3^2,...), 해시값 한번 더 해싱해서 할당방법




# DFS
깊이 우선 탐색(Depth-First Search)

- 모든 노드 방문하고자 할 때 사용
- 현 경로상 노드를 기억하므로 적은 메모리 사용
- deep한 단계에서 빠름

- 해가 없으면 단계 끝날 때까지 탐색 -> 미리 정한 임의의 깊이까짐나 탐색 후 빠져나와 다른 경로 탐색하도록 효율성 높여야함.
- 최단 경로라는 보장 없음.

**작동 원리**
1) using Stack

> 방문 표시 후 스택에 push
스택에 아무 노드가 없을 때까지:
	스택 가장 위 노드 pop
	방문 표시
	인접 노드 보면서:
		아직 방문 안했으면:
			방문 표시
			스택 push

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

> 방문 처리
현재 노드와 연결된 다른 노드
방문 안했으면
재귀적 방문

```python
def dfs(graph, node, visited):
	visited[node] = True
	for i in graph[node]:
		if not visited[i]:
			dfs(graph, i, visited)
```

# BFS
너비 우선 탐색(Dreadth-First Search)

- 재귀적으로 동작 X
- 최단거리 문제
- queue/deque 활용

- 답 경로가 여러개이면 최단경로 보장.
- 최단경로 존재하면 무한히 깊어져도 답 가능.

- 기억공간 많이 필요
- 모든 그래프 탐색 후 실패 가능
- 무한 그래프이면 해 못찾고 종료도 불가능.

**작동 원리**
> 시작 노드 방문 표시, 큐에 넣기
큐에 아무 노드 없을 때까지:
	큐 가장 앞 노드 꺼내기
	인접 노드 돌면서
		처음 방문이면
			방문 표시
			큐에 넣기

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