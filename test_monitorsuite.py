# test_monitorsuite.py
"""
Tests for MonitorSuite module.
"""

import unittest
from monitorsuite import MonitorSuite

class TestMonitorSuite(unittest.TestCase):
    """Test cases for MonitorSuite class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MonitorSuite()
        self.assertIsInstance(instance, MonitorSuite)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MonitorSuite()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
