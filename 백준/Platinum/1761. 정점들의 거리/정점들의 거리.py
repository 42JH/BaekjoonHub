import sys
from collections import deque
input = sys.stdin.readline
LOG = 16

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))
	graph[b].append((a, c))

parent = [[0] * (n + 1) for _ in range(LOG)]
depth = [-1] * (n + 1)
dist = [0] * (n + 1)
depth[1] = 0
q = deque([1])
while q:
	x = q.popleft()
	for y, c in graph[x]:
		if depth[y] == -1:
			depth[y] = depth[x] + 1
			dist[y] = dist[x] + c
			parent[0][y] = x
			q.append(y)

for i in range(1, LOG):
	for j in range(1, n + 1):
		parent[i][j] = parent[i - 1][parent[i - 1][j]]

def lca(a, b):
	if depth[a] > depth[b]:
		a, b = b, a
	for i in range(LOG - 1, -1, -1):
		if depth[b] - depth[a] >= 1 << i:
			b = parent[i][b]
	if a == b:
		return a
	for i in range(LOG - 1, -1, -1):
		if parent[i][a] != parent[i][b]:
			a = parent[i][a]
			b = parent[i][b]
	return parent[0][a]

m = int(input())
ans = []
for _ in range(m):
	a, b = map(int, input().split())
	ans.append(dist[a] + dist[b] - 2 * dist[lca(a, b)])
print('\n'.join(map(str, ans)))
