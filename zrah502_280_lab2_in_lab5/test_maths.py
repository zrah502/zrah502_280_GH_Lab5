import unittest     # Import the Python unit testing framework
import maths        # Our code to test


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''

    def test_add(self):
        ''' Tests the add function. '''
        result = maths.add(4,5,2,"convert_base")
        self.assertEqual(result, "1001", "The add function returned an incorrect value!")

    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        result = maths.fibonacci(5)
        self.assertEqual(result, 5, "The fibonacci function returned an incorrect value!")

    
    def test_convert_base_under_10(self):
        result = maths.convert_base(9, 2)
        self.assertEqual(result, "1001", "The convert_base function returned an incorrect value!")
        
    
    def test_convert_base_over_ten(self):
        result = maths.convert_base(9, 12)
        self.assertEqual(result, "9", "The convert_base function returned an incorrect value!")
        
    
    def test_factorial(self):
        result = maths.factorial(4)
        self.assertEqual(result, "24", "The factorial function returned an incorrect value!")
        

# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
