#这个类的作用:把setup方法和teardown方法,从测试用例类中分离出来
#以后创建测试用例类时,就不需要重新写setUp和tearDown方法

#如何实现这样一个类?
#现在我们写一个类也继承了unittest.TestCase类,并且重写setUp和teardown方法,
#以后所有的测试用例只需要继承这个类,是不是会自动继承父类中的setUp()和tearDown()

import unittest
import time
from selenium import webdriver


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("这个方法类似于java中的beforeMethod")
        self.driver = webdriver.Chrome()
        ##隐式等待
        # 优点:会自动判断网页是否加载好,一旦网页加载好,就会执行下面的语句
        self.driver.implicitly_wait(30)
        # self.driver.maximize_window()

    @classmethod
    def tearDownClass(self):
        print("这个方法类似于java中的afterMethod")
        time.sleep(15)
        self.driver.quit()