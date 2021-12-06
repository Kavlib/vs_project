"""Module script."""


def product(a, b):
    """Redsf dsdfd sdfdffd.

    >>> product(3,2)
    6
    >>> product(2,5)
    10
    """
    # sdfi lskdjflksdfj

    return a*b


def increment(a):
    """Increment number."""
    return a+1


def decrement(a):
    """Decrement number.

    Decrement number with minus 1
    >>> decrement(1)
    0
    """
    return a-1


def sum(a, b):
    """Sum of two.

    >>> sum(1,1)
    2
    """
    return a+b


def test_product():
    """Test product function."""
    assert product(5, 6) == 30
    assert product(4, 3) == 12


def test_increment():
    """Test increment function."""
    assert increment(1) == 2


if __name__ == '__main__':
    c = product(3, 4)
    print(c)
