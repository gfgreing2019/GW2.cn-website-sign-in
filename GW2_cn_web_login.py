import time
from selenium import webdriver
# 1.python运行环境(IDE我用pycharm按照提示安装python3),并且安装selenium包(FILE->setting->右侧'+'->搜索selenium->install)

def login(username, password):
    url = 'http://do.gw2.kongzhong.com/kungen/login?backurl=http://do.gw2.kongzhong.com/kungen/&validated=true'
    driver = webdriver.Firefox()            # 2.需要下载一个火狐浏览器放在可执行路径中。
    driver.get(url)
    name_input = driver.find_element_by_class_name('input-username')  # 找到用户名的输入框
    pass_input = driver.find_element_by_class_name('input-password')  # 找到输入密码的输入框
    login_button = driver.find_element_by_class_name('login-btn')  # 找到登录按钮
    time.sleep(1.8)  # 稍微等待，防止触发机器人判定
    name_input.clear()
    name_input.send_keys(username)  # 程序填写用户名
    time.sleep(2.1)
    pass_input.clear()
    pass_input.send_keys(password)  # 程序填写写密码
    time.sleep(1.7)
    login_button.click()  # 点击登录按钮
    switch_button = driver.find_element_by_xpath('/html/body/div[8]/div/ul/li[3]/img')  # 找到切换签到页面按钮
    sgin_button = driver.find_element_by_class_name('sginbtn')  # 找到签到按钮
    time.sleep(1.3)
    switch_button.click()  # 点击转到签到页面
    time.sleep(1.5)
    try:
        sgin_button.click()  # 点击签到
    except BaseException:   #异常处理
        print("error")
    time.sleep(3.5)
    driver.quit()

if __name__ == "__main__":
    name = "*************"  # 3.冒号中填入要签到的账户和密码
    pw = "***********"
    login(name, pw)
# windows 可以加入定时任务； linux服务器可以写入crantab