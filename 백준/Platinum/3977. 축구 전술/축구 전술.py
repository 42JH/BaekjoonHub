import sys

data = sys.stdin.buffer.read().split()
idx = 0
t = int(data[idx])
idx += 1
out = []
for _ in range(t):
	n, m = int(data[idx]), int(data[idx + 1])
	idx += 2
	graph = [[] for _ in range(n)]
	rev = [[] for _ in range(n)]
	edges = []
	for _ in range(m):
		a, b = int(data[idx]), int(data[idx + 1])
		idx += 2
		graph[a].append(b)
		rev[b].append(a)
		edges.append((a, b))

	visited = [False] * n
	order = []
	for s in range(n):
		if visited[s]:
			continue
		visited[s] = True
		stack = [s]
		its = [iter(graph[s])]
		while its:
			for y in its[-1]:
				if not visited[y]:
					visited[y] = True
					stack.append(y)
					its.append(iter(graph[y]))
					break
			else:
				its.pop()
				order.append(stack.pop())

	comp = [-1] * n
	cnt = 0
	for s in reversed(order):
		if comp[s] != -1:
			continue
		comp[s] = cnt
		stack = [s]
		while stack:
			x = stack.pop()
			for y in rev[x]:
				if comp[y] == -1:
					comp[y] = cnt
					stack.append(y)
		cnt += 1

	indeg = [0] * cnt
	for a, b in edges:
		if comp[a] != comp[b]:
			indeg[comp[b]] += 1
	roots = [c for c in range(cnt) if indeg[c] == 0]
	if len(roots) == 1:
		for i in range(n):
			if comp[i] == roots[0]:
				out.append(str(i))
	else:
		out.append('Confused')
	out.append('')
print('\n'.join(out))
