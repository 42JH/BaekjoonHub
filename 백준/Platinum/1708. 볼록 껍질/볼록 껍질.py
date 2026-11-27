import sys
input = sys.stdin.readline

n = int(input())
pts = sorted(tuple(map(int, input().split())) for _ in range(n))

def ccw(o, a, b):
	return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

lower = []
for p in pts:
	while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) <= 0:
		lower.pop()
	lower.append(p)
upper = []
for p in reversed(pts):
	while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) <= 0:
		upper.pop()
	upper.append(p)
print(len(lower) + len(upper) - 2)
