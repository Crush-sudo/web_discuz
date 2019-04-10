import unittest
from testsuites.BaseTestCase import BaseTestCase
from pageobjects.page_home import Page_home
from pageobjects.page_login import Page_login
from pageobjects.page_module import Page_module
from pageobjects.page_vote import Page_vote
import time
username="admin"
userpsd="802352"
vote_title="谁最帅"
vote_one="我"
vote_two="你"
vote_three="他"
vote_day="2"
vote_body="我最帅"
class test_release_vote(BaseTestCase):
    def test_release_vote(self):
        """第四个业务流程场景"""
        '''
        业务流程
        发表投票帖子
        进行投票
        取出投票各个选项的名称以及投票比例
        取出投票的主题名称
        '''
        home_page=Page_home(self.driver)
        login_page=Page_login(self.driver)
        module_page=Page_module(self.driver)
        vote_page=Page_vote(self.driver)
        flag = login_page.login(username, userpsd)
        self.assertEqual(True, flag, msg="%s登录失败" % username)
        if flag == True:
            home_page.click_newmodule()
            module_page.click_release()
            module_page.click_vote()
            vote_page.release_vote(vote_title,vote_one,vote_two,vote_three,vote_day,vote_body)
            vote_page.ok_vote()
            value = vote_page.get_vote()
            self.assertEqual(value[0],vote_title,msg="发布投票%s错误"%value[0])
            print("标题：", value[0])
            for i in range(0,len(value[1])):
                print("选项{}：投票结果{}".format(value[1][i],value[2][i]))
            time.sleep(5)
            login_page.quit_login()
            self.assertEqual(True, login_page.assert_page(), msg="执行失败")
        else:
            self.driver.close()
if __name__ =="__main__":
    unittest.main(verbosity=2)