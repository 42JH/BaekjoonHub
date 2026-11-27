import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
pos = {}
for i, x in enumerate(b):
	pos[x] = i + 1

tree = [0] * (n + 1)
ans = 0
for i, x in enumerate(a):
	p = pos[x]
	s = 0
	j = p
	while j > 0:
		s += tree[j]
		j -= j & -j
	ans += i - s
	j = p
	while j <= n:
		tree[j] += 1
		j += j & -j
print(ans)
