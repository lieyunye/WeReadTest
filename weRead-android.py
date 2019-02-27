import os
import time
import random

# https://brew.sh 安装homebrew： /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
# 1、安装adb brew cask install android-platform-tools
# 2、adb devices查看哪些设备连接并可用
# 3、授权、打开usb调试


# 无线连接手机
# os.system('adb tcpip 5555') 开启手机5555端口号
#os.popen('adb connect 192.168.20.194:5555')

# adb shell logcat | grep -i ActivityManager 在log中“ActivityManager:Displayed”之后的部分就含有am 命令需要的package和launch activity。
os.system('adb shell am start -n com.tencent.weread/com.tencent.weread.LauncherActivity')

i = 0
while i < 3 * 60 * 60:
	randomValue = random.randint(1,10)
	print (randomValue)
	time.sleep(randomValue)
	print (time.strftime('%Y-%m-%d-%H-%I-%M-%S',time.localtime(time.time())))
	swipe_x1=600
	swipe_y1=800-randomValue
	swipe_x2=300+randomValue
	swipe_y2=800
	cmd = 'adb shell input swipe {x1} {y1} {x2} {y2}'.format(
        x1=swipe_x1,
        y1=swipe_y1,
        x2=swipe_x2,
        y2=swipe_y2
       )
	print(cmd)
	os.system(cmd)
	i += 1



