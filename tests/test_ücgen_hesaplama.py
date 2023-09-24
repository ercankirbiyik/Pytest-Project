import pytest


def cevre_hesaplama(a, b, c):
    return a+b+c

def alan_hesaplama(taban, yükseklik):
    return  (taban*yükseklik)/2

@pytest.fixture()
def ucgen():
    print("Fixture anatasyonu için oluşturulmuş fonksiyon başladı...")
    yield  # Testten önce bir kere yukarıdaki işlemi yapacak ve en sonda da aşağıdaki işlemi yapacak anlamına gelir
    print("Fixture anatasyonu için oluşturulmuş fonksiyon bitti...")


@pytest.mark.smoke
def test_cevre_hesaplama():
    assert cevre_hesaplama(3, 4, 5) == 12
    print(" 'Çevre hesaplama' ")


# xfail anatasyonu bu testin başarısız olacağını gösteren anatasyon ve ignore edecektir
@pytest.mark.xfail(reason = "Testlerin neden xfail olarak işaretlendiğine dair açıklama")
def test_cevre_hesaplama2():
    assert cevre_hesaplama(3, 4, 7) == 14
    print(" 'Çevre hesaplama' ")


@pytest.mark.regresion
@pytest.mark.smoke
def test_alan_hesaplama():
    assert alan_hesaplama(12, 9) == 54


# xfail anatasyonu bu testin başarısız olacağını gösteren anatasyon ve ignore edecektir
@pytest.mark.xfail(reason = "Testlerin neden xfail olarak işaretlendiğine dair açıklama")
def test_alan_hesaplama2():
    assert alan_hesaplama(12, 9) == 54

@pytest.mark.fixture
def test_cevre_hesaplama3(ucgen):
    print("Üçgen 3 çevre hesaplandı")
    assert cevre_hesaplama(3, 4, 5) == 12


@pytest.mark.fixture
def test_alan_hesaplama3(ucgen):
    print("Üçgen 3 alan hesaplandı")
    assert alan_hesaplama(12, 9) == 54