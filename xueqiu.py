import wda
import time
import random

c = wda.Client()

print (c.status())

s = c.session('com.xueqiu')# 启动雪球app

print (s.bundle_id)

print (s.window_size())
# e = s(name='WRReadingViewController')#http://localhost:8100/inspector 找到显示文字的控件
i = 0
while i < 0.8 * 60 * 60:
	randomValue = random.randint(1,10)
	randomValue = 10
	print (randomValue)
	time.sleep(randomValue)
	print (time.strftime('%Y-%m-%d-%H-%I-%M-%S',time.localtime(time.time())))
	# s.swipe_down()
	s.swipe(300, 300, 300, 600, 0.5)
	i += 1



