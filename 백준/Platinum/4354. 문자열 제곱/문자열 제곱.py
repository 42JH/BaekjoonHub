import sys
input = sys.stdin.readline

out = []
while True:
	s = input().rstrip('\n')
	if s == '.':
		break
	p = (s + s).find(s, 1)
	out.append(len(s) // p)
print('\n'.join(map(str, out)))
