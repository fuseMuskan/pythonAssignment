import unittest
from main import sum


class TestArgumentFunctions(unittest.TestCase):

    def test_sum(self):
        """Test Cases for sum function
        """
        self.assertEqual(sum(1), 1)
        self.assertEqual(sum(1, 2, 3, 4, 5), 15)
        self.assertEqual(sum(-1, 5), 4)
        self.assertEqual(sum(6.5, 0.5), 7)


if __name__ == '__main__':
    unittest.main()
