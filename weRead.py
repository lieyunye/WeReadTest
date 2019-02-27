import wda
import time
import random

c = wda.Client()

print (c.status())

s = c.session('com.tencent.weread')# 启动微信阅读

print (s.bundle_id)

print (s.window_size())
e = s(name='WRReaderViewController')#http://localhost:8100/inspector 找到显示文字的控件
i = 0
while i < 0.8 * 60 * 60:
	randomValue = random.randint(1,10)
	print (randomValue)
	time.sleep(randomValue)
	print (time.strftime('%Y-%m-%d-%H-%I-%M-%S',time.localtime(time.time())))
	e.scroll('right',0.8)
	i += 1



