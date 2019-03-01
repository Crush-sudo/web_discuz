import unittest
from testsuites.BaseTestCase import BaseTestCase
from pageobjects.homepage import HomePage
from ddt import ddt,data,unpack
import time
username="sxd"
userpsd="802352.sxd"
mes_title="haotest"
mes_story="haotest,hello word"
mes_reply="see you"
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
        home_page=HomePage(self.driver)
        name=home_page.login(username,userpsd)
        self.assertEqual(username,name,msg=username)
        if username in name:
            home_page.click_newmodule()
            home_page.click_release()
            home_page.click_vote()
            home_page.release_vote(vote_title,vote_one,vote_two,vote_three,vote_day,vote_body)
            home_page.ok_vote()
            value=home_page.get_vote()
            self.assertEqual(value[0],vote_title,msg="投票标题%s"%value[0])
            print("标题：",value[0])
            for i in range(0,len(value[1])):
                print("选项{}：投票结果{}".format(value[1][i],value[2][i]))
            time.sleep(5)
            home_page.exit()
            self.assertEqual(True, home_page.assert_page(), msg="执行成功")
if __name__ =="__main__":
    unittest.main(verbosity=2)