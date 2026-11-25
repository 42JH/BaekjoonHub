import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
empty = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 0]
virus = [(i, j) for i in range(n) for j in range(m) if board[i][j] == 2]

def safe_count():
	lab = [row[:] for row in board]
	q = deque(virus)
	while q:
		x, y = q.popleft()
		for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
			nx, ny = x + dx, y + dy
			if 0 <= nx < n and 0 <= ny < m and lab[nx][ny] == 0:
				lab[nx][ny] = 2
				q.append((nx, ny))
	return sum(row.count(0) for row in lab)

ans = 0
for walls in combinations(empty, 3):
	for x, y in walls:
		board[x][y] = 1
	ans = max(ans, safe_count())
	for x, y in walls:
		board[x][y] = 0
print(ans)
