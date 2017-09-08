import sqlite3,os
import warnings

from db.DAOString import *

def creatdb():
    if not os.path.exists(DBPATH):
        con = get_con()
        con.execute(CREATE_STOCK)
        con.execute(CREATE_REP)
        con.close()

def get_con_on_st():
    con = sqlite3.connect(DBPATH)
    return con

def get_con_on_test():
    con = sqlite3.connect(TESTPATH)
    return con

def test_mode():
    get_con = get_con_on_test
    if not os.path.exists(TESTPATH):
        con = get_con()
        con.execute(CREATE_STOCK)
        con.execute(CREATE_REP)
        con.close()

get_con = get_con_on_st


class DAO():
    # def __init__(self):
    #     self.tbname = ''
    def insert(self, obj):
        pass


    def update(self):
        pass

    def delete(self, id):
        conn = get_con()
        def choose(tbname):
            if tbname == 'stock':
                sql = "delete from stock where STOCK_ID="
            elif tbname == 'report':
                sql = "delete from report where REP_ID="
            else:
                warnings.warn(
                    'wrong tbname')
                return None
            return sql
        sql = choose(tbname) + str(id)
        conn.execute(sql)
        conn.commit()
        conn.close()

    def set_testmode(self):
        self.testmode = 'true'


    def deletall(self, tb):
        #测试用
        if 'true' == 'true':
            sql = "delete from " + tb
            self.exu(sql)
        # else:
        #     raise RuntimeError('not testmode')


    def exu_has_ret(self, sql):
        conn = get_con()
        cur = conn.execute(sql)
        set = cur.fetchall()
        cur.close()
        return set

    def exu(self, sql, obj=None):
        conn = get_con()
        if obj is None:
            conn.execute(sql)
        else:
            conn.execute(sql, obj)
        conn.commit()
        conn.close()

class stockDAO(DAO):
    def __init__(self):
        super().__init__()

    def save_stock(self, id, name):
        sql = INSERT_STO % (id, name)
        self.exu(sql)

    def get_stock_not_updated(self, year):
        sql = SEL_not_updated % (year)
        set = self.exu_has_ret(sql)
        return set

    def update_year(self, id, year):
        obj = (year, id)
        sql = UPDATE_TEAR % obj
        self.exu(sql)


    def get_all_stock(self):
        sql = "select * from STOCK"
        set = self.exu_has_ret(sql)
        return set

    def select(self, id):
        sql = SELid % id
        set = self.exu_has_ret(sql)
        return set

    def delete(self, id):
        sql = DEL_STO % (id)
        self.exu(sql)


class RepDAO(DAO):
    def __init__(self):
        super().__init__()

    def save(self, name, id, url, type):
        obj = (name, id, url, type)
        self.exu(INSERT_REP, obj)

    def unloaded_rep(self, stockid):
        sql = SEL_not_loaded % stockid
        set = self.exu_has_ret(sql)
        return set

    def unloaded_reps(self):
        set = self.exu_has_ret(SEL_not_loaded_all)
        return set

    def update_flag(self, name):
        self.exu(UPDATE_loaded % name)

    def get_rep(self, repname):
        sql = SEL_name % repname
        set = self.exu_has_ret(sql)
        return set

    def get_all(self):
        set = self.exu_has_ret(SEL_ALL)
        return set


creatdb()
stock = stockDAO()
report = RepDAO()



# test_mode()

# test_mode()
# obj = RepDAO()
#
# # obj.set_testmode()
# # obj.deletall('report')
#
# url = r'http://blog.csdn.net/wklken/article/details/6312870'
# name = '2044年度报告'
# # obj.save(1, name, url, '年度报告')
#
# sql = "select * from REPORT where REP_NAME='2044年度报告'"
# conn = get_con()
# cur = conn.execute(sql)
# set = cur.fetchall()
# cur.close()
# print(set)