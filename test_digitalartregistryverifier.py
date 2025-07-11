# test_digitalartregistryverifier.py
"""
Tests for DigitalArtRegistryVerifier module.
"""

import unittest
from digitalartregistryverifier import DigitalArtRegistryVerifier

class TestDigitalArtRegistryVerifier(unittest.TestCase):
    """Test cases for DigitalArtRegistryVerifier class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DigitalArtRegistryVerifier()
        self.assertIsInstance(instance, DigitalArtRegistryVerifier)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DigitalArtRegistryVerifier()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
