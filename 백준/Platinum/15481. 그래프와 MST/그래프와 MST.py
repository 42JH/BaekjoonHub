import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
edges = []
for i in range(m):
	u, v, w = map(int, input().split())
	edges.append((w, u, v, i))

p = list(range(n + 1))
def find(x):
	while p[x] != x:
		p[x] = p[p[x]]
		x = p[x]
	return x

g = [[] for _ in range(n + 1)]
used = [False] * m
total = 0
for w, u, v, i in sorted(edges):
	a, b = find(u), find(v)
	if a != b:
		p[a] = b
		total += w
		used[i] = True
		g[u].append((v, w))
		g[v].append((u, w))

LOG = 18
par = [[0] * (n + 1) for _ in range(LOG)]
mx = [[0] * (n + 1) for _ in range(LOG)]
dep = [0] * (n + 1)
visited = [False] * (n + 1)
visited[1] = True
q = deque([1])
while q:
	u = q.popleft()
	for v, w in g[u]:
		if not visited[v]:
			visited[v] = True
			dep[v] = dep[u] + 1
			par[0][v] = u
			mx[0][v] = w
			q.append(v)

for k in range(1, LOG):
	for v in range(1, n + 1):
		mid = par[k - 1][v]
		par[k][v] = par[k - 1][mid]
		mx[k][v] = max(mx[k - 1][v], mx[k - 1][mid])

def path_max(u, v):
	res = 0
	if dep[u] < dep[v]:
		u, v = v, u
	diff = dep[u] - dep[v]
	for k in range(LOG):
		if diff >> k & 1:
			res = max(res, mx[k][u])
			u = par[k][u]
	if u == v:
		return res
	for k in range(LOG - 1, -1, -1):
		if par[k][u] != par[k][v]:
			res = max(res, mx[k][u], mx[k][v])
			u = par[k][u]
			v = par[k][v]
	return max(res, mx[0][u], mx[0][v])

out = []
for w, u, v, i in edges:
	if used[i]:
		out.append(total)
	else:
		out.append(total - path_max(u, v) + w)
print('\n'.join(map(str, out)))