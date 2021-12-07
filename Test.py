def product(a, b):
    return a * b

"""def test_product():"
    assert product(2, 4) == 8"""

if __name__ == '__main__':
    a = int(input('zadej hodnotu a:'))
    b = int(input('zadej hodnotu b:'))
    c = product(a, b)
    print(c)
    