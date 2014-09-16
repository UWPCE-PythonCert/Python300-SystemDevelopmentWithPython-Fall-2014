import unittest

from branch import branch

class TestBranch(unittest.TestCase):

    def test_branch_true(self):
        branch(True)
        self.assertTrue(True) # do a real test here

    def test_branch_false(self):
        branch(False)
        self.assertTrue(True) # do a real test here
