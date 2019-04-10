from pageobjects.Base import BasePage
from selenium.webdriver.common.by import By
import time
class Page_login(BasePage):
    '''登录 导航栏'''
    #用户名输入框
    __login_page_input_name_loc = (By.CSS_SELECTOR, '#ls_username')
    #密码输入框
    __login_page_input_psd_loc = (By.CSS_SELECTOR, '#ls_password')
    #登录按钮
    __login_page_button_login_loc = (By.CSS_SELECTOR, '.pn em')
    #找回密码
    __login_page_find_psd_button_loc = (By.CSS_SELECTOR,'.pns td:nth-last-child(1)>a')
    #立即注册
    __login_page_reg_button_loc = (By.CSS_SELECTOR,".pns tr:nth-child(2) td:nth-child(4)>a")
    #用户名
    __name_loc = (By.CSS_SELECTOR, ".vwmy>a")
    #退出按钮
    __login_page_button_quit_loc = (By.LINK_TEXT, "退出")
    # 管理中心
    __login_page_manage_button_loc = (By.LINK_TEXT, "管理中心")

    #登录
    def login(self,username,password):
        self.sendkeys(username,*self.__login_page_input_name_loc)
        self.sendkeys(password,*self.__login_page_input_psd_loc)
        self.click(*self.__login_page_button_login_loc)
        self.logger.info("%s登录"%username)
        uname=self.get_element_text(*self.__name_loc)
        if username in uname:
            self.logger.info("%s登录成功"%username)
            return True
        else:
            self.logger.error("%s登录失败" % username)
            return False
    #退出登录
    def quit_login(self):
        self.click(*self.__login_page_button_quit_loc)
        self.logger.info("退出登录")
    #点击管理
    def click_Management(self):
        self.click(*self.__login_page_manage_button_loc)
        self.logger.info("点击后台管理")
        self.switch_to_windownum(1)
    #确定退出成功
    def assert_page(self):
        self.logger.info("退出登录")
        return self.is_not_element_exists(*self.__name_loc)
    #找回密码
    def find_psd(self):
        self.click(*self.__login_page_find_psd_button_loc)
        self.logger.info("点击找回密码按钮")
    #立即注册
    def reg(self):
        self.click(*self.__login_page_reg_button_loc)
        self.logger.info("点击立即注册")