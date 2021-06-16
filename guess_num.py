import random
r = random.randint(1, 100)
while True:
	num = input('你猜數字多少? ')
	num = int(num)
	if num == r:
		print('你猜對了! ')
		break
	elif num < r:
		print('你猜錯了! 答案比較大!')
	elif num > r:
		print('你猜錯啦! 答案比較小')
