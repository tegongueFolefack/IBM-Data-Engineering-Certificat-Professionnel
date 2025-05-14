# Import the 'unittest' module to create unit tests for your code.
import unittest

# Import the 'square' and 'double' functions from the 'mymodule' module.
from mymodule import add

# Define a test case class for testing the 'square' function.
# A test case is a single unit of testing. It checks a specific aspect of the code's behavior.
class TestSquare(unittest.TestCase): 

    # Define the first test method for the 'square' function.
    # Test methods should start with the word 'test' so that the test runner recognizes them as test cases.
    def test1(self): 
        # Check that calling 'square(2)' returns 4.
        # This tests if the function correctly computes the square of 2.
        self.assertEqual(add(2,4), 6) # test when 2 is given as input the output is 4.

        # Check that calling 'square(3.0)' returns 9.0.
        # This tests if the function correctly computes the square of 3.0, verifying that it handles float inputs.
        self.assertEqual(add(0,0), 0)  # test when 3.0 is given as input the output is 9.0.
        
        self.assertEqual(add(2.3,3.6), 5.9)  # test when 3.0 is given as input the output is 9.0.

        self.assertEqual(add("hello","world"), "helloworld")  # test when 3.0 is given as input the output is 9.0.

        # Check that calling 'square(-3)' does not return -9.
        # This tests that the function's output is not -9, verifying that the square of -3 should be 9.
        self.assertNotEqual(add(-3,-3), -6)  # test when -3 is given as input the output is not -9.


unittest.main()
Next