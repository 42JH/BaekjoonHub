import sys
input = sys.stdin.readline

def update(i, d):
	while i < len(tree):
		tree[i] += d
		i += i & -i

def get(i):
	res = 0
	while i > 0:
		res += tree[i]
		i -= i & -i
	return res

t = int(input())
for _ in range(t):
	n, m = map(int, input().split())
	movies = list(map(int, input().split()))
	tree = [0] * (n + m + 1)
	pos = [0] * (n + 1)
	for i in range(1, n + 1):
		pos[i] = m + i
		update(pos[i], 1)
	top = m
	ans = []
	for x in movies:
		ans.append(get(pos[x] - 1))
		update(pos[x], -1)
		pos[x] = top
		update(top, 1)
		top -= 1
	print(*ans)
