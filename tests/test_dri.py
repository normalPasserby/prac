import unittest
from driver import (
    NetWorker,
    get_url_and_name,
)

class driverTest(unittest.TestCase):
    def setUp(self):
        pass

    def testgetpwd(self):
        a= get_url_and_name()
        #print(a)
        self.assertEqual(a, r'E:\stock\report\url_and_name',msg='stock path is wrong!')

    def testwork_info_exist(self):
        self.netw = NetWorker('000000')
        state = self.netw.work()
        self.assertTrue(state is None)



if __name__ =='__main__':
    unittest.main()


