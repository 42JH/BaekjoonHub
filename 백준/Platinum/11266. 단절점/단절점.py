import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

disc = [0] * (v + 1)
low = [0] * (v + 1)
cut = [False] * (v + 1)
timer = 0
for root in range(1, v + 1):
	if disc[root]:
		continue
	timer += 1
	disc[root] = low[root] = timer
	children = 0
	stack = [(root, 0, 0)]
	while stack:
		x, p, i = stack[-1]
		if i < len(graph[x]):
			stack[-1] = (x, p, i + 1)
			y = graph[x][i]
			if y == p:
				continue
			if disc[y]:
				low[x] = min(low[x], disc[y])
			else:
				timer += 1
				disc[y] = low[y] = timer
				stack.append((y, x, 0))
				if x == root:
					children += 1
		else:
			stack.pop()
			if stack:
				u = stack[-1][0]
				low[u] = min(low[u], low[x])
				if u != root and low[x] >= disc[u]:
					cut[u] = True
	if children >= 2:
		cut[root] = True

res = [i for i in range(1, v + 1) if cut[i]]
print(len(res))
print(*res)
