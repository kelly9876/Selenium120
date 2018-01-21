#0.打开浏览器
import time
from selenium import webdriver
driver = webdriver.Chrome()

#1.打开登录页面
driver.get("http://172.31.4.74/index.php?m=user&c=public&a=login")

#2.输入用户名
driver.find_element_by_id("username").send_keys("chengcheng01")

#3.输入密码
driver.find_element_by_name("password").send_keys("135790")

#4.点击登录
driver.find_element_by_class_name("login_btn").click()