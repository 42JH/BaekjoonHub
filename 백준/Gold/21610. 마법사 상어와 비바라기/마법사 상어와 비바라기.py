import sys
input = sys.stdin.readline

n, m = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
for _ in range(m):
	d, s = map(int, input().split())
	moved = []
	for x, y in clouds:
		nx = (x + dx[d] * s) % n
		ny = (y + dy[d] * s) % n
		water[nx][ny] += 1
		moved.append((nx, ny))

	was_cloud = [[False] * n for _ in range(n)]
	for x, y in moved:
		was_cloud[x][y] = True

	for x, y in moved:
		cnt = 0
		for k in (2, 4, 6, 8):
			nx, ny = x + dx[k], y + dy[k]
			if 0 <= nx < n and 0 <= ny < n and water[nx][ny] > 0:
				cnt += 1
		water[x][y] += cnt

	clouds = []
	for i in range(n):
		for j in range(n):
			if water[i][j] >= 2 and not was_cloud[i][j]:
				water[i][j] -= 2
				clouds.append((i, j))

print(sum(sum(row) for row in water))
