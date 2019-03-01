import unittest
from framework.browser_engine import BrowserEngine
from ddt import ddt,data,unpack
@ddt
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        print("开始测试")
        self.be=BrowserEngine()
        self.driver=self.be.open_browser()
    def tearDown(self):
        print("结束测试")
        self.be.quit_browsey()
