import sys
input = sys.stdin.readline

n, m = map(int, input().split())
colors = []
DIV = 10**9 + 7
count = 0

for _ in range(n):
	colors.append(list(input().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for x in range(n):
	for y in range(m):
		for k in range(4):
			nx, ny = x + dx[k], y + dy[k]
			if 0 <= nx < n and 0 <= ny < m:
				if colors[x][y] != colors[nx][ny]:
					count += 1
					break

answer = 2**(n*m-count) % DIV
print(answer)