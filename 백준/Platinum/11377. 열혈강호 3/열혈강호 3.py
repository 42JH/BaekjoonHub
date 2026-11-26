import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
	graph[i] = list(map(int, input().split()))[1:]

work = [0] * (m + 1)

def dfs(x):
	for w in graph[x]:
		if work[w] == 0:
			work[w] = x
			return True
	for w in graph[x]:
		if visited[w]:
			continue
		visited[w] = True
		if dfs(work[w]):
			work[w] = x
			return True
	return False

cnt = 0
visited = [False] * (m + 1)
for i in range(1, n + 1):
	if cnt == m:
		break
	if dfs(i):
		cnt += 1
		visited = [False] * (m + 1)

extra = 0
visited = [False] * (m + 1)
for i in range(1, n + 1):
	if extra == k or cnt + extra == m:
		break
	if dfs(i):
		extra += 1
		visited = [False] * (m + 1)
print(cnt + extra)
