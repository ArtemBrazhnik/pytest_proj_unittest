import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], -1, "test"), "test")

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1, -2), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -1), [4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, 2), [1, 2])
        self.assertEqual(arrs.my_slice([], 1, 4), [])
        self.assertEqual(arrs.my_slice([1, 2, 3], -4, 3), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 0, 4), [1, 2, 3, 4])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 4), [2, 3, 4])
