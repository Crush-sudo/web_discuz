import unittest
from testsuites.BaseTestCase import BaseTestCase
from pageobjects.homepage import HomePage
import time
username="sxd"
userpsd="802352.sxd"
mes_title="haotest"
mes_story="haotest,hello word"
mes_reply="see you,hello word"
class test_login_post_reoly(BaseTestCase):
    def test_login_post_reoly(self):
        """第一个业务流程场景"""
        '''
        业务流程
        登录  发帖  回复  退出
        '''
        home_page=HomePage(self.driver)
        name=home_page.login(username,userpsd)
        self.assertEqual(username,name,msg="%s登录成功"%username)
        if username in name:
            home_page.click_default()
            home_page.post_message(mes_title,mes_story)
            time.sleep(2)
            home_page.Reply(mes_reply)
            home_page.exit()
            self.assertEqual(True,home_page.assert_page(),msg="执行成功")
if __name__ =="__main__":
    unittest.main(verbosity=2)