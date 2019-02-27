# 解锁keychain，以便可以正常的签名应用，
PASSWORD="lieyunye"
security unlock-keychain -p $PASSWORD ~/Library/Keychains/login.keychain

# 获取设备的UDID，用到了之前的 libimobiledevice
UDID=$(idevice_id -l | head -n1)

# 真机运行测试
 xcodebuild -project /Volumes/lyy/work/test/iOS/WebDriverAgent/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=$UDID" test
# /Users/lieyunye/Downloads/Xcode-beta.app/Contents/Developer/usr/bin/xcodebuild -project /Volumes/lyy/work/test/iOS/WebDriverAgent/WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "id=$UDID" test

# 模拟器运行测试
# xcodebuild -project WebDriverAgent.xcodeproj -scheme WebDriverAgentRunner -destination "platform=iOS Simulator,name=iPhone X" test

#iproxy 8100 8100转发端口

