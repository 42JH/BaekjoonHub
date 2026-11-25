import sys
input = sys.stdin.readline

MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, int(MAX ** 0.5) + 1):
	if is_prime[i]:
		for j in range(i * i, MAX + 1, i):
			is_prime[j] = False

primes = []
cnt = [0] * (MAX + 1)
for i in range(2, MAX + 1):
	if is_prime[i]:
		primes.append(i)
	cnt[i] = len(primes)

n = int(input())
ans = []
for _ in range(n):
	a, b = map(int, input().split())
	k = cnt[b] - cnt[a - 1]
	if k % 2 == 0:
		ans.append(-1)
	else:
		ans.append(primes[cnt[a - 1] + k // 2])
print('\n'.join(map(str, ans)))
