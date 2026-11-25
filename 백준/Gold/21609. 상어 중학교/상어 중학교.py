import sys
from collections import deque
input = sys.stdin.readline

EMPTY = -2
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_group(sx, sy, visited):
	color = board[sx][sy]
	q = deque([(sx, sy)])
	seen = [[False] * n for _ in range(n)]
	seen[sx][sy] = True
	visited[sx][sy] = True
	blocks = [(sx, sy)]
	rainbow = 0
	while q:
		x, y = q.popleft()
		for k in range(4):
			nx, ny = x + dx[k], y + dy[k]
			if 0 <= nx < n and 0 <= ny < n and not seen[nx][ny]:
				if board[nx][ny] == 0 or board[nx][ny] == color:
					seen[nx][ny] = True
					if board[nx][ny] == 0:
						rainbow += 1
					else:
						visited[nx][ny] = True
					blocks.append((nx, ny))
					q.append((nx, ny))
	return blocks, rainbow

def gravity():
	for j in range(n):
		for i in range(n - 2, -1, -1):
			if board[i][j] < 0:
				continue
			x = i
			while x + 1 < n and board[x + 1][j] == EMPTY:
				board[x + 1][j] = board[x][j]
				board[x][j] = EMPTY
				x += 1

def rotate():
	global board
	board = [[board[j][n - 1 - i] for j in range(n)] for i in range(n)]

score = 0
while True:
	visited = [[False] * n for _ in range(n)]
	best = None
	for i in range(n):
		for j in range(n):
			if board[i][j] > 0 and not visited[i][j]:
				blocks, rainbow = find_group(i, j, visited)
				if len(blocks) < 2:
					continue
				key = (len(blocks), rainbow, i, j)
				if best is None or key > best[0]:
					best = (key, blocks)
	if best is None:
		break
	blocks = best[1]
	score += len(blocks) ** 2
	for x, y in blocks:
		board[x][y] = EMPTY
	gravity()
	rotate()
	gravity()
print(score)
