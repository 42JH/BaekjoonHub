import sys
input = sys.stdin.readline

MAX = 1000000
tree = [0] * (MAX + 1)

def update(i, d):
	while i <= MAX:
		tree[i] += d
		i += i & -i

def kth(k):
	pos = 0
	step = 1 << 20
	while step:
		if pos + step <= MAX and tree[pos + step] < k:
			pos += step
			k -= tree[pos]
		step >>= 1
	return pos + 1

n = int(input())
ans = []
for _ in range(n):
	q = list(map(int, input().split()))
	if q[0] == 1:
		t = kth(q[1])
		ans.append(t)
		update(t, -1)
	else:
		update(q[1], q[2])
print('\n'.join(map(str, ans)))
