import sys
input = sys.stdin.readline

n = int(input())
seat = [[0] * n for _ in range(n)]
like = {}
order = []
for _ in range(n * n):
	data = list(map(int, input().split()))
	order.append(data[0])
	like[data[0]] = set(data[1:])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for s in order:
	best = None
	for i in range(n):
		for j in range(n):
			if seat[i][j]:
				continue
			fav = 0
			blank = 0
			for k in range(4):
				ni, nj = i + dx[k], j + dy[k]
				if 0 <= ni < n and 0 <= nj < n:
					if seat[ni][nj] in like[s]:
						fav += 1
					elif seat[ni][nj] == 0:
						blank += 1
			cand = (-fav, -blank, i, j)
			if best is None or cand < best:
				best = cand
	seat[best[2]][best[3]] = s

score = [0, 1, 10, 100, 1000]
ans = 0
for i in range(n):
	for j in range(n):
		s = seat[i][j]
		cnt = 0
		for k in range(4):
			ni, nj = i + dx[k], j + dy[k]
			if 0 <= ni < n and 0 <= nj < n and seat[ni][nj] in like[s]:
				cnt += 1
		ans += score[cnt]
print(ans)
