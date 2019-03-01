import xlrd
from framework.logger import Logger
logger = Logger(logger="util").getlog()
class Util(object):
    @classmethod
    def read_excel(self,excelPath,sheetName="Sheet1"):
        """
        将Excel表的数据读取出来
        思路：先读行，再读列，以列表字典方式进行数据存储
        :param excelPath:
        :param sheetName:
        :return:
        """
        workbook=xlrd.open_workbook(excelPath)
        sheet=workbook.sheet_by_name(sheetName)
        #获取第一行作为key
        keys=sheet.row_values(0)
        #获取总行数
        rowNum=sheet.nrows
        #获取总列数
        cloNum =sheet.ncols
        if rowNum <=1:
            logger.info("excel表中数据总行数小于1")
        else:
            r=[]
            #数据从第二行开始
            for i in range(1,rowNum):
                sheet_data={}
                values = sheet.row_values(i)
                for j in range(cloNum):
                    sheet_data[keys[j]]=values[j]
                r.append(sheet_data)
        return r
if __name__=="__main__":
    print(Util.read_excel(r"E:\PyCharm\Discuz\framework\test.xlsx"))