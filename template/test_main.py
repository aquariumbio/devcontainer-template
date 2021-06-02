"""
Tests for __main__.py
"""
import pytest

from template.__main__ import say_hello

@pytest.mark.parametrize("name, expect", [
    ("Devin", "Hello Devin")
])
def test_say_hello(name, expect):
    """
    Test the text returned by say_hello
    """
    output = say_hello(name)
    assert output == expect
