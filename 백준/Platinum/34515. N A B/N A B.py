import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def go(pos, i, j, tight, started):
	if pos == L:
		if started and i == len(A) and j == len(B):
			return 1
		return 0
	if not tight and started and dp[pos][i][j] != -1:
		return dp[pos][i][j]

	limit = int(N[pos]) if tight else 9
	res = 0
	for d in range(limit + 1):
		nt = tight and d == limit
		if not started:
			if d == 0:
				res += go(pos + 1, 0, 0, nt, False)
				continue
			if L - pos <= M:
				continue
		ni, nj = i, j
		if ni < len(A) and A[ni] == str(d):
			ni += 1
		if nj < len(B) and B[nj] == str(d):
			nj += 1
		res += go(pos + 1, ni, nj, nt, True)

	if not tight and started:
		dp[pos][i][j] = res
	return res

T = int(input())
for _ in range(T):
	N, A, B = input().split()
	L = len(N)
	M = max(len(A), len(B))
	dp = [[[-1] * (len(B) + 1) for _ in range(len(A) + 1)] for _ in range(L)]
	print(go(0, 0, 0, True, False))
