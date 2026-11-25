import sys
from collections import deque

data = sys.stdin.buffer.read().split()
n, m = int(data[0]), int(data[1])
board = [data[2 + i].decode() for i in range(n)]

outside = [[False] * m for _ in range(n)]
q = deque()
for i in range(n):
	for j in range(m):
		if (i == 0 or i == n - 1 or j == 0 or j == m - 1) and board[i][j] == '0':
			outside[i][j] = True
			q.append((i, j))
while q:
	x, y = q.popleft()
	for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
		nx, ny = x + dx, y + dy
		if 0 <= nx < n and 0 <= ny < m and not outside[nx][ny] and board[nx][ny] == '0':
			outside[nx][ny] = True
			q.append((nx, ny))

s = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n):
	row = 0
	for j in range(m):
		if not outside[i][j]:
			row += 1
		s[i + 1][j + 1] = s[i][j + 1] + row

idx = 2 + n
k = int(data[idx])
ans = []
for t in range(k):
	p = idx + 1 + 4 * t
	r1, c1, r2, c2 = int(data[p]), int(data[p + 1]), int(data[p + 2]), int(data[p + 3])
	cnt = s[r2][c2] - s[r1 - 1][c2] - s[r2][c1 - 1] + s[r1 - 1][c1 - 1]
	if cnt == 0:
		ans.append('Yes')
	else:
		ans.append('No ' + str(cnt))
print('\n'.join(ans))
