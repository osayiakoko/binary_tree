import unittest
from binary_tree import BinaryTree


class TestBinaryTree(unittest.TestCase):
    def test_positive(self):
        test_value = 6
        test_list = [1,[2,[3,4,5], 6], [7,8,9]]

        bt = BinaryTree()

        message = "Test vale is not true"
        self.assertTrue(bt.value_in_tree(test_list, 4), message)
        self.assertTrue(bt.value_in_tree(test_list, 6), message)
        self.assertTrue(bt.value_in_tree(test_list, 8), message)


if __name__ == '__main__':
    unittest.main()
