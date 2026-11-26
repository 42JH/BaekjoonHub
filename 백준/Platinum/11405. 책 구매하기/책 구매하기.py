import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
want = list(map(int, input().split()))
have = list(map(int, input().split()))
cost_in = [list(map(int, input().split())) for _ in range(m)]

V = n + m + 2
src, sink = V - 2, V - 1
graph = [[] for _ in range(V)]
to = []
cap = []
cost = []

def add_edge(u, v, c, w):
	graph[u].append(len(to))
	to.append(v)
	cap.append(c)
	cost.append(w)
	graph[v].append(len(to))
	to.append(u)
	cap.append(0)
	cost.append(-w)

for j in range(m):
	add_edge(src, n + j, have[j], 0)
for i in range(n):
	add_edge(i, sink, want[i], 0)
for j in range(m):
	for i in range(n):
		add_edge(n + j, i, INF, cost_in[j][i])

ans = 0
while True:
	dist = [INF] * V
	in_q = [False] * V
	prev = [-1] * V
	dist[src] = 0
	q = deque([src])
	while q:
		x = q.popleft()
		in_q[x] = False
		for e in graph[x]:
			if cap[e] > 0 and dist[x] + cost[e] < dist[to[e]]:
				dist[to[e]] = dist[x] + cost[e]
				prev[to[e]] = e
				if not in_q[to[e]]:
					in_q[to[e]] = True
					q.append(to[e])
	if dist[sink] == INF:
		break
	amount = INF
	v = sink
	while v != src:
		e = prev[v]
		amount = min(amount, cap[e])
		v = to[e ^ 1]
	v = sink
	while v != src:
		e = prev[v]
		cap[e] -= amount
		cap[e ^ 1] += amount
		v = to[e ^ 1]
	ans += amount * dist[sink]
print(ans)
