import sys
input = sys.stdin.readline

n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())

ok = [False] * 4
for a, b in p:
	dx, dy = a - x, b - y
	if abs(dx) <= dy: ok[0] = True
	if abs(dx) <= -dy: ok[1] = True
	if abs(dy) <= dx: ok[2] = True
	if abs(dy) <= -dx: ok[3] = True

print('NO' if all(ok) else 'YES')
