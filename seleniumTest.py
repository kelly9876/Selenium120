#0.打开浏览器
import time
from selenium import webdriver
driver = webdriver.Chrome()

#1.打开登录页面
driver.get("http://172.31.4.74/index.php?m=user&c=public&a=login")

#2.输入用户名
driver.find_element_by_id("username").send_keys("changcheng")
#接下来手工注册一个账号,写代码实现输入用户名和密码,点击登录按钮

#3.输入密码
driver.find_element_by_name("password").send_keys("123654")

#4.点击登录
driver.find_element_by_class_name("login_btn").click()

time.sleep(5)
#driver.find_element_by_link_text("进入商城购物").click()

#账号设置功能测试
#1.账号设置
driver.find_element_by_link_text("账号设置").click()

#2.个人资料
driver.find_element_by_partial_link_text("个人资料").click()

#3.修改个人资料
#xpath中//表示相对路径
#*表示任意元素
#[]表示属性
#@id表示id属性
#driver.find_element_by_xpath("//*[@id=\"true_name\"]")
#xpath的缺点:定位速度很慢

#cssSelector优点:快,定位简单,准确
driver.find_element_by_css_selector("#true_name").clear()
driver.find_element_by_css_selector("#true_name").send_keys("张三")
driver.find_element_by_css_selector("[value=\"2\"]").click()

#selenium不能删除页面元素的属性,只能通过javascript来实现
driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
driver.find_element_by_id("date").clear()
driver.find_element_by_id("date").send_keys("1970-10-25")
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("55555555")

#4.保存
driver.find_element_by_css_selector(".btn4").click()
#对弹出窗的操作
#在处理弹出框操作前,一定要加一个固定的时间等待
time.sleep(3)
#弹窗内确定按钮操作
driver.switch_to.alert.accept()
#弹窗内取消操作
#driver.switch_to.alert.dismiss()