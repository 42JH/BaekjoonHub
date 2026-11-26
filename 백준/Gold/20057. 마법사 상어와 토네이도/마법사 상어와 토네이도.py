import sys
input = sys.stdin.readline

n = int(input())
sand = [list(map(int, input().split())) for _ in range(n)]

left = [(-1, 1, 1), (1, 1, 1), (-1, 0, 7), (1, 0, 7), (-2, 0, 2), (2, 0, 2),
		(-1, -1, 10), (1, -1, 10), (0, -2, 5)]
spread = [left]
for _ in range(3):
	spread.append([(-b, a, p) for a, b, p in spread[-1]])
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

out = 0

def blow(x, y, d):
	global out
	total = sand[x][y]
	if total == 0:
		return
	moved = 0
	for a, b, p in spread[d]:
		amount = total * p // 100
		moved += amount
		nx, ny = x + a, y + b
		if 0 <= nx < n and 0 <= ny < n:
			sand[nx][ny] += amount
		else:
			out += amount
	ax, ay = x + dx[d], y + dy[d]
	rest = total - moved
	if 0 <= ax < n and 0 <= ay < n:
		sand[ax][ay] += rest
	else:
		out += rest
	sand[x][y] = 0

x = y = n // 2
d = 0
length = 1
while True:
	for _ in range(2):
		for _ in range(length):
			x += dx[d]
			y += dy[d]
			blow(x, y, d)
			if x == 0 and y == 0:
				print(out)
				exit()
		d = (d + 1) % 4
	length += 1
