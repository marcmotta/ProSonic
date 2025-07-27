# test_prosonic.py
"""
Tests for ProSonic module.
"""

import unittest
from prosonic import ProSonic

class TestProSonic(unittest.TestCase):
    """Test cases for ProSonic class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ProSonic()
        self.assertIsInstance(instance, ProSonic)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ProSonic()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
