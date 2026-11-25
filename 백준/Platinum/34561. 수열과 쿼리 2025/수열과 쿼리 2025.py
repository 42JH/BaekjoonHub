import sys

MAX = 300000
data = sys.stdin.buffer.read().split()
n = int(data[0])
a = list(map(int, data[1:n + 1]))
m = int(data[n + 1])

parent = list(range(MAX + 1))
value = list(range(MAX + 1))
owner = [0] * (MAX + 1)
for v in a:
	owner[v] = v

def find(x):
	while parent[x] != x:
		parent[x] = parent[parent[x]]
		x = parent[x]
	return x

ans = []
i = n + 2
for _ in range(m):
	if data[i] == b'1':
		x, y = int(data[i + 1]), int(data[i + 2])
		i += 3
		if x == y or owner[x] == 0:
			continue
		if owner[y] == 0:
			owner[y] = owner[x]
			value[owner[x]] = y
		else:
			parent[owner[x]] = owner[y]
		owner[x] = 0
	else:
		z = int(data[i + 1])
		i += 2
		ans.append(value[find(a[z - 1])])
print('\n'.join(map(str, ans)))
