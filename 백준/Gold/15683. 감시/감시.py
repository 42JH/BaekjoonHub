import sys
input = sys.stdin.readline

n, m = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
modes = {
	1: [[0], [1], [2], [3]],
	2: [[0, 2], [1, 3]],
	3: [[0, 1], [1, 2], [2, 3], [3, 0]],
	4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
	5: [[0, 1, 2, 3]],
}
cctv = [(i, j, office[i][j]) for i in range(n) for j in range(m) if 1 <= office[i][j] <= 5]

def watch(board, x, y, d):
	changed = []
	nx, ny = x + dx[d], y + dy[d]
	while 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 6:
		if board[nx][ny] == 0:
			board[nx][ny] = 7
			changed.append((nx, ny))
		nx += dx[d]
		ny += dy[d]
	return changed

ans = n * m

def dfs(idx):
	global ans
	if idx == len(cctv):
		ans = min(ans, sum(row.count(0) for row in office))
		return
	x, y, t = cctv[idx]
	for mode in modes[t]:
		changed = []
		for d in mode:
			changed += watch(office, x, y, d)
		dfs(idx + 1)
		for cx, cy in changed:
			office[cx][cy] = 0

dfs(0)
print(ans)
