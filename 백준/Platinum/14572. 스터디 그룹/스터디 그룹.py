import sys
input = sys.stdin.readline

n, k, D = map(int, input().split())
st = []
for _ in range(n):
	m, d = map(int, input().split())
	mask = 0
	for a in map(int, input().split()):
		mask |= 1 << (a - 1)
	st.append((d, mask))
st.sort()

cnt = [0] * k
ans = 0
l = 0
for r in range(n):
	d, mask = st[r]
	for b in range(k):
		if mask >> b & 1:
			cnt[b] += 1
	while d - st[l][0] > D:
		for b in range(k):
			if st[l][1] >> b & 1:
				cnt[b] -= 1
		l += 1
	size = r - l + 1
	know = 0
	common = 0
	for x in cnt:
		if x:
			know += 1
		if x == size:
			common += 1
	ans = max(ans, (know - common) * size)
print(ans)
