import sys

data = sys.stdin.buffer.read().split()
n = int(data[0])
a = list(map(int, data[1:n + 1]))

prefix = [0] * (n + 1)
for i in range(n):
	prefix[i + 1] = prefix[i] + a[i]

left = [0] * n
stack = []
for i in range(n):
	while stack and a[stack[-1]] >= a[i]:
		stack.pop()
	left[i] = stack[-1] + 1 if stack else 0
	stack.append(i)

right = [0] * n
stack = []
for i in range(n - 1, -1, -1):
	while stack and a[stack[-1]] >= a[i]:
		stack.pop()
	right[i] = stack[-1] - 1 if stack else n - 1
	stack.append(i)

ans = 0
for i in range(n):
	ans = max(ans, (prefix[right[i] + 1] - prefix[left[i]]) * a[i])
print(ans)
