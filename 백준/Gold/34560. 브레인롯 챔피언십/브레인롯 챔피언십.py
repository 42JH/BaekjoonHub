import sys
input = sys.stdin.readline

n = int(input())
name = []
stat = []
for _ in range(n):
	w = input().split()
	name.append(w[0])
	stat.append(tuple(map(int, w[1:])))

less = []
more = []
for s in range(3):
	order = sorted(range(n), key=lambda i: stat[i][s])
	lo = [0] * n
	hi = [0] * n
	bits = 0
	i = 0
	while i < n:
		j = i
		while j < n and stat[order[j]][s] == stat[order[i]][s]:
			j += 1
		for t in range(i, j):
			lo[order[t]] = bits
		for t in range(i, j):
			bits |= 1 << order[t]
		i = j
	bits = 0
	i = n - 1
	while i >= 0:
		j = i
		while j >= 0 and stat[order[j]][s] == stat[order[i]][s]:
			j -= 1
		for t in range(j + 1, i + 1):
			hi[order[t]] = bits
		for t in range(j + 1, i + 1):
			bits |= 1 << order[t]
		i = j
	less.append(lo)
	more.append(hi)

def win_set(g, l):
	e = [~(g[s] | l[s]) for s in range(3)]
	g1, g2, g3 = g
	l1, l2, l3 = l
	e1, e2, e3 = e
	res = g1 & g2 & (g3 | e3 | l3)
	res |= g1 & g3 & (e2 | l2)
	res |= g2 & g3 & (e1 | l1)
	res |= g1 & e2 & e3
	res |= e1 & g2 & e3
	res |= e1 & e2 & g3
	return res

beat = []
beaten = []
for i in range(n):
	g = [less[s][i] for s in range(3)]
	l = [more[s][i] for s in range(3)]
	beat.append(win_set(g, l))
	beaten.append(win_set(l, g))

white = (1 << n) - 1
on_stack = 0
cycle = False
for st in range(n):
	if cycle:
		break
	if not white >> st & 1:
		continue
	white &= ~(1 << st)
	on_stack |= 1 << st
	stack = [st]
	while stack:
		x = stack[-1]
		if beat[x] & on_stack:
			cycle = True
			break
		nxt = beat[x] & white
		if nxt:
			y = (nxt & -nxt).bit_length() - 1
			white &= ~(1 << y)
			on_stack |= 1 << y
			stack.append(y)
		else:
			on_stack &= ~(1 << x)
			stack.pop()

if cycle:
	print('Paradoxe Absurdo')
else:
	res = sorted(name[i] for i in range(n) if beaten[i] == 0)
	print('\n'.join(res))
