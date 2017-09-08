import os
import requests
from db.DAO import (
    stock,
    report,
)
import re


LOADURL = 'http://www.cninfo.com.cn/cninfo-new/disclosure/szse_main/download/%s?announceTime=%s'
#windows
PATH = r'E:\stock\report\%s\%s.pdf'
STOCKPATH = r'E:\stock\report\%s'

#linux
LINUX_REPORT_PATH = os.getcwd() + '/report/%s/%s.pdf'
#/home/zwh/PycharmProjects/aPractice-master/report/??
LINUX_STOCKPATH = os.getcwd() + '/report/%s'


#给原来的，得到load url
def convert_to_load_url(url):
    regex = re.compile(r'(\d){4,10}')
    mo1 = regex.search(url)
    regex = re.compile(r'(\d){4}-\d\d-\d\d')
    mo2 = regex.search(url)
    # url = LOADURL + mo1.group() + '?announceTime=' + mo2.group()
    load_url = LOADURL % (mo1.group(), mo2.group())
    return load_url

# 改成xxxx20xx年度报告
def get_formal_name(filename, stock_name):
    regex = re.compile(r'20\d\d.*')
    name = regex.search(filename)
    return stock_name + name.group()




class Loadder():
    # load file which is not exist


    def get_urls(self):
        set = report.unloaded_reps()
        return set


    def get_stock_name(self,stock_id):
        set = stock.select(stock_id)
        row = set[0]
        return row[1]



    def load_report(self, load_url, filename, stock_name):

        #目录跨平台
        def get_path_by_system(filename,stock_name):
            import platform, os
            sys = platform.system()
            if sys == 'Linux':
                os.getcwd()
                stock_dirctory = LINUX_STOCKPATH%stock_name
                path = LINUX_REPORT_PATH % (stock_name,filename)
                return stock_dirctory, path

            elif sys == 'Windows':
                stock_dirctory = STOCKPATH%stock_name
                # path = './' + stock_name + '/' + filename + '.pdf'
                path = PATH % (stock_name,filename)
                return stock_dirctory , path

        stock_dirctory , path = get_path_by_system(filename,stock_name)


        #   是否有report 目录
        if not os.path.exists(stock_dirctory):
            os.makedirs(stock_dirctory)
        #是否有表
        if os.path.exists(path):
            print(filename + 'exist')
            return

        res = requests.get(load_url)
        with open(path, 'wb') as f:
            for cont in res.iter_content(300000):
                f.write(cont)
                # print(len(cont))
        print("Sucessful to download" + "       " + filename)
        report.update_flag(filename)


    def load(self):
        set = self.get_urls()
        for row in set:
            rep_name = row[0]
            stock_id = row[1]
            rep_url = row[2]
            stock_name = self.get_stock_name(stock_id)
            load_url = convert_to_load_url(rep_url)
            self.load_report(load_url, rep_name, stock_name)


lod = Loadder()


