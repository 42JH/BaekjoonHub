import sys
input = sys.stdin.readline

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cmds = list(map(int, input().split()))

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
top, bottom, north, south, west, east = 0, 0, 0, 0, 0, 0

for c in cmds:
	nx, ny = x + dx[c], y + dy[c]
	if not (0 <= nx < n and 0 <= ny < m):
		continue
	x, y = nx, ny
	if c == 1:
		top, east, bottom, west = west, top, east, bottom
	elif c == 2:
		top, west, bottom, east = east, top, west, bottom
	elif c == 3:
		top, north, bottom, south = south, top, north, bottom
	else:
		top, south, bottom, north = north, top, south, bottom

	if board[x][y] == 0:
		board[x][y] = bottom
	else:
		bottom = board[x][y]
		board[x][y] = 0
	print(top)
