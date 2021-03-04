import unittest
import FizzBuzz


#unittest class tests
class TestCase(unittest.TestCase):
    def test_fib_9(self): 
        i = 1
        arr = []
        while i <= 100: 
            arr.append(i)
            i+=1 
        self.assertEqual(FizzBuzz.FizzBuzz(), arr) 



if __name__ == '__main__':
    unittest.main(verbosity=2)
