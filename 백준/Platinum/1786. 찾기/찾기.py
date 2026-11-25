import sys
input = sys.stdin.readline

T = input().rstrip('\n')
P = input().rstrip('\n')

fail = [0] * len(P)
j = 0
for i in range(1, len(P)):
	while j > 0 and P[i] != P[j]:
		j = fail[j - 1]
	if P[i] == P[j]:
		j += 1
		fail[i] = j

res = []
j = 0
for i in range(len(T)):
	while j > 0 and T[i] != P[j]:
		j = fail[j - 1]
	if T[i] == P[j]:
		if j == len(P) - 1:
			res.append(i - len(P) + 2)
			j = fail[j]
		else:
			j += 1
print(len(res))
print(*res)
