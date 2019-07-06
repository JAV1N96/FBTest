# 1.导入appium的webdriver
from appium import webdriver

def get_driver():
    """
        获取设备driver
    """
    desired_caps = {}
    desired_caps['platformName'] = 'Android'                    # 打开什么平台的app，固定的 > 启动安卓平台
    desired_caps['platformVersion'] = '5.1.1'                   # 安卓系统的版本号：adb shell getprop ro.build.version.release
    desired_caps['deviceName'] = 'vivo x6plus d'                # 手机/模拟器的型号：adb shell getprop ro.product.model
    desired_caps['appPackage'] = 'io.appium.android.apis'       # app的名字：adb shell dumpsys activity | findstr "mFocusedActivity"
    desired_caps['appActivity'] = '.ApiDemos'                   # app的启动页名字：adb shell dumpsys activity | findstr "mFocusedActivity"
    desired_caps['unicodeKeyboard'] = True                      # 为了支持中文
    desired_caps['resetKeyboard'] = True                        # 设置成appium自带的键盘

    # 去打开app，并且返回当前app的操作对象
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    return driver

def test():
    """
        查找单个元素
    """
    # 获取driver
    driver = get_driver()

    #  通过id获取元素:最准确
    app = driver.find_element_by_id("android:id/text1")
    app.click()

    # 返回键
    driver.back()

    # 通过text获取元素
    Animation = driver.find_element_by_android_uiautomator('new UiSelector().text("Animation")')
    Animation.click()

    # 返回键
    driver.back()

    # 通过content-desc来获取元素
    app = driver.find_element_by_accessibility_id("App")
    app.click()

    # 返回键
    driver.back()

    # 通过xpath获取:使用最多
    media = driver.find_element_by_xpath("//android.widget.TextView[@text='Media' and @content-desc='Media']")
    media.click()


if __name__ == "__main__":
    test()