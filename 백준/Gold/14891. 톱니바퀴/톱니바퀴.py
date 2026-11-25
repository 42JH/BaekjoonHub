import sys
from collections import deque
input = sys.stdin.readline

gears = [deque(map(int, input().strip())) for _ in range(4)]
k = int(input())
for _ in range(k):
	num, d = map(int, input().split())
	num -= 1
	dirs = [0] * 4
	dirs[num] = d
	for i in range(num, 0, -1):
		if gears[i][6] != gears[i - 1][2]:
			dirs[i - 1] = -dirs[i]
		else:
			break
	for i in range(num, 3):
		if gears[i][2] != gears[i + 1][6]:
			dirs[i + 1] = -dirs[i]
		else:
			break
	for i in range(4):
		if dirs[i]:
			gears[i].rotate(dirs[i])

ans = 0
for i in range(4):
	if gears[i][0] == 1:
		ans += 1 << i
print(ans)
