import sys
input = sys.stdin.readline

n = int(input())
p = [tuple(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())

q = set()
for a, b in p:
	s, d = (a - x) + (b - y), (a - x) - (b - y)
	if s >= 0 and d <= 0: q.add(0)
	if s <= 0 and d >= 0: q.add(1)
	if s >= 0 and d >= 0: q.add(2)
	if s <= 0 and d <= 0: q.add(3)

print('NO' if len(q) == 4 else 'YES')
