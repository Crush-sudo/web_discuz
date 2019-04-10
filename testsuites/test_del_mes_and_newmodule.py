import unittest
from testsuites.BaseTestCase import BaseTestCase
from pageobjects.page_login import Page_login
from pageobjects.page_home import Page_home
from pageobjects.page_module import Page_module
from pageobjects.page_mes import Page_mes
from pageobjects.page_admin import Page_admin
import time
username="sxd"
userpsd="802352.sxd"
ad_name="admin"
ad_psd="802352"
mes_title="haotest"
mes_story="haotest,hello word"
mes_reply="see you,hello word"
module_name="今日板块"
class test_del_mes_and_newmodule(BaseTestCase):
    def test_del_mes_and_newmodule(self):
        """第二个业务流程场景"""
        '''
        业务流程
            登录  进入默认板块 删除帖子 进入板块管理 创建板块 退出 普通用户登录 发帖 退出
        '''
        home_page=Page_home(self.driver)
        login_page=Page_login(self.driver)
        module_page=Page_module(self.driver)
        mes_page=Page_mes(self.driver)
        admin_page=Page_admin(self.driver)
        flag=login_page.login(ad_name,ad_psd)
        self.assertEqual(True,flag,msg="%s登录失败"+ad_name)
        if flag==True:
            home_page.click_default()
            module_page.click_mes()
            mes_page.del_mes()
            login_page.click_Management()
            admin_flag=admin_page.manage_login(ad_psd)
            self.assertEqual(True,admin_flag,msg="admin登录失败")
            if admin_flag==True:
                admin_page.click_forum()
                admin_page.add_module(module_name)
                login_page.quit_login()
                login_page.quit_login()
                time.sleep(5)
                two_flag = login_page.login(username, userpsd)
                self.assertEqual(True, flag, msg="%s登录失败" + username)
                if two_flag==True:
                    home_page.click_newmodule()
                    module_page.post_message(mes_title, mes_reply)
                    time.sleep(2)
                    module_page.reply(mes_reply)
                    login_page.quit_login()
                    self.assertEqual(True, login_page.assert_page(), msg="执行失败")
                else:
                    self.driver.close()
if __name__ =="__main__":
    unittest.main(verbosity=2)