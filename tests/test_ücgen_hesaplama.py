def cevre_hesaplama(a, b, c):
    return a+b+c

def alan_hesaplama(taban, yükseklik):
    return  (taban*yükseklik)/2

def test_cevre_hesaplama():
    assert cevre_hesaplama(3, 4, 5) == 12

def test_alan_hesaplama():
    assert alan_hesaplama(12, 9) == 54

