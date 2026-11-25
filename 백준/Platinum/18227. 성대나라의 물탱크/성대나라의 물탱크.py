import sys
input = sys.stdin.readline

n, c = map(int, input().split())
g = [[] for _ in range(n + 1)]
for _ in range(n - 1):
	a, b = map(int, input().split())
	g[a].append(b)
	g[b].append(a)

tin = [0] * (n + 1)
tout = [0] * (n + 1)
dep = [0] * (n + 1)
dep[c] = 1
cnt = 0
stack = [c]
while stack:
	u = stack.pop()
	if u < 0:
		tout[-u] = cnt
		continue
	cnt += 1
	tin[u] = cnt
	stack.append(-u)
	for v in g[u]:
		if not dep[v]:
			dep[v] = dep[u] + 1
			stack.append(v)

size = 1
while size < n:
	size *= 2
seg = [0] * (2 * size)

def add(i):
	i += size - 1
	while i:
		seg[i] += 1
		i //= 2

def total(l, r):
	l += size - 1
	r += size
	s = 0
	while l < r:
		if l & 1:
			s += seg[l]
			l += 1
		if r & 1:
			r -= 1
			s += seg[r]
		l //= 2
		r //= 2
	return s

out = []
for _ in range(int(input())):
	t, a = map(int, input().split())
	if t == 1:
		add(tin[a])
	else:
		out.append(total(tin[a], tout[a]) * dep[a])
print('\n'.join(map(str, out)))
