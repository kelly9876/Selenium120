#自动化测试框架unittest
#框架的优点:
#1.批量组织和执行测试用例
#2.封装了一些底层常用的方法,使测试用例更简洁

#如何使用unittest
#1.导包
import unittest

import time
from selenium import webdriver

#2.我们自己写的测试用例类,需要继承unittest中的父类TestCase
class UpdateMemberInfoTest(unittest.TestCase):
    # 3.重写父类的setUp和teatDown方法
    # setUp==beforeMethod,teatDown==afterMethod

    # setup方法和setupClass方法的区别:setup是每次测试用例都要重新执行一遍
    # setClass是在类中所有测试用例之前 只执行一遍
    # 测试用例之间的执行顺序是按照字母的顺序执行的,denglu是d开头,那么就比member_update是m开头的先执行
    @classmethod
    def setUpClass(self):
        print("这个方法类似于java中的beforeMethod")
        self.driver = webdriver.Chrome()
        ##隐式等待
        # 优点:会自动判断网页是否加载好,一旦网页加载好,就会执行下面的语句
        self.driver.implicitly_wait(30)
        #self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        print("这个方法类似于java中的afterMethod")
        time.sleep(15)
        self.driver.quit()

    # 4.声明一个测试用例方法,需要以test作为方法名的开头
    def test_member_updating(self):
        print("这是一个测试用例方法,这个方法用于修改会员信息的测试")
        driver = self.driver

        # 账号设置功能测试
        # 1.账号设置
        driver.find_element_by_link_text("账号设置").click()

        # 2.个人资料
        driver.find_element_by_partial_link_text("个人资料").click()

        # 3.修改个人资料
        # xpath中//表示相对路径
        # *表示任意元素
        # []表示属性
        # @id表示id属性
        # driver.find_element_by_xpath("//*[@id=\"true_name\"]")
        # xpath的缺点:定位速度很慢

        # cssSelector优点:快,定位简单,准确
        driver.find_element_by_css_selector("#true_name").clear()
        driver.find_element_by_css_selector("#true_name").send_keys("张三")
        driver.find_element_by_css_selector("[value=\"2\"]").click()

        # selenium不能删除页面元素的属性,只能通过javascript来实现
        driver.execute_script('document.getElementById("date").removeAttribute("readonly")')
        driver.find_element_by_id("date").clear()
        driver.find_element_by_id("date").send_keys("1970-10-25")
        driver.find_element_by_id("qq").clear()
        driver.find_element_by_id("qq").send_keys("55555555")

        # 4.保存
        driver.find_element_by_css_selector(".btn4").click()
        # 对弹出窗的操作
        # 在处理弹出框操作前,一定要加一个固定的时间等待
        time.sleep(3)
        # 弹窗内确定按钮操作
        driver.switch_to.alert.accept()

    def test_denglu(self):
        print("这是登录的测试用例")
        driver = self.driver
        # 1. 打开登录页面
        # http://localhost/index.php?m=user&c=public&a=login
        # 接口测试: 请求最重要的一个请求方式get, url地址, 有了这两部分,就可以构造请求,接收响应了

        driver.get("http://172.31.4.74/index.php?m=user&c=public&a=login")
        # 2. 输入用户名
        # 分为两部分, 找到用户名输入框, 对输入框输入文字
        # 元素的定位顺序: id---> name----> class
        driver.find_element_by_id("username").send_keys("changcheng")
        # 接下来手工主测一个账号, 写代码实现输入用户名和密码,点击登录按钮
        # 3.输入密码
        driver.find_element_by_name("password").send_keys("123654")
        # 4.点击登录
        driver.find_element_by_class_name("login_btn").click()

if __name__ == '__main__':
    unittest.main()