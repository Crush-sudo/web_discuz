from pageobjects.Base import BasePage
from selenium.webdriver.common.by import By
import time
class Page_admin(BasePage):
    '''后台页面'''
    # 管理员密码输入框
    __manage_page_input_psd_loc = (By.XPATH, '//input[@name="admin_password"]')
    # 管理员登录按钮
    __manage_page_button_loc = (By.CSS_SELECTOR, ".loginnofloat input")
    #管理员名
    __manage_page_name_loc = (By.CSS_SELECTOR, ".uinfo")
    #论坛
    __manage_page_forum_button_loc = (By.CSS_SELECTOR, "#header_forum")
    # 新建板块
    __manage_page_add_module_button_loc = (By.CSS_SELECTOR, ".lastboard>a")
    #新建板块等级
    __manage_page_input_id_loc = (By.XPATH, '//*[@id="cpform"]/table/tbody[3]/tr[1]/td[2]/input')
    #新建板块名称
    __manage_page_input_text_loc = (By.XPATH, '//*[@id="cpform"]/table/tbody[3]/tr[1]/td[3]/div/input')
    #提交按钮
    __manage_page_submit_button_loc = (By.CSS_SELECTOR, ".fixsel>input")
    # 管理员登录
    def manage_login(self, psd):
        self.sendkeys(psd, *self.__manage_page_input_psd_loc)
        self.click(*self.__manage_page_button_loc)
        self.logger.info("admin登录")
        uname=self.get_element_text(*self.__manage_page_name_loc)
        if "admin" in uname:
            self.logger.info("管理员登录成功")
            return True
        else:
            self.logger.error("管理员登录失败")
            return False
    #点击论坛
    def click_forum(self):
        self.click(*self.__manage_page_forum_button_loc)
        self.logger.info("点击论坛")
    #添加板块
    def add_module(self,text):
        self.switch_to_iframe(0)
        self.click(*self.__manage_page_add_module_button_loc)
        self.clear(*self.__manage_page_input_text_loc)
        self.sendkeys("3",*self.__manage_page_input_id_loc)
        self.sendkeys(text,*self.__manage_page_input_text_loc)
        self.click(*self.__manage_page_submit_button_loc)
        self.logger.info("添加板块%s"%text)
        self.switch_to_now()