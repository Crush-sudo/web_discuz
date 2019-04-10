from pageobjects.Base import BasePage
from selenium.webdriver.common.by import By
import time
class Page_module(BasePage):
    '''板块页面'''
    #帖子标题
    __module_page_input_title_loc = (By.CSS_SELECTOR, '#subject')
    # 帖子内容
    __module_page_input_story_loc = (By.CSS_SELECTOR, '#fastpostmessage')
    # 发帖按钮
    __module_page_button_submit_loc = (By.CSS_SELECTOR, '.ptm button')
    # 帖子列表
    __module_page_mes_button_loc = (By.CSS_SELECTOR, ".num .xi2")
    # 发布按钮
    __module_page_release_button_loc = (By.CSS_SELECTOR, "#newspecial")
    # 投票按钮
    __module_page_vote_button_loc = (By.CSS_SELECTOR, "#editorbox>.mbw>li:nth-last-child(1)>a")

    # 发帖
    def post_message(self, title, story):
        self.sendkeys(title, *self.__module_page_input_title_loc)
        self.sendkeys(story, *self.__module_page_input_story_loc)
        self.click(*self.__module_page_button_submit_loc)
        self.logger.info("发帖%s" % title)

    # 回贴
    def reply(self, reply):
        self.sendkeys(reply, *self.__module_page_input_story_loc)
        self.click(*self.__module_page_button_submit_loc)
        self.logger.info("回复%s" % reply)

    # 点击一个帖子
    def click_mes(self):
        self.click(*self.__module_page_mes_button_loc)
        self.logger.info("打开一个帖子")

    # 点击发布按钮
    def click_release(self):
        self.click(*self.__module_page_release_button_loc)
        self.logger.info("点击发布")

    # 点击投票按钮
    def click_vote(self):
        self.click(*self.__module_page_vote_button_loc)
        self.logger.info("发起投票")