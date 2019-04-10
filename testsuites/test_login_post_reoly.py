import unittest
from testsuites.BaseTestCase import BaseTestCase
from pageobjects.page_login import Page_login
from pageobjects.page_home import Page_home
from pageobjects.page_module import Page_module

username="sxd"
userpsd="802352.sxd"
mes_title="haotest"
mes_story="haotest,hello word"
mes_reply="see you,hello word"
class test_login_post_reoly(BaseTestCase):
    def test_login_post_reoly(self):
        """业务流程
        登录  发帖  回复  退出"""
        login_page=Page_login(self.driver)
        home_page=Page_home(self.driver)
        module_page=Page_module(self.driver)
        flag=login_page.login(username,userpsd)
        self.assertEqual(True,flag,msg="%s登录失败"%username)
        if flag==True:
            home_page.click_default()
            module_page.post_message(mes_title,mes_reply)
            module_page.reply(mes_reply)
            login_page.quit_login()
            self.assertEqual(True, login_page.assert_page(), msg="执行失败")
        else:
            self.driver.close()
if __name__ =="__main__":
    unittest.main(verbosity=2)