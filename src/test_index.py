import pytest
import index
import index2
def test_uncovered_if():
    assert index2.uncovered_if() == False

def test_fully_covered():
    assert index.fully_covered() == True




