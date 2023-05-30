import pytest
from um import count


def test_input():
    assert count("Um, you sure?") == 1
    assert count("um") == 1
    assert count("Um, if you say so, um..") == 2
    assert count("Um????") == 1
    assert count("Summary") == 0