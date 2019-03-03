import HTMLTestRunner
import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(".")))
from testsuites.test_login_post_reoly import test_login_post_reoly
from testsuites.test_del_mes_and_newmodule import test_del_mes_and_newmodule
from testsuites.test_search_mes import test_search_mes
from testsuites.test_release_vote import test_release_vote
#构造存储路径
report_path=os.path.dirname(os.path.abspath("."))+"/report/"
if not os.path.exists(report_path):os.mkdir(report_path)
#构造测试套件
suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(test_login_post_reoly))
suite.addTest(unittest.makeSuite(test_del_mes_and_newmodule))
suite.addTest(unittest.makeSuite(test_search_mes))
suite.addTest(unittest.makeSuite(test_release_vote))
#执行
if __name__=='__main__':
    html_report=report_path+r'\report.html'
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="Discuz测试",description="Discuz主要流程测试")
    runner.run(suite)