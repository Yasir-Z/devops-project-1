import pytest


def test_addition():
    """Test basic addition."""
    assert 1 + 1 == 2


def test_subtraction():
    """Test basic subtraction."""
    assert 5 - 3 == 2


def test_string_operations():
    """Test string methods."""
    assert "hello".upper() == "HELLO"
    assert "WORLD".lower() == "world"


class TestMathOperations:
    """Test class for math operations."""

    def test_multiplication(self):
        """Test multiplication."""
        assert 2 * 3 == 6

    def test_division(self):
        """Test division."""
        assert 10 / 2 == 5
        assert 7 // 2 == 3  # Floor division

    def test_power(self):
        """Test exponentiation."""
        assert 2**3 == 8
