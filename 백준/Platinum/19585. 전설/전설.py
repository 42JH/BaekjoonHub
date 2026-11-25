import sys
input = sys.stdin.readline

c, n = map(int, input().split())
trie = {}
for _ in range(c):
	cur = trie
	for ch in input().strip():
		if ch not in cur:
			cur[ch] = {}
		cur = cur[ch]
	cur['end'] = True

nick = set()
for _ in range(n):
	nick.add(input().strip())

q = int(input())
ans = []
for _ in range(q):
	s = input().strip()
	cur = trie
	flag = False
	for i in range(len(s)):
		if s[i] not in cur:
			break
		cur = cur[s[i]]
		if 'end' in cur and s[i + 1:] in nick:
			flag = True
			break
	if flag:
		ans.append('Yes')
	else:
		ans.append('No')
print('\n'.join(ans))
