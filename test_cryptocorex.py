# test_cryptocorex.py
"""
Tests for CryptoCoreX module.
"""

import unittest
from cryptocorex import CryptoCoreX

class TestCryptoCoreX(unittest.TestCase):
    """Test cases for CryptoCoreX class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoCoreX()
        self.assertIsInstance(instance, CryptoCoreX)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoCoreX()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
