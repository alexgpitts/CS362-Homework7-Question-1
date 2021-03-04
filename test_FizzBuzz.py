import unittest
import FizzBuzz


#unittest class tests
class TestCase(unittest.TestCase):

    #A test that checks a number divisible by 3 and 5
    def test_FizzBuzz_1(self): 
        self.assertEqual(FizzBuzz.FizzBuzz(15), "FizzBuzz") 

    #A test that checks a number divisible by 3 and not 5
    def test_FizzBuzz_2(self): 
        self.assertEqual(FizzBuzz.FizzBuzz(12), "Fizz") 

    #A test that checks a number divisible by 5 and not 3
    def test_FizzBuzz_3(self): 
        self.assertEqual(FizzBuzz.FizzBuzz(20), "Buzz") 



if __name__ == '__main__':
    unittest.main(verbosity=2)
