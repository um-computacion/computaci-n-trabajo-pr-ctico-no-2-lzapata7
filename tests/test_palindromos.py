import unittest
from src.palindromos import is_palindrome

class TestPalindromesSimples(unittest.TestCase):
    
    def test_palindrome_sometemos(self):
        self.assertTrue(is_palindrome("sometemos"))
    
    def test_palindrome_neuquen(self):
        self.assertTrue(is_palindrome("neuquen"))
    
    def test_palindrome_arañara(self):
        self.assertTrue(is_palindrome("arañara"))

if __name__ == '__main__':
    unittest.main()