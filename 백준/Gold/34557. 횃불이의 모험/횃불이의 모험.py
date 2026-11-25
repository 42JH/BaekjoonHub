import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
	for j in range(n):
		if board[i][j] == 2:
			x, y = i, j
event = {}
for key in 'WASD':
	event[key] = input().strip()
keys = input().strip()

move = {'W': (-1, 0), 'A': (0, -1), 'S': (1, 0), 'D': (0, 1)}
order = {'W': 0, 'A': 1, 'S': 2, 'D': 3}

def go(key):
	global x, y
	nx, ny = x + move[key][0], y + move[key][1]
	if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 1:
		x, y = nx, ny

prev = ''
for cur in keys:
	if cur == prev:
		if event[cur] == 'Stay':
			go(cur)
	else:
		up = prev != '' and event[prev] == 'Up'
		down = event[cur] == 'Down'
		if up and down:
			if order[prev] < order[cur]:
				go(prev)
				go(cur)
			else:
				go(cur)
				go(prev)
		elif up:
			go(prev)
		elif down:
			go(cur)
	prev = cur

print(x + 1, y + 1)
