import os,time
import logging

class Logger(object):
    def __init__(self, logger):
        '''
        指定保存日志的文件路径，日志级别，以及调用文件
        将日志存入到指定文件中
        :param logger:
        '''
        #创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        #创建一个Handler，用于写入日志文件
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath("."))+"/logs/"
        #如果case组织结构式/testsuit/featuremodel/xxx.py,那么得到的相对路径的父路径就是项目根路径
        log_name=log_path+rq+'.log'
        fh=logging.FileHandler(log_name)
        fh.setLevel(logging.INFO)

        #再创建一个Handler，用于输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        #定义handler的输出格式
        formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)

    def getlog(self):
        return self.logger





