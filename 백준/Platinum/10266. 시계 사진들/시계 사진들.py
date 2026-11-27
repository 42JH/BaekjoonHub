import sys
input = sys.stdin.readline

SIZE = 360000
n = int(input())
a = [0] * SIZE
b = [0] * SIZE
for x in map(int, input().split()):
	a[x] = 1
for x in map(int, input().split()):
	b[x] = 1

text = a + a
pattern = b
fail = [0] * SIZE
j = 0
for i in range(1, SIZE):
	while j > 0 and pattern[i] != pattern[j]:
		j = fail[j - 1]
	if pattern[i] == pattern[j]:
		j += 1
		fail[i] = j

found = False
j = 0
for i in range(len(text)):
	while j > 0 and text[i] != pattern[j]:
		j = fail[j - 1]
	if text[i] == pattern[j]:
		if j == SIZE - 1:
			found = True
			break
		j += 1
print('possible' if found else 'impossible')
