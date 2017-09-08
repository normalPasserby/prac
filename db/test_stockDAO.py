from unittest import TestCase

from db.DAO import (
    stockDAO,
    test_mode,
)

class TestStockDAO(TestCase):
    def setUp(self):
        test_mode()
        self.sto = stockDAO()
        self.sto.set_testmode()
        self.sto.deletall('stock')

    def test_save_stock(self):
        sto = self.sto
        sto.save_stock(1, 'test')
        set = sto.select(1)
        row = set[0]
        self.assertEqual(row[0], 1)
        self.assertEqual(row[1], 'test')

    def test_update_year(self):
        sto = self.sto
        sto.save_stock(2, 'test')
        sto.update_year(2, 2000)
        set = sto.select(2)
        row = set[0]
        self.assertEqual(row[2], 2000)


    def test_get_stock_not_updated(self):
        sto = self.sto
        sto.save_stock(1, 'test1')
        sto.save_stock(2, 'test2')
        sto.save_stock(3, 'test3')
        sto.update_year(1, 2000)
        sto.update_year(2, 2050)
        set = sto.get_stock_not_updated(2020)
        self.assertEqual(set[0][2], 2000)
        self.assertEqual(set[1][2], 0)

    def test_delete(self):
        sto = self.sto
        sto.save_stock(1, 'test1')
        sto.save_stock(2, 'test2')
        sto.delete(1)
        set = sto.get_stock_not_updated(2020)
        self.assertEqual(set[0][0], 2)