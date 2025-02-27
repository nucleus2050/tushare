# -*- coding:utf-8 -*- 
'''
Created on 2015/3/14
@author: Jimmy Liu
'''
import unittest
import tushare.stock.trading as fd

class Test(unittest.TestCase):

    def set_data(self):
        self.code = '000001'
        self.start = '2020-01-03'
        self.end = '2023-01-16'
        self.year = 2014
        self.quarter = 4
        
    # def test_get_hist_data(self):
    #     self.set_data()
    #     # df = fd.get_hist_data(self.code, self.start,ktype='5')
    #     df = fd.get_hist_data(self.code, self.start,self.start,ktype='5')
    #     print(df)

    def test_get_h_data(self):
        df = fd.get_hist_data('000001',start='2019-05-20',end='2022-07-21')
        print(df)

    # def test_get_index(self):
    #     df = fd.get_index()
    #     print(df)

    # def test_get_tick_data(self):
    #     self.set_data()
    #     df = fd.get_tick_data(self.code, self.end)
    #     print(df)

    # def test_get_today_all(self):
    #     print(fd.get_today_all())
    #
    # def test_get_realtime_quotesa(self):
    #     self.set_data()
    #     print(fd.get_realtime_quotes(self.code))

    # def test_get_h_data(self):
    #     self.set_data()
    #     print(fd.get_h_data(self.code, self.start, self.end))

    # def test_get_today_ticks(self):
    #     self.set_data()
    #     print(fd.get_today_ticks(self.code))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()