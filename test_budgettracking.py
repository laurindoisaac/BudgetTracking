# test_budgettracking.py
"""
Tests for BudgetTracking module.
"""

import unittest
from budgettracking import BudgetTracking

class TestBudgetTracking(unittest.TestCase):
    """Test cases for BudgetTracking class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BudgetTracking()
        self.assertIsInstance(instance, BudgetTracking)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BudgetTracking()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
