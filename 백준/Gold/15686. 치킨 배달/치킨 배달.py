import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
house = []
chicken = []
for i in range(n):
	row = list(map(int, input().split()))
	for j in range(n):
		if row[j] == 1:
			house.append((i, j))
		elif row[j] == 2:
			chicken.append((i, j))

ans = float('inf')
for pick in combinations(chicken, m):
	total = 0
	for hx, hy in house:
		total += min(abs(hx - cx) + abs(hy - cy) for cx, cy in pick)
		if total >= ans:
			break
	ans = min(ans, total)
print(ans)
