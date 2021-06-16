import random
start = input('請決定隨機數字起始值: ')
end = input('請決定隨機數字結束值: ')
start = int(start)
end = int(end)
r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1快寫法
	num = input('你猜數字多少? ')
	num = int(num)
	if num == r:
		print('你猜對了! ')
		print('這是你猜的第', count, '次')
		break
	elif num < r:
		print('你猜錯了! 答案比較大!')
	elif num > r:
		print('你猜錯啦! 答案比較小')
	print('這是你猜的第', count, '次') #不寫在 if 架構裡面,是因為寫在裡面的話要寫三次,重複了
