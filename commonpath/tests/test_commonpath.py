import unittest
from commonpath import CommonPath
from os.path import normpath


class TestCommonPath(unittest.TestCase):
    list1 = ['/home/user1/tmp/coverage/test',
             '/home/user1/tmp/covert/operator',
             '/home/user1/tmp/coven/members']
    list2 = ['/home',
             '/home/user1/tmp/coverage/test',
             '/home/user1/tmp/covert/operator',
             '/home/user1/tmp/coven/members']

    def test_nat_paths(self):
        self.assertEqual(CommonPath(self.list2).natural(), normpath('/home/user1/tmp'))

    def test_nat_paths_max_depth(self):
        self.assertEqual(CommonPath(self.list2).natural(max_depth=3), normpath('/home/user1'))

    def test_abs_paths(self):
        self.assertEqual(CommonPath(self.list2).absolute(), normpath('/home'))

    def test_abs_paths_max_depth(self):
        self.assertEqual(CommonPath(self.list1).absolute(max_depth=3), normpath('/home/user1'))
