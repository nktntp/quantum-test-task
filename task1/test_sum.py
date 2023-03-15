import unittest
import sum

class TestSum(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(sum.solution(1), 1)
        self.assertEqual(sum.solution(3), 6)
        self.assertEqual(sum.solution(10), 55)


if __name__ == "__main__":
    unittest.main()