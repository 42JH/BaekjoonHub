import sys
input = sys.stdin.readline

n = int(input())
P = [tuple(map(int, input().split())) for _ in range(n)]

edges = []
for i in range(n):
	for j in range(i + 1, n):
		edges.append((abs(P[i][0] - P[j][0]) + abs(P[i][1] - P[j][1]) + P[i][2] + P[j][2], i, j))
edges.sort()

p = list(range(n))
def find(x):
	while p[x] != x:
		p[x] = p[p[x]]
		x = p[x]
	return x

mst = 0
for c, i, j in edges:
	a, b = find(i), find(j)
	if a != b:
		p[a] = b
		mst += c

s = sum(c for x, y, c in P)
print(*[mst - s + c for x, y, c in P])
