import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
sea = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
	for j in range(n):
		if sea[i][j] == 9:
			x, y = i, j
			sea[i][j] = 0

size = 2
eat = 0
time = 0
while True:
	dist = [[-1] * n for _ in range(n)]
	dist[x][y] = 0
	q = deque([(x, y)])
	fish = []
	while q:
		cx, cy = q.popleft()
		for dx, dy in ((-1, 0), (0, -1), (0, 1), (1, 0)):
			nx, ny = cx + dx, cy + dy
			if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1 and sea[nx][ny] <= size:
				dist[nx][ny] = dist[cx][cy] + 1
				q.append((nx, ny))
				if 0 < sea[nx][ny] < size:
					fish.append((dist[nx][ny], nx, ny))
	if not fish:
		break
	d, x, y = min(fish)
	time += d
	sea[x][y] = 0
	eat += 1
	if eat == size:
		size += 1
		eat = 0
print(time)
