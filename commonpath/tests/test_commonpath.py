import unittest
import commonpath
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
        self.assertEqual(commonpath.natural(self.list2), normpath('/home/user1/tmp'))

    def test_nat_paths_max_depth(self):
        self.assertEqual(commonpath.natural(self.list2, max_depth=3), normpath('/home/user1'))

    def test_abs_paths(self):
        self.assertEqual(commonpath.most(self.list2), normpath('/home'))

    def test_abs_paths_max_depth(self):
        self.assertEqual(commonpath.most(self.list1, max_depth=3), normpath('/home/user1'))
