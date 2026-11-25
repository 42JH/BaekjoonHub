import sys
input = sys.stdin.readline

n = int(input())
X, Y, C = [], [], []
for _ in range(n):
	x, y, c = map(int, input().split())
	X.append(x)
	Y.append(y)
	C.append(c)

rest = list(range(1, n))
dist = [abs(X[j] - X[0]) + abs(Y[j] - Y[0]) + C[j] + C[0] for j in rest]
mst = 0
while rest:
	i = dist.index(min(dist))
	mst += dist[i]
	u = rest[i]
	rest[i] = rest[-1]
	rest.pop()
	dist[i] = dist[-1]
	dist.pop()
	ux, uy, uc = X[u], Y[u], C[u]
	dist = [min(d, abs(X[j] - ux) + abs(Y[j] - uy) + C[j] + uc) for d, j in zip(dist, rest)]

s = sum(C)
print(*[mst - s + c for c in C])
