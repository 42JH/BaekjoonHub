import sys
input = sys.stdin.readline

n, k, s = map(int, input().split())
a = list(map(int, input().split()))

if k >= 37 and n >= 37:
	print('MEGA')
	exit()

R = min(k, n)
NEG = -10 ** 18
dp = [s] * (R + 1) + [NEG]
for i in range(n):
	x = a[i]
	dp = [max(v + x if v + x > 0 else NEG, 2 * w) for v, w in zip(dp, dp[1:])] + [NEG]
	if dp[0] <= 0:
		print(-1)
		exit()
	if dp[0] - 500 * (n - i - 1) > 10 ** 11:
		print('MEGA')
		exit()

if dp[0] > 10 ** 11:
	print('MEGA')
else:
	print(dp[0])
