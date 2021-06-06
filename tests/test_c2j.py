import unittest
import os
import sys
from c2j.transform import csv_json, json_csv

sys.path.append(os.path.join(os.path.abspath(os.curdir), 'c2j'))


class c2j_test(unittest.TestCase):

    def test_csv_json(self):
        res1 = []
        os.chdir('tests\jsontest')
        path = os.path.abspath('1.csv')
        csv_json(path)
        for ad, dirs, fil in os.walk(os.path.abspath(os.curdir)):
            for f in fil:
                res1.append(f)
        if 'yourjsonfile.json' in res1:
            test_result = True
        self.assertTrue(test_result)

    def test_json_csv(self):
        res2 = []
        os.chdir('..\csvtest')
        path = os.path.abspath('1.json')
        json_csv(path)
        for ad, dirs, fil in os.walk(os.path.abspath(os.curdir)):
            for f in fil:
                res2.append(f)
        if 'yourcsvfile.csv' in res2:
            test_result = True
        self.assertTrue(test_result)
