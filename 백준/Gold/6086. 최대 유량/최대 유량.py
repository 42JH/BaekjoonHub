import sys
from collections import deque
input = sys.stdin.readline

def idx(c):
	if 'A' <= c <= 'Z':
		return ord(c) - ord('A')
	return ord(c) - ord('a') + 26

SIZE = 52
cap = [[0] * SIZE for _ in range(SIZE)]
flow = [[0] * SIZE for _ in range(SIZE)]
n = int(input())
for _ in range(n):
	a, b, f = input().split()
	a, b, f = idx(a), idx(b), int(f)
	cap[a][b] += f
	cap[b][a] += f

src, sink = idx('A'), idx('Z')
total = 0
while True:
	prev = [-1] * SIZE
	prev[src] = src
	q = deque([src])
	while q and prev[sink] == -1:
		x = q.popleft()
		for y in range(SIZE):
			if prev[y] == -1 and cap[x][y] - flow[x][y] > 0:
				prev[y] = x
				q.append(y)
	if prev[sink] == -1:
		break
	amount = float('inf')
	y = sink
	while y != src:
		x = prev[y]
		amount = min(amount, cap[x][y] - flow[x][y])
		y = x
	y = sink
	while y != src:
		x = prev[y]
		flow[x][y] += amount
		flow[y][x] -= amount
		y = x
	total += amount
print(total)
