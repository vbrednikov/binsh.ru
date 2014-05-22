#!/usr/bin/env python
from nose.tools import nottest
import unittest

class TestExample(unittest.TestCase):
  def example_test_1(self):
    assert 1==1
  
  def example_test_2(self):
    assert 2*2==4

  def example_test_12_runme(self):
    self.assertEqual( [{1:3, 5:10, 5:15}], [{1:4, 5:10, 5:15}])

if __name__=="__main__":
  import nose
  import os
  os.environ['NOSE_VERBOSE']="2"
  os.environ['NOSE_DETAILED_ERRORS']="1"
  os.environ['NOSE_TESTMATCH']=".*_runme"
  nose.runmodule()
