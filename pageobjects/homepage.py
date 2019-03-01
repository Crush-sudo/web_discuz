from pageobjects.Base import BasePage
from selenium.webdriver.common.by import By
import time
#继承Base类
class HomePage(BasePage):
    #定位器，通过元素属性定位元素
    #登录页面
    __login_page_input_name_loc=(By.CSS_SELECTOR,'#ls_username')
    __login_page_input_psd_loc = (By.CSS_SELECTOR, '#ls_password')
    __login_page_button_login_loc = (By.CSS_SELECTOR, '.pn em')

    __name_loc = (By.CSS_SELECTOR,".vwmy>a")
    #发帖回帖
    __home_page_button_default_loc = (By.LINK_TEXT, '默认板块')
    __home_page_button_new_loc = (By.CSS_SELECTOR, '.fl_row:nth-last-child(2) h2>a')
    __home_page_input_title_loc = (By.CSS_SELECTOR,'#subject')
    __home_page_input_story_loc = (By.CSS_SELECTOR, '#fastpostmessage')
    __home_page_button_submit_loc = (By.CSS_SELECTOR, '.ptm button')
    __home_page_button_quit_loc = (By.LINK_TEXT,"退出")
    #删除帖子
    __home_page_mes_button_loc = (By.CSS_SELECTOR,".num .xi2")
    __home_page_mes_del_loc = (By.CSS_SELECTOR,"#modmenu>a")
    __home_page_mes_del_ok_loc = (By.CSS_SELECTOR,".o button")
    #管理中心
    __home_page_manage_button_loc = (By.LINK_TEXT,"管理中心")
    #管理页面
    __manage_page_input_psd_loc = (By.XPATH,'//input[@name="admin_password"]')
    __manage_page_button_loc = (By.CSS_SELECTOR,".loginnofloat input")
    __manage_page_name_loc = (By.CSS_SELECTOR,".uinfo")
    __manage_page_forum_button_loc = (By.CSS_SELECTOR,"#header_forum")
    #新建板块
    __manage_page_add_module_button_loc =(By.CSS_SELECTOR,".lastboard>a")
    __manage_page_input_id_loc = (By.XPATH,'//*[@id="cpform"]/table/tbody[3]/tr[1]/td[2]/input')
    __manage_page_input_text_loc = (By.XPATH,'//*[@id="cpform"]/table/tbody[3]/tr[1]/td[3]/div/input')
    __manage_page_submit_button_loc = (By.CSS_SELECTOR,".fixsel>input")
    #帖子搜索
    __home_page_select_input_loc = (By.CSS_SELECTOR,".scbar_txt_td>input")
    __home_page_select_button_loc = (By.CSS_SELECTOR,".scbar_btn_td>button")
    __mes_page_first_button_loc = (By.CSS_SELECTOR,".pbw:first-of-type a")
    __mes_page_title_loc = (By.CSS_SELECTOR,"#thread_subject")
    #发布按钮
    __home_page_release_button_loc = (By.CSS_SELECTOR,"#newspecial")
    __home_page_vote_button_loc = (By.CSS_SELECTOR,"#editorbox>.mbw>li:nth-last-child(1)>a")
    #发布投票
    __vote_page_title_loc = (By.CSS_SELECTOR,"#subject")
    __vote_page_one_loc = (By.CSS_SELECTOR,"#pollm_c_1 .px:first-of-type")
    __vote_page_two_loc = (By.CSS_SELECTOR, "#pollm_c_1 p:nth-child(2) input")
    __vote_page_three_loc = (By.CSS_SELECTOR, "#pollm_c_1 p:nth-child(3) input")
    __vote_page_day_input_loc = (By.CSS_SELECTOR,"#polldatas")
    __vote_page_button_loc = (By.CSS_SELECTOR,".mbm .pnc")
    __vote_page_body_loc =(By.CSS_SELECTOR,"body")
    #投票
    __vote_page_choose_loc = (By.CSS_SELECTOR,"#option_2")
    __vote_page_ok_button_loc = (By.CSS_SELECTOR,"#pollsubmit")
    #投票值
    __vote_page_values_loc = (By.CSS_SELECTOR,".pvt label")
    __vote_page_value_res_loc = (By.CSS_SELECTOR,".pcht tr td:last-of-type")
    __vote_page_title_value_loc = (By.CSS_SELECTOR,".ts>span")
    #登录
    def login(self,username,password):
        self.sendkeys(username,*self.__login_page_input_name_loc)
        self.sendkeys(password,*self.__login_page_input_psd_loc)
        self.click(*self.__login_page_button_login_loc)
        self.logger.info("%s登录"%username)
        return self.get_element_text(*self.__name_loc)
    #点击默认板块
    def click_default(self):
        self.click(*self.__home_page_button_default_loc)
    #点击新板块
    def click_newmodule(self):
        self.click(*self.__home_page_button_new_loc)
    #发帖
    def post_message(self,title,story):
        self.sendkeys(title,*self.__home_page_input_title_loc)
        self.sendkeys(story,*self.__home_page_input_story_loc)
        self.click(*self.__home_page_button_submit_loc)
        self.logger.info("发帖%s"%title)
    #回复
    def Reply(self,reply):
        self.sendkeys(reply,*self.__home_page_input_story_loc)
        self.click(*self.__home_page_button_submit_loc)
        self.logger.info("回复%s"%reply)
    #退出
    def exit(self):
        self.click(*self.__home_page_button_quit_loc)
        self.logger.info("退出登录")
    #删除帖子
    def del_mes(self):
        self.click(*self.__home_page_mes_button_loc)
        self.click(*self.__home_page_mes_del_loc)
        self.click(*self.__home_page_mes_del_ok_loc)
        self.logger.info("删除帖子成功")
    #点击管理
    def click_Management(self):
        self.click(*self.__home_page_manage_button_loc)
    #管理员登录
    def manage_login(self,psd):
        self.sendkeys(psd,*self.__manage_page_input_psd_loc)
        self.click(*self.__manage_page_button_loc)
        self.logger.info("admin登录")
        return self.get_element_text(*self.__manage_page_name_loc)
    #点击论坛
    def click_forum(self):
        self.click(*self.__manage_page_forum_button_loc)
        self.logger.info("点击论坛")
    #添加板块
    def add_module(self,text):
        self.click(*self.__manage_page_add_module_button_loc)
        self.clear(*self.__manage_page_input_text_loc)
        self.sendkeys("3",*self.__manage_page_input_id_loc)
        self.sendkeys(text,*self.__manage_page_input_text_loc)
        self.click(*self.__manage_page_submit_button_loc)
        self.logger.info("添加板块%s"%text)
    #搜帖子
    def select_mes(self,mes):
        self.clear(*self.__home_page_select_input_loc)
        self.sendkeys(mes,*self.__home_page_select_input_loc)
        self.click(*self.__home_page_select_button_loc)
        self.logger.info("搜索帖子%s"%mes)
    #点击帖子第一个
    def click_first_mes(self):
        self.click(*self.__mes_page_first_button_loc)
    #获取帖子标题
    def get_mes_title(self):
        mes=self.get_element_text(*self.__mes_page_title_loc)
        self.logger.info("帖子标题：%s" % mes)
        return mes
    #点击发布按钮
    def click_release(self):
        self.click(*self.__home_page_release_button_loc)
        self.logger.info("点击发布")
    #点击投票按钮
    def click_vote(self):
        self.click(*self.__home_page_vote_button_loc)
        self.logger.info("点击投票")
    #发布投票
    def release_vote(self,title,one,two,three,day,body):
        self.sendkeys(title, *self.__vote_page_title_loc)
        self.sendkeys(one, *self.__vote_page_one_loc)
        self.sendkeys(two, *self.__vote_page_two_loc)
        self.sendkeys(three, *self.__vote_page_three_loc)
        self.sendkeys(day, *self.__vote_page_day_input_loc)
        self.switch_to_iframe(0)
        self.sendkeys(body,*self.__vote_page_body_loc)
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
    def assert_page(self):
        return self.is_not_element_exists(*self.__name_loc)







