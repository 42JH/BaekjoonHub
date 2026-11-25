import sys
input = sys.stdin.readline

L = int(input())
s = input().rstrip()

fail = [0] * L
j = 0
for i in range(1, L):
	while j > 0 and s[i] != s[j]:
		j = fail[j - 1]
	if s[i] == s[j]:
		j += 1
		fail[i] = j
print(L - fail[-1])