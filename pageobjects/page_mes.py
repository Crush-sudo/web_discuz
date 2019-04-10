from pageobjects.Base import BasePage
from selenium.webdriver.common.by import By
import time
class Page_mes(BasePage):
    '''帖子页面'''
    #删除主题按钮
    __mes_page_mes_del_loc = (By.CSS_SELECTOR,"#modmenu>a")
    #确定删除
    __mes_page_mes_del_ok_loc = (By.CSS_SELECTOR,".o button")
    #删除帖子
    def del_mes(self):
        self.click(*self.__mes_page_mes_del_loc)
        self.click(*self.__mes_page_mes_del_ok_loc)
        self.logger.info("删除帖子成功")