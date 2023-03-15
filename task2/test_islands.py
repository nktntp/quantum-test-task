import unittest
from islands import number_of_islands


class TestIslands(unittest.TestCase):

    def test_case1(self):
        matrix = [[0, 1, 0],
                  [0, 0, 0],
                  [0, 1, 1]]
        
        self.assertEqual(number_of_islands(matrix), 2)
    
    def test_case2(self):
        matrix = [[0, 0, 0, 1],
                  [0, 0, 1, 0],
                  [0, 1, 0, 0]]
        
        self.assertEqual(number_of_islands(matrix), 3)
    
    def test_case3(self):
        matrix = [[0, 0, 0, 1],
                  [0, 0, 1, 1],
                  [0, 1, 0, 1]]
        
        self.assertEqual(number_of_islands(matrix), 2)
    
    def test_case4(self):
        matrix = [[1, 1, 1, 1, 1],
                  [0, 0, 1, 0, 0],
                  [1, 1, 1, 1, 1]]
        
        self.assertEqual(number_of_islands(matrix), 1)


if __name__ == "__main__":
    unittest.main()