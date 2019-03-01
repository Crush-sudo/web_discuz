import unittest
from testsuites.BaseTestCase import BaseTestCase
from pageobjects.homepage import HomePage
import time
username="sxd"
userpsd="802352.sxd"
ad_name="admin"
ad_psd="802352"
mes_title="haotest"
mes_story="haotest,hello word"
mes_reply="see you"
module_name="今日板块"
class test_del_mes_and_newmodule(BaseTestCase):
    def test_del_mes_and_newmodule(self):
        """第二个业务流程场景"""
        '''
        业务流程
            登录  
            进入默认板块
            删除帖子
            进入板块管理
            创建板块
            退出
            普通用户登录
            发帖
            退出
        '''
        home_page=HomePage(self.driver)
        name=home_page.login(ad_name,ad_psd)
        self.assertEqual(name,ad_name,msg="登录成功")
        if ad_name in name:
            home_page.click_default()
            home_page.del_mes()
            home_page.click_Management()
            home_page.switch_to_windownum(1)
            admin_name=home_page.manage_login(ad_psd)
            if ad_name in admin_name:
                home_page.click_forum()
                home_page.switch_to_iframe(0)
                home_page.add_module(module_name)
                home_page.switch_to_now()
                home_page.exit()
                home_page.exit()
                time.sleep(5)
                name=home_page.login(username,userpsd)
                self.assertEqual(name,username,msg="登录成功")
                if username in name:
                    home_page.click_newmodule()
                    home_page.post_message(mes_title, mes_story)
                    home_page.Reply(mes_reply)
                    home_page.exit()
                    self.assertEqual(True, home_page.assert_page(), msg="执行成功")
if __name__ =="__main__":
    unittest.main(verbosity=2)