import sys

data = sys.stdin.buffer.read().split()
v, e = int(data[0]), int(data[1])
graph = [[] for _ in range(v + 1)]
for i in range(e):
	a, b = int(data[2 + 2 * i]), int(data[3 + 2 * i])
	graph[a].append(b)
	graph[b].append(a)

disc = [0] * (v + 1)
low = [0] * (v + 1)
bridges = []
timer = 0
for root in range(1, v + 1):
	if disc[root]:
		continue
	timer += 1
	disc[root] = low[root] = timer
	stack = [(root, 0, 0)]
	while stack:
		x, p, i = stack[-1]
		if i < len(graph[x]):
			stack[-1] = (x, p, i + 1)
			y = graph[x][i]
			if y == p:
				continue
			if disc[y]:
				if disc[y] < low[x]:
					low[x] = disc[y]
			else:
				timer += 1
				disc[y] = low[y] = timer
				stack.append((y, x, 0))
		else:
			stack.pop()
			if stack:
				u = stack[-1][0]
				if low[x] < low[u]:
					low[u] = low[x]
				if low[x] > disc[u]:
					bridges.append((min(u, x), max(u, x)))

bridges.sort()
out = [str(len(bridges))]
for a, b in bridges:
	out.append(f'{a} {b}')
print('\n'.join(out))
