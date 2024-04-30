#!/usr/bin/python3
""" Unittest for max_integer([...]) """

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """ Test a  case with a list if  integers """
    
        test_1 = [10, 5, 7, 5]
        self.assertEqual(max_integer(test_1), 10)
    
        """ Test a list with zero as the only integer """    
        self.assertEqual(max_integer([0]), 0)
    
        """ Test case with an empty list """    
        self.assertEqual(max_integer([]), None)
    
        """ Test one number list """
        self.assertEqual(max_integer([1]), 1)
    
        """ Test a list with only zeros """
        test_2 = [0, 0, 0, 0, 0]
        self.assertEqual(max_integer(test_2), 0)
        
        """ Test a list with floating point numbers """
        list_3 = [2.5, 3.6, 7.9, 10.0]
        self.assertAlmostEqual(max_integer(list_3), 10)
        
        """" Testing a list with only negative integers """
        self.assertEqual(max_integer([-2, -5, -1, -10, -40]), -1)
        
        """ Testing a list with both positive and negative integers """
        self.assertEqual(max_integer([-2, 17, 45, -50, -13, -19, 12]), 45)
        
        """ Testing lists with duplicates highest numbers"""
        self.assertEqual(max_integer([1, 2, 7, 4, 7, 2, 1]), 7)
 
        """ Testing list with a large number """
        self.assertEqual(max_integer([1, 1000000]), 1000000)

if __name__ == "__main__":
    unittest.main()