def dfs_iter(start):
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


def dfs_recursion(graph, node, visited):
	visited[node] = True
	for i in graph[node]:
		if not visited[i]:
			dfs_recursion(graph, i, visited)	


def bfs(graph, start, visited):
	queue = deque([start])
	visited[start] = True
	while queue:
		v = queue.popleft()
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True