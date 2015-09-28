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
    list3 = [
        'C:\\Users\\Adam Smith\\Documents\\doc1.txt',
        'C:\\Users\\Adam Smith\\Documents\\doc2.txt',
        'C:\\Users\\log.txt',
        'D:\\doc4.txt',
        'C:\\Users\\Adam Smith\\Documents\\doc3.txt',
        'C:\\Users\\Adam Smith\\Documents\\Folder\\image.jpg'
    ]

    def test_nat_paths(self):
        self.assertEqual(commonpath.natural(self.list2), normpath('/home/user1/tmp'))

    def test_nat_paths_list3(self):
        self.assertEqual(commonpath.natural(self.list3), normpath('C:\\Users\\Adam Smith\\Documents'))

    def test_nat_paths_max_depth(self):
        self.assertEqual(commonpath.natural(self.list2, max_depth=3), normpath('/home/user1'))

    def test_most_paths(self):
        self.assertEqual(commonpath.most(self.list2), normpath('/home'))

    def test_most_paths_list3(self):
        self.assertEqual(commonpath.most(self.list3), normpath('C:\\Users'))

    def test_most_paths_max_depth(self):
        self.assertEqual(commonpath.most(self.list1, max_depth=3), normpath('/home/user1'))

    def test_common_paths(self):
        self.assertEqual(commonpath.common(self.list2),  normpath('/home'))

    def test_common_paths_list3(self):
        self.assertIsNone(commonpath.common(self.list3))
