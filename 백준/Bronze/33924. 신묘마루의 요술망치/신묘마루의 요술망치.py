r, c = map(int, input().split())
k = int(input())
s = input().strip()

ring = [(1, 1), (1, 2), (2, 2), (3, 2), (4, 2), (4, 1), (3, 1), (2, 1)]

for op in s:
	if op == 'A':
		r = r + 2 if r <= 2 else r - 2
	elif op == 'B':
		if r == 1 or r == 3:
			r += 1
		else:
			r -= 1
		c = 3 - c
	elif op == 'C':
		r = 5 - r
		c = 3 - c
	else:
		i = ring.index((r, c))
		r, c = ring[(i + 1) % 8]

print(r, c)
