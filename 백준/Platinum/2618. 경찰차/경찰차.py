import sys
input = sys.stdin.readline

n = int(input())
w = int(input())
ev = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(w)]

def dist(p, q):
	return abs(p[0] - q[0]) + abs(p[1] - q[1])

def pos1(i):
	return (1, 1) if i == 0 else ev[i]

def pos2(j):
	return (n, n) if j == 0 else ev[j]

dp1 = [dist((1, 1), ev[1])]
dp2 = [dist((n, n), ev[1])]
arg1 = [0] * (w + 1)
arg2 = [0] * (w + 1)
for k in range(2, w + 1):
	step = dist(ev[k - 1], ev[k])
	c1 = [v + dist(pos1(i), ev[k]) for i, v in enumerate(dp2)]
	c2 = [v + dist(pos2(j), ev[k]) for j, v in enumerate(dp1)]
	i1 = c1.index(min(c1))
	i2 = c2.index(min(c2))
	arg1[k] = i1
	arg2[k] = i2
	dp1 = [v + step for v in dp1] + [c1[i1]]
	dp2 = [v + step for v in dp2] + [c2[i2]]

if min(dp1) <= min(dp2):
	car, other = 1, dp1.index(min(dp1))
	best = min(dp1)
else:
	car, other = 2, dp2.index(min(dp2))
	best = min(dp2)

who = [0] * (w + 1)
k = w
while k >= 1:
	who[k] = car
	if k == 1:
		break
	if other == k - 1:
		if car == 1:
			car, other = 2, arg1[k]
		else:
			car, other = 1, arg2[k]
	k -= 1

print(best)
print('\n'.join(map(str, who[1:])))
