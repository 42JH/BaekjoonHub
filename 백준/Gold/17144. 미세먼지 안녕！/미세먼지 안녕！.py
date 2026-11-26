import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
up = [i for i in range(r) if room[i][0] == -1][0]
down = up + 1

cnt = [[0] * c for _ in range(r)]
for i in range(r):
	for j in range(c):
		for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
			ni, nj = i + di, j + dj
			if 0 <= ni < r and 0 <= nj < c and room[ni][nj] != -1:
				cnt[i][j] += 1

def spread():
	global room
	f = [[v // 5 if v > 0 else 0 for v in row] for row in room]
	zero = [0] * c
	new = []
	for i in range(r):
		above = f[i - 1] if i > 0 else zero
		below = f[i + 1] if i < r - 1 else zero
		row = f[i]
		left = [0] + row[:-1]
		right = row[1:] + [0]
		new.append([v - a * k + u + d + l + rr for v, a, k, u, d, l, rr in zip(room[i], row, cnt[i], above, below, left, right)])
	new[up][0] = -1
	new[down][0] = -1
	room = new

def clean():
	for i in range(up - 1, 0, -1):
		room[i][0] = room[i - 1][0]
	for j in range(c - 1):
		room[0][j] = room[0][j + 1]
	for i in range(up):
		room[i][c - 1] = room[i + 1][c - 1]
	for j in range(c - 1, 1, -1):
		room[up][j] = room[up][j - 1]
	room[up][1] = 0

	for i in range(down + 1, r - 1):
		room[i][0] = room[i + 1][0]
	for j in range(c - 1):
		room[r - 1][j] = room[r - 1][j + 1]
	for i in range(r - 1, down, -1):
		room[i][c - 1] = room[i - 1][c - 1]
	for j in range(c - 1, 1, -1):
		room[down][j] = room[down][j - 1]
	room[down][1] = 0

for _ in range(t):
	spread()
	clean()

print(sum(sum(row) for row in room) + 2)