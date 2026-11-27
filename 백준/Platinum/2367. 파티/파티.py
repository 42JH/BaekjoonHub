import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, k, d = map(int, input().split())
limit = list(map(int, input().split()))
V = n + d + 2
src, sink = 0, V - 1
graph = [[] for _ in range(V)]
to = []
cap = []

def add_edge(u, v, c):
	graph[u].append(len(to))
	to.append(v)
	cap.append(c)
	graph[v].append(len(to))
	to.append(u)
	cap.append(0)

for i in range(1, n + 1):
	add_edge(src, i, k)
	for t in list(map(int, input().split()))[1:]:
		add_edge(i, n + t, 1)
for t in range(1, d + 1):
	add_edge(n + t, sink, limit[t - 1])

def bfs():
	global level
	level = [-1] * V
	level[src] = 0
	q = deque([src])
	while q:
		x = q.popleft()
		for e in graph[x]:
			if cap[e] > 0 and level[to[e]] == -1:
				level[to[e]] = level[x] + 1
				q.append(to[e])
	return level[sink] != -1

def dfs(x, f):
	if x == sink:
		return f
	while it[x] < len(graph[x]):
		e = graph[x][it[x]]
		y = to[e]
		if cap[e] > 0 and level[y] == level[x] + 1:
			pushed = dfs(y, min(f, cap[e]))
			if pushed:
				cap[e] -= pushed
				cap[e ^ 1] += pushed
				return pushed
		it[x] += 1
	return 0

total = 0
while bfs():
	it = [0] * V
	while True:
		f = dfs(src, float('inf'))
		if f == 0:
			break
		total += f
print(total)
