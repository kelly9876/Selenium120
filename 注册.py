#0.打开浏览器
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://172.31.4.74/index.php?m=user&c=public&a=reg")

#手工注册一个账号,写代码实现输入用户名和密码,点击登录按钮
# driver.find_element_by_link_text("立即注册").click()
# time.sleep(5)
driver.find_element_by_name("username").send_keys("chengcheng01")
driver.find_element_by_name("password").send_keys("135790")
driver.find_element_by_name("userpassword2").send_keys("135790")
driver.find_element_by_name("mobile_phone").send_keys("13529304893")
driver.find_element_by_name("email").send_keys("783@163.com")
driver.find_element_by_class_name("reg_btn").click()