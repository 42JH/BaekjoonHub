import sys
input = sys.stdin.readline

n, c = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
	a, b = map(int, input().split())
	g[a].append(b)
	g[b].append(a)

st = [0] * (n + 1)
par = [0] * (n + 1)
dep = [0] * (n + 1)
dep[c] = 1
order = []
stack = [c]
while stack:
	u = stack.pop()
	order.append(u)
	st[u] = len(order)
	for v in g[u]:
		if v != par[u]:
			par[v] = u
			dep[v] = dep[u] + 1
			stack.append(v)

sz = [1] * (n + 1)
for u in reversed(order):
	sz[par[u]] += sz[u]

bit = [0] * (n + 1)
def add(i):
	while i <= n:
		bit[i] += 1
		i += i & -i

def get(i):
	s = 0
	while i:
		s += bit[i]
		i -= i & -i
	return s

out = []
for _ in range(int(input())):
	t, a = map(int, input().split())
	if t == 1:
		add(st[a])
	else:
		out.append((get(st[a] + sz[a] - 1) - get(st[a] - 1)) * dep[a])
print('\n'.join(map(str, out)))
