import unittest
from testsuites.BaseTestCase import BaseTestCase
from pageobjects.homepage import HomePage
import time
username="sxd"
userpsd="802352.sxd"
se_mes_title="haotest"
class test_search_mes(BaseTestCase):
    def test_search_mes(self):
        """第三个业务流程场景"""
        '''
        业务流程
            用户登录
            进行帖子搜索
            搜索haotest帖子
            进入搜索的帖子
            验证帖子标题和期望的一致
            用户退出
        '''
        home_page=HomePage(self.driver)
        name=home_page.login(username,userpsd)
        if username in name:
            home_page.select_mes(se_mes_title)
            home_page.switch_to_windownum(1)
            home_page.click_first_mes()
            home_page.switch_to_windownum(2)
            mes_title=home_page.get_mes_title()
            self.assertEqual(mes_title,se_mes_title,msg="查找%s贴成功"%mes_title)
            home_page.exit()
            self.assertEqual(True, home_page.assert_page(), msg="执行成功")
if __name__ =="__main__":
    unittest.main(verbosity=2)