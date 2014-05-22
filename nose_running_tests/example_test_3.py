#!/usr/bin/env python
class TestExample:
  def example_test_1(self):
    assert 1 == 1
  def example_test_2(self):
    assert 2*2 == 4

if __name__=="__main__":
  import nose
  nose.runmodule(argv=['__file__', '-v', '-d'])
