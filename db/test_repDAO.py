from unittest import TestCase
from db.DAO import (
    RepDAO,
    test_mode,
)


class TestRepDAO(TestCase):
    def setUp(self):
        test_mode()
        self.obj = RepDAO()
        obj = self.obj
        obj.set_testmode()
        obj.deletall('report')

    def test_get_rep(self):
        obj = self.obj
        url = r'http://blog.csdn.net/wklken/article/details/6312870'
        name = '2044年度报告'
        obj.save(name, 1, url, '年度报告')
        set = obj.get_rep(name)
        self.assertEqual(set[0][0], name)
        self.assertEqual(set[0][1], 1)
        self.assertEqual(set[0][2], url)
        self.assertEqual(set[0][3], '年度报告')

    def test_update_flag(self):
        obj = self.obj
        url = r'http://blog.csdn.net/wklken/article/details/6312870'
        name = '2022年度报告'
        obj.save(name, 1, url, '年度报告')

        obj.update_flag(name)
        set = obj.get_rep(name)

        self.assertEqual(set[0][0], name)
        self.assertEqual(set[0][4], 'true')

    def test_unloaded_reps(self):
        obj = self.obj

        url = r'httails/6312870'
        name = '2011年度报告'
        obj.save(name, 1, url, '年度报告')

        name2 = '2022年度报告'
        obj.save(name2, 1, url, '年度报告')

        obj.update_flag(name)
        set = obj.unloaded_rep(1)
        self.assertEqual(set[0][0], name2)




