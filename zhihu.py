   
from appium import webdriver


desired_caps = {}
desired_caps['platformName'] = 'Android'                                 # 打开什么平台的app，固定的 > 启动安卓平台
desired_caps['platformVersion'] = '5.1.1'                                # 安卓系统的版本号：adb shell getprop ro.build.version.release
desired_caps['deviceName'] = 'vivo x6plus d'                             # 手机/模拟器的型号：adb shell getprop ro.product.model
desired_caps['appPackage'] = 'com.zhihu.android'                         # app的名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['appActivity'] = '.app.ui.activity.MainActivity'            # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity"
desired_caps['unicodeKeyboard'] = True                                   # 为了支持中文
desired_caps['resetKeyboard'] = True                                     # 设置成appium自带的键盘


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


A = driver.find_element_by_id('com.zhihu.android:id/go_to_btn').click()

username = driver.find_element_by_id('com.zhihu.android:id/email_input_view')
#username.send_keys('18523216163')

driver.set_value(username,"18523216163")

password = driver.find_element_by_id('com.zhihu.android:id/password')
password.send_keys('ljj1996.')


login = driver.find_element_by_id('com.zhihu.android:id/btn_progress').click()


login_success_msg = driver.find_element_by_class_name('android.support.v7.widget.LinearLayoutCompat')

assert login_success_msg.text == ("登陆成功")

#print("Test success!")




