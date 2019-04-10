from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
import time,os.path
logger=Logger(logger="BasePage").getlog()
#基类，父类
class BasePage(object):
    def __init__(self,driver):
        self.driver=driver
        self.logger=logger
    #后退
    def back(self):
        try:
            self.driver.back()
            self.logger.info("页面后退")
        except Exception as e:
            self.get_windows_img()
            self.logger.error("页面后退失败,%s"%e)
    #前进
    def forward(self):
        try:
            self.driver.forward()
            self.logger.info("浏览器前进")
        except Exception as e:
            self.get_windows_img()
            self.logger.error("浏览器前进失败，%s"%e)

    #访问URL
    def open_url(self,url):
        try:
            self.driver.get(url)
            self.logger.info("Open url: %s"%url)
        except Exception as e:
            self.get_windows_img()
            self.logger.error("Open url error: %s"%e)
    #关闭浏览器
    def quit_browser(self):
        try:
            self.driver.quit()
            self.logger.info("Now,Close and quit the browser.")
        except Exception as e:
            self.get_windows_img()
            self.logger.error("close browser error,%s"%e)
    #关闭某个页面
    def close(self):
        try:
            self.driver.close()
            self.logger.info("关闭页面")
        except Exception as e:
            self.get_windows_img()
            self.logger.error("关闭页面失败，%s"%e)
    #填写
    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)
        el.clear()
        try:
            el.send_keys(text)
            self.logger.info("输入：%s"%text)
        except Exception as e:
            self.get_windows_img()
            self.logger.error("输入%s错误，%s"%(text,e))
    #单击
    def click(self,*loc):
        try:
            el = self.find_element(*loc)
            el.click()
            self.logger.info("点击%s"%el)
        except Exception as e:
            self.get_windows_img()
            self.logger.error("点击失败")
    #查找元素
    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            self.logger.info("%s找到页面元素:%s"%(self,loc))
            return self.driver.find_element(*loc)
        except:
            self.get_windows_img()
            self.logger.error("%s页面未能找到%s元素"%(self,loc))
    # 查找元素组
    def find_elements(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            self.logger.info("%s找到页面元素:%s" % (self, loc))
            return self.driver.find_elements(*loc)
        except:
            self.get_windows_img()
            self.logger.error("%s页面未能找到%s元素" % (self, loc))
    #清除文本框
    def clear(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
            self.logger.info("清除%s"%el)
        except Exception as e:
            self.get_windows_img()
            self.logger.error("清除失败，%s"%e)
    #窗口最大化
    def max_window(self):
        self.max_window()
        self.logger.info("窗口最大化")
    #设置窗口大小
    def set_window(self,wide,high):
        self.driver.set_window_size(wide,high)
        self.logger.info("窗口大小设置为：%s*%s"%(wide,high))
    #刷新
    def F5(self):
        self.driver.refresh()
        self.logger.info("页面刷新")
    #执行js
    def js(self,js):
        self.driver.execute_script(js)
        self.logger.info("执行js：%s"%js)
    #等待
    def wait(self,secs):
        self.driver.implicitly_wait(secs)
        self.logger.info("等待%s秒"%secs)
    #切换窗口
    def switch_to_windownum(self,num):
        try:
            self.driver.switch_to.window(self.driver.window_handles[num])
            self.get_windows_img()
            self.logger.info("切换窗口成功")
        except Exception as e:
            self.get_windows_img()
            self.logger.error("切换窗口失败：%s"%e)
    #切换iframe
    def switch_to_iframe(self,num):
        try:
            self.driver.switch_to.frame(num)
            self.get_windows_img()
            self.logger.info("切换iframe成功")
        except Exception as e:
            self.get_windows_img()
            self.logger.info("切换iframe失败：%s"%e)
    #根据属性切换frame
    def switch_to_frame_by(self,*loc):
        try:
            self.driver.switch_to.frame(self.find_elements(*loc)[0])
        except Exception as e:
            self.get_windows_img()
            self.logger.info("切换iframe失败：%s"%e)
    #获取所有的frame
    def frame_list(self):
        return self.driver.find_elements_by_tag_name("iframe")
    #激活当前窗口
    def switch_to_now(self):
        try:
            self.driver.switch_to.window(self.driver.current_window_handle)
            self.logger.info("激活窗口成功")
        except Exception as e:
            self.get_windows_img()
            self.logger.error("激活窗口失败：%s"%e)
    #选择新打开的浏览器窗口
    def switch_next_window(self):
        try:
            current_window = self.driver.current_window_handle
            handles = self.driver.window_handles
            for handle in handles:
                if handle != current_window:
                    self.driver._switch_to.window(handle)
                    self.logger.info("切换到新窗口")
        except Exception as e:
            self.get_windows_img()
            self.logger.info("切换窗口失败：%s"%e)
    #判断页面元素不存在
    def is_not_element_exists(self,*loc):
        try:
            self.driver.find_element(*loc)
            return False
        except Exception as e:
            self.get_windows_img()
            return True
    #判断页面元素是否存在
    def is_element_exists(self,*loc):
        try:
            self.driver.find_element(*loc)
            return True
        except Exception as e:
            self.get_windows_img()
            return False
    #返回控件元素的文本信息
    def get_element_text(self,*loc):
        return self.find_element(*loc).text
    #返回元素的属性值
    def get_attribute(self,attrname,*loc):
        return self.find_element(*loc).get_attribute(attrname)
    #获取当前执行文件的系统路径
    def getcwd(self):
        return os.getcwd()
    #判断页面是否加载完毕
    def is_page_load_complete(self):
        js = "return document.readyState"
        result=self.driver.execute_script(js)
        if result =="complete":
            self.logger.info("页面加载完成")
            return True
        else:
            self.logger.error("页面加载未完成")
            return False
    #获取屏幕截图
    def get_windows_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+"/songxuedong_web_Discuz/screenshots/"
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+rq+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            self.logger.info("屏幕截图，保存路径是%s"%screen_name)
        except Exception as e:
            self.get_windows_img()
            logger.error("%s截屏失败%s"%(self,e))
    #点击弹窗的确定
    def accept_alert(self):
        try:
            self.driver._switch_to.alert.accept()
            self.logger.info("点击了弹窗的确定按钮")
        except Exception as e:
            self.get_windows_img()
            self.logger.info("关闭弹窗失败")
    # 弹窗关闭
    def dismiss_alert(self):
        try:
            self.driver._switch_to.alert.dismiss()
            self.logger.info("点击了弹窗的关闭按钮")
        except Exception as e:
            self.get_windows_img()
            self.logger.info("关闭弹窗失败")
    #点击空白
    def click_body(self):
        self.find_element("xpath", "/html/body").click()
        self.logger.info("点击空白区域")
    #鼠标移动到指定元素
    def move_to_element(self,*loc):
        self.move_to_element(self.find_element(*loc)).perform()
        self.logger.info("移动鼠标")
    #检查元素的属性值是否正确
    def attr_chenk(self,attrname,attr_value,*loc):
        attr=self.get_attribute(attrname,*loc)
        if attr==attr_value:
            return True
        else:
            return False
    #常用的键盘操作
    def win_key(self,*keys):
        self.driver.send_keys(*keys)



