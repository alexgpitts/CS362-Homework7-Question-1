import unittest
import FizzBuzz


#unittest class tests
class TestCase(unittest.TestCase):

    #A test that checks a number divisible by 3 and 5
    def test_FizzBuzz_1(self): 
        self.assertEqual(FizzBuzz.FizzBuzz(15), "FizzBuzz") 



if __name__ == '__main__':
    unittest.main(verbosity=2)
