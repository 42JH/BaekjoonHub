import sys

data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
V = 2 * n
graph = [[] for _ in range(V)]
rev = [[] for _ in range(V)]

def node(x):
	if x > 0:
		return 2 * (x - 1)
	return 2 * (-x - 1) + 1

for i in range(m):
	a, b = node(int(data[2 + 2 * i])), node(int(data[3 + 2 * i]))
	graph[a ^ 1].append(b)
	graph[b ^ 1].append(a)
	rev[b].append(a ^ 1)
	rev[a].append(b ^ 1)

visited = [False] * V
order = []
for s in range(V):
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

comp = [-1] * V
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

ans = []
for i in range(n):
	if comp[2 * i] == comp[2 * i + 1]:
		print(0)
		exit()
	ans.append(1 if comp[2 * i] > comp[2 * i + 1] else 0)
print(1)
print(*ans)
