import unittest
from testsuites.BaseTestCase import BaseTestCase
from pageobjects.page_home import Page_home
from pageobjects.page_login import Page_login
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
        home_page = Page_home(self.driver)
        login_page = Page_login(self.driver)
        flag = login_page.login(username, userpsd)
        self.assertEqual(True, flag, msg="%s登录失败" % username)
        if flag == True:
            home_page.select_mes(se_mes_title)
            home_page.click_first_mes()
            # mes_title=home_page.get_mes_title()
            # self.assertEqual(mes_title,se_mes_title,msg="查找%s贴失败"%mes_title)
            search_flag=home_page.is_search_mes(se_mes_title)
            self.assertEqual(True,search_flag,msg="搜索结果和预期不一致")
            login_page.quit_login()
            self.assertEqual(True, login_page.assert_page(), msg="执行失败")
        else:
            self.driver.close()
if __name__ =="__main__":
    unittest.main(verbosity=2)