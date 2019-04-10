from pageobjects.Base import BasePage
from selenium.webdriver.common.by import By
class Page_vote(BasePage):
    '''投票页面'''
    #投票标题
    __vote_page_title_loc = (By.CSS_SELECTOR, "#subject")
    #选项1
    __vote_page_one_loc = (By.CSS_SELECTOR, "#pollm_c_1 .px:first-of-type")
    #选项2
    __vote_page_two_loc = (By.CSS_SELECTOR, "#pollm_c_1 p:nth-child(2) input")
    #选项3
    __vote_page_three_loc = (By.CSS_SELECTOR, "#pollm_c_1 p:nth-child(3) input")
    #天数
    __vote_page_day_input_loc = (By.CSS_SELECTOR, "#polldatas")
    #提交按钮
    __vote_page_button_loc = (By.CSS_SELECTOR, ".mbm .pnc")
    #投票内容
    __vote_page_body_loc = (By.CSS_SELECTOR, "body")
    # 投票选择
    __vote_page_choose_loc = (By.CSS_SELECTOR, "#option_2")
    #投票提交按钮
    __vote_page_ok_button_loc = (By.CSS_SELECTOR, "#pollsubmit")
    # 投票人数
    __vote_page_values_loc = (By.CSS_SELECTOR, ".pvt label")
    #投票选项
    __vote_page_value_res_loc = (By.CSS_SELECTOR, ".pcht tr td:last-of-type")
    #投票的标题
    __vote_page_title_value_loc = (By.CSS_SELECTOR, ".ts>span")
    # 发布投票
    def release_vote(self, title, one, two, three, day, body):
        self.sendkeys(title, *self.__vote_page_title_loc)
        self.sendkeys(one, *self.__vote_page_one_loc)
        self.sendkeys(two, *self.__vote_page_two_loc)
        self.sendkeys(three, *self.__vote_page_three_loc)
        self.sendkeys(day, *self.__vote_page_day_input_loc)
        self.switch_to_iframe(0)
        self.sendkeys(body, *self.__vote_page_body_loc)
        self.switch_to_now()
        self.click(*self.__vote_page_button_loc)
        self.logger.info("发布投票")
    #投票
    def ok_vote(self):
        self.click(*self.__vote_page_choose_loc)
        self.click(*self.__vote_page_ok_button_loc)
        self.logger.info("投票")
    #获取值
    def get_vote(self):
        list=[]
        list2=[]
        values=self.find_elements(*self.__vote_page_values_loc)
        for i in values:
            list.append(i.text)
        res = self.find_elements(*self.__vote_page_value_res_loc)
        for i in res:
            if i.text =="" or len(i.text)>12:
                pass
            else:
                list2.append(i.text)
        title_res = self.get_element_text(*self.__vote_page_title_value_loc)
        self.logger.info("标题：%s\n选项：%s\n投票结果：%s"%(title_res,list,list2))
        return [title_res,list,list2]