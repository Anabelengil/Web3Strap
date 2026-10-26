# test_web3strap.py
"""
Tests for Web3Strap module.
"""

import unittest
from web3strap import Web3Strap

class TestWeb3Strap(unittest.TestCase):
    """Test cases for Web3Strap class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = Web3Strap()
        self.assertIsInstance(instance, Web3Strap)

    def test_run_method(self):
        """Test the run method."""
        instance = Web3Strap()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
