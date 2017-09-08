#浏览器自动化


PRE_URL = 'http://www.cninfo.com.cn/information/companyinfo_n.html?fulltext?szmb'

import os, time,sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import warnings


from db.DAO import (
    stock,
    report
)

def get_valid_elem(elems):
    def contain(text):
        words = ['摘要', '取消']
        for word in words:
            if word in text:
                return True
        return False

    new = []
    for elem in elems:
        if contain(elem.text):
            continue
        new.append(elem)
    return new


def get_url_and_name():
    return 'E:/stock/report/url_and_name'
    #E:/stock/report/url_and_name

def get_path_of_stock(stock_num):
    return get_url_and_name() + '\\' + stock_num + '.html'




class NetWorker():

    def firefox(self):
        profile = webdriver.FirefoxProfile()
        profile.set_preference('permissions.default.stylesheet', 2)
        profile.set_preference('permissions.default.image', 2)
        profile.update_preferences()
        return webdriver.Firefox(profile)

    # def phantomJS(self):
    #     #有bug
    #     path = r'E:\aboutPython\phantomjs-2.1.1-windows\bin\phantomjs.exe'
    #     # return webdriver.PhantomJS(executable_path=path)


    def check_info_exist(self, stock_num):
        set = stock.select(stock_num)
        if set != []:
            raise RuntimeError(str(stock_num) + ' has exist')


    def write_stock_info(self, name, stock_num, url, type):
        report.save(name, stock_num, url, type)

    def write_ndbg_info(self, stock_elems, stock_num):
        stock_elems = get_valid_elem(stock_elems)
        for elem in stock_elems:
            name = elem.text
            url = elem.get_attribute('href')
            self.write_stock_info(name, stock_num, url, '年度报告')

    def start_work(self, stock_num):
        browser = self.firefox()

        url = PRE_URL + stock_num
        browser.get(url)
        browser.implicitly_wait(20)

        # switch and click
        browser.switch_to_frame("i_nr")
        ndbg = browser.find_element_by_link_text('年度报告')
        browser.execute_script('$(arguments[0]).click()', ndbg)

        # get stock'name
        td = browser.find_element_by_tag_name('td')
        stock_name = td.text[-4:]
        time.sleep(2)
        print('股名' + stock_name)

        try:
            stock.save_stock(int(stock_num),stock_name)
        except:
            print(stock_name + 'has exist')

        def find_elems():
            elems = browser.find_element_by_id('ul_his_fulltext') \
                .find_elements_by_tag_name('a')
            return elems


        self.write_ndbg_info(find_elems(), stock_num)
        # turn to page 2
        time.sleep(2)
        try:
            page = browser.find_element_by_id('Pagination')
            page2 = page.find_element_by_link_text('2')
            browser.execute_script('$(arguments[0]).click()', page2)
            time.sleep(2)

            self.write_ndbg_info(find_elems(), stock_num)
            print('have page2')
        except:
            print('no page2')

        #
        browser.close()
        # browser.quit()

    def get_rep_info(self, stock_num):

        self.check_info_exist(stock_num)
        # try:
        #
        # except:
        #     print(sys.exc_info())
        #     return

        self.start_work(stock_num)

# report.deletall('report')
# stock.deletall('stock')
#
net = NetWorker()
# net.get_rep_info('000050')
# set = report.get_all()
# for row in set:
#     print(row)





