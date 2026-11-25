import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph = [[] for _ in range(v + 1)]
rev = [[] for _ in range(v + 1)]
for _ in range(e):
	a, b = map(int, input().split())
	graph[a].append(b)
	rev[b].append(a)

visited = [False] * (v + 1)
order = []
for s in range(1, v + 1):
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

comp = [0] * (v + 1)
scc = []
for s in reversed(order):
	if comp[s]:
		continue
	comp[s] = len(scc) + 1
	group = [s]
	stack = [s]
	while stack:
		x = stack.pop()
		for y in rev[x]:
			if not comp[y]:
				comp[y] = comp[s]
				group.append(y)
				stack.append(y)
	scc.append(sorted(group))

scc.sort()
print(len(scc))
for group in scc:
	print(*group, -1)
