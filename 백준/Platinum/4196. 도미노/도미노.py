import sys

data = sys.stdin.buffer.read().split()
idx = 0
t = int(data[idx])
idx += 1
out = []
for _ in range(t):
	n, m = int(data[idx]), int(data[idx + 1])
	idx += 2
	graph = [[] for _ in range(n + 1)]
	rev = [[] for _ in range(n + 1)]
	edges = []
	for _ in range(m):
		a, b = int(data[idx]), int(data[idx + 1])
		idx += 2
		graph[a].append(b)
		rev[b].append(a)
		edges.append((a, b))

	visited = [False] * (n + 1)
	order = []
	for s in range(1, n + 1):
		if visited[s]:
			continue
		visited[s] = True
		stack = [(s, 0)]
		while stack:
			x, i = stack[-1]
			if i < len(graph[x]):
				stack[-1] = (x, i + 1)
				y = graph[x][i]
				if not visited[y]:
					visited[y] = True
					stack.append((y, 0))
			else:
				stack.pop()
				order.append(x)

	comp = [0] * (n + 1)
	cnt = 0
	for s in reversed(order):
		if comp[s]:
			continue
		cnt += 1
		comp[s] = cnt
		stack = [s]
		while stack:
			x = stack.pop()
			for y in rev[x]:
				if not comp[y]:
					comp[y] = cnt
					stack.append(y)

	indeg = [0] * (cnt + 1)
	for a, b in edges:
		if comp[a] != comp[b]:
			indeg[comp[b]] += 1
	out.append(sum(1 for c in range(1, cnt + 1) if indeg[c] == 0))
print('\n'.join(map(str, out)))
