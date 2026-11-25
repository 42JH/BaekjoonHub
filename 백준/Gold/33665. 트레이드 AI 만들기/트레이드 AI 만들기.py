w = [list(map(int, input().split())) for _ in range(10)]
own = input().strip()
trade = input().strip()
mortgage = input().strip()
my_cash = int(input())
op_cash = int(input())
my_give = int(input())
op_give = int(input())
A = int(input())
B = int(input())

def value(owner, cash, who):
	res = 0
	for i in range(10):
		cnt = 0
		for j in range(4):
			if owner[4 * i + j] == who:
				cnt += 1
		if cnt > 0:
			res += w[i][cnt - 1]
	res += cash * A // 100
	for k in range(40):
		if owner[k] == who and mortgage[k] == '1':
			res -= B
	return res

after = list(own)
for k in range(40):
	if trade[k] == '1':
		after[k] = '1'
	elif trade[k] == '2':
		after[k] = '2'

before_diff = value(own, my_cash, '1') - value(own, op_cash, '2')
my_after = my_cash - my_give + op_give
op_after = op_cash - op_give + my_give
after_diff = value(after, my_after, '1') - value(after, op_after, '2')

print('YES' if after_diff >= before_diff else 'NO')
