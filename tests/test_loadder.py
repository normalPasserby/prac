from unittest import TestCase
from Loadder import *
from db.DAO import (
    report,
    test_mode,
)
class TestLoadder(TestCase):

    def setUp(self):
        test_mode()
        report.deletall('report')
        report.deletall('stock')

    def test_convert_to_load_url(self):
        url = 'http://www.cninfo.com.cn/cninfo-new/disc' \
              'losure/szse_main/bulletin_detail/true/1201986606?announceTime=2016-02-19'
        load_url = convert_to_load_url(url)
        ans = 'http://www.cninfo.com.cn/cninfo-new/disclosure/szse_m' \
              'ain/download/1201986606?announceTime=2016-02-19'
        self.assertEqual(load_url, ans)

    def test_get_urls(self):
        url = 'http://www.cninfo'
        report.save('242swe', 4,url, 'type')
        lo = Loadder()
        set = lo.get_urls()

        ans = [('242swe', 4, 'http://www.cninfo', 'type', 'false')]
        self.assertEqual(set, ans)


    def  test_get_stock_name(self):
        stock.save_stock(1,'efde')
        lo = Loadder()
        an = lo.get_stock_name(1)
        self.assertEqual(an, 'efde')



