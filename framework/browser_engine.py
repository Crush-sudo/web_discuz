import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger
logger=Logger(logger="BrowserEngine").getlog()
class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath('.'))
    chrome_driver_path=dir+'/songxuedong_web_Discuz/tools/chromedriver.exe'
    ie_driver_path=dir+'/songxuedong_web_Discuz/tools/IEDriverServer.exe'
    FireFox_driver_path=dir+'/songxuedong_web_Discuz/tools/geckodriver.exe'
    #打开浏览器
    def open_browser(self):
        config=ConfigParser()
        file_path=os.path.dirname(os.path.abspath('.'))+'/songxuedong_web_Discuz/config/config.ini'
        config.read(file_path)

        browser=config.get("browserType","browserName")
        logger.info("You had select %s browser."% browser)
        url=config.get("testServer","URL")
        logger.info("The test server url is: %s"% url)

        if browser=="Firefox":
            self.driver=webdriver.Firefox(firefox_profile=self.FireFox_driver_path)
            logger.info("Starting firefox browser.")
        elif browser=="Chrome":
            self.driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting chrome browser.")
        elif browser=="IE":
            self.driver=webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        self.driver.get(url)
        logger.info("Open url: %s"%url)
        self.driver.maximize_window()
        logger.info("Maximize the current window.")
        self.driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return self.driver
    #关闭浏览器
    def quit_browsey(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()


