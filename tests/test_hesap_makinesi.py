def toplama(a, b):
    return a+b

def çıkarma(a, b):
    return a-b

def çarpma(a, b):
    return a*b

def bölme(a, b):
    return a/b

def test_toplama():
    assert 4 == toplama(2, 2)

def test_çıkarma():
    assert çıkarma(3, 2) == 1

def test_çarpma():
    assert 13 != çarpma(3, 4)

def test_bölme():
    assert 11.7 != bölme(36, 3.1)


def test_toplama2():
    assert toplama(4, 7) == 12

def test_çarpma2():
    assert çarpma(12, 1.1) == 13