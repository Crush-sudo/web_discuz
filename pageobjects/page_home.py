from pageobjects.Base import BasePage
from selenium.webdriver.common.by import By
import time
class Page_home(BasePage):
    '''主页面'''
    #默认板块
    __home_page_button_default_loc = (By.LINK_TEXT, '默认板块')
    #新板块
    __home_page_button_new_loc = (By.CSS_SELECTOR, '.fl_row:nth-last-child(2) h2>a')
    # 帖子搜索框
    __home_page_select_input_loc = (By.CSS_SELECTOR, ".scbar_txt_td>input")
    #搜索按钮
    __home_page_select_button_loc = (By.CSS_SELECTOR, ".scbar_btn_td>button")
    #搜索结果第一个
    __home_page_first_button_loc = (By.CSS_SELECTOR, ".pbw:first-of-type a")
    #帖子标题
    __home_page_title_loc = (By.CSS_SELECTOR, "#thread_subject")
    #点击默认板块
    def click_default(self):
        self.click(*self.__home_page_button_default_loc)
    #点击新板块
    def click_newmodule(self):
        self.click(*self.__home_page_button_new_loc)
    #搜帖子
    def select_mes(self,mes):
        self.clear(*self.__home_page_select_input_loc)
        self.sendkeys(mes,*self.__home_page_select_input_loc)
        self.click(*self.__home_page_select_button_loc)
        self.logger.info("搜索帖子%s"%mes)
        self.switch_to_windownum(1)
    #点击帖子第一个
    def click_first_mes(self):
        self.click(*self.__home_page_first_button_loc)
        self.logger.info("打开帖子")
        self.switch_to_windownum(2)
    #获取帖子标题
    def get_mes_title(self):
        mes=self.get_element_text(*self.__home_page_title_loc)
        self.logger.info("帖子标题：%s" % mes)
        return mes
    #判断搜索到的帖子和预期是否一致
    def is_search_mes(self,mes):
        if mes==self.get_mes_title():
            self.logger.info("搜索结果和预期一致")
            return True
        else:
            self.logger.error("搜索结果和预期不一致")
            return False