import sys
input = sys.stdin.readline

while True:
	h = list(map(int, input().split()))
	if h[0] == 0:
		break
	n = h[0]
	h = h[1:] + [0]
	st = []
	ans = 0
	for i in range(n + 1):
		while st and h[st[-1]] >= h[i]:
			height = h[st.pop()]
			width = i if not st else i - st[-1] - 1
			ans = max(ans, height * width)
		st.append(i)
	print(ans)