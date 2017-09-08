from unittest import TestCase
from driver import NetWorker
from db.DAO import (
    stock,
    report,
    test_mode
)


class TestNetWorker(TestCase):
    def setUp(self):
        test_mode()

        report.set_testmode()
        report.deletall('report')

        stock.set_testmode()
        stock.deletall('stock')

    def test_check_info_exist(self):
        stock.save_stock(101, 'deew')
        net = NetWorker()
        try:
            net.check_info_exist(101)
        except RuntimeError as e:
            str = '101 has exist'
            self.assertEqual(e.__str__(), str)


    def test_write_stock_info(self):
        net = NetWorker()
        net.write_stock_info('2011公司', 23, r'www.fefs/', '年度报告')
        set = report.get_rep('2011公司')
        row = set[0]
        self.assertEqual(row[1], 23)