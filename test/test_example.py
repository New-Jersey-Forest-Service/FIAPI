import unittest
import pytest

#example functions/script from pytest docs
def inc(x):
    return x + 1

#test that will fail
def test_fail():
    assert inc(3) == 5

#test that will pass
def test_pass():
    assert inc(4) == 5

