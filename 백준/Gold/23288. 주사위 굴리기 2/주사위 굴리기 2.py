import sys
from collections import deque
input = sys.stdin.readline

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def count(sx, sy):
	b = board[sx][sy]
	visited = [[False] * m for _ in range(n)]
	visited[sx][sy] = True
	q = deque([(sx, sy)])
	cnt = 1
	while q:
		x, y = q.popleft()
		for i in range(4):
			nx, ny = x + dx[i], y + dy[i]
			if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == b:
				visited[nx][ny] = True
				cnt += 1
				q.append((nx, ny))
	return cnt

top, bottom, north, south, west, east = 1, 6, 2, 5, 4, 3
x, y, d = 0, 0, 0
ans = 0
for _ in range(k):
	nx, ny = x + dx[d], y + dy[d]
	if not (0 <= nx < n and 0 <= ny < m):
		d = (d + 2) % 4
		nx, ny = x + dx[d], y + dy[d]
	x, y = nx, ny

	if d == 0:
		top, east, bottom, west = west, top, east, bottom
	elif d == 1:
		top, south, bottom, north = north, top, south, bottom
	elif d == 2:
		top, west, bottom, east = east, top, west, bottom
	else:
		top, north, bottom, south = south, top, north, bottom

	ans += board[x][y] * count(x, y)

	if bottom > board[x][y]:
		d = (d + 1) % 4
	elif bottom < board[x][y]:
		d = (d + 3) % 4
print(ans)
