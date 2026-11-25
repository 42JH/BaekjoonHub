import sys

data = sys.stdin.buffer.read().split()
n, m, k = int(data[0]), int(data[1]), int(data[2])
pre = [0] * (n + 1)
for i in range(n):
	pre[i + 1] = pre[i] + int(data[3 + i])

b1 = [0] * (n + 2)
b2 = [0] * (n + 2)

def update(tree, i, d):
	while i <= n + 1:
		tree[i] += d
		i += i & -i

def get(tree, i):
	res = 0
	while i > 0:
		res += tree[i]
		i -= i & -i
	return res

def prefix(i):
	return pre[i] + get(b1, i) * i - get(b2, i)

ans = []
idx = 3 + n
for _ in range(m + k):
	if data[idx] == b'1':
		l, r, d = int(data[idx + 1]), int(data[idx + 2]), int(data[idx + 3])
		idx += 4
		update(b1, l, d)
		update(b1, r + 1, -d)
		update(b2, l, d * (l - 1))
		update(b2, r + 1, -d * r)
	else:
		l, r = int(data[idx + 1]), int(data[idx + 2])
		idx += 3
		ans.append(prefix(r) - prefix(l - 1))
print('\n'.join(map(str, ans)))
