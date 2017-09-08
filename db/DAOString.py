CREATE_STOCK = '''CREATE TABLE STOCK
       (STOCK_ID    INTEGER PRIMARY KEY     NOT NULL,
        STOCK_NAME  TEXT         NOT NULL,
        RECENT_YEAR        INTEGER       );'''

CREATE_REP = '''CREATE TABLE report
       (REP_NAME    TEXT    PRIMARY KEY     NOT NULL,
        STOCK_ID    INTEGER                 NOT NULL,
        REP_URL     TEXT                NOT NULL,
        REP_TYPE    TEXT                NOT NULL,
        loaded      TEXT                NOT NULL,
        FOREIGN KEY (STOCK_ID) REFERENCES STOCK(STOCK_ID));'''

#临时存储待下载
#CRE

# def create_table(sql, dbname):
#     conn = get_con(dbname)
#     conn.execute(sql)
#     conn.close()
DBPATH = r'E:\stock\py_pro\db\myst.db'
TESTPATH = r'E:\stock\py_pro\db\test.db'

INSERT_STO = "INSERT INTO STOCK (STOCK_ID,STOCK_NAME,RECENT_YEAR) \
          VALUES (%d, '%s', 0)"
DEL_STO = "delete from stock where STOCK_ID=%d"
UPDATE_TEAR = 'UPDATE stock SET recent_year = %d WHERE STOCK_ID = %d '
SELid = 'select * from STOCK where stock_id=%s'
SEL_not_updated = "select * from STOCK where recent_year <= %d"


INSERT_REP = "INSERT INTO REPORT (REP_NAME,STOCK_ID,REP_URL,REP_TYPE,loaded) \
          VALUES (?, ?, ?, ?, 'false')"
DEL_REP = "delete from REPORT where REP_ID=?"
SEL_name = "select * from REPORT where REP_NAME='%s'"
UPDATE_loaded = "UPDATE REPORT SET loaded = 'true' WHERE REP_NAME = '%s' "
SEL_not_loaded = "select * from REPORT where STOCK_ID=%d AND loaded='false' "
SEL_ALL = "select * from REPORT "
SEL_not_loaded_all = "select * from REPORT where loaded='false' "


