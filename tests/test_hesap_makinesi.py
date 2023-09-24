import pytest

'''
    'python3 -m pytest -v' komutu ile terminalden bütün testler çalıştırılabilir
    
    '@pytest.mark.skip' anatasyonu bu testi atla anlamına gelir ve testi çalıştırmaz, parantez içinde (reason = '') sebebi belirtilebilir
    
    'pytest.mark.xfail' anatasyonu testin başarısız olacağını gösteren anatasyondur ve test ignore edilir
    
    '@pytest.mark.skipif' anatasyonu parantez içinde verilen koşul sağlanmazsa veya sağlanırsa testi çalıştır anlamına gelir.
    
    'python3 -m pytest -vm smoke' komutu ile sadece @pytest.mark.smoke anatasyonu ile işaretlenmiş testler çalıştırılabilir
       -> smoke bizim kendi verdiğimiz bir işaretleme grubudur, buna istediğimiz ismi verebiliriz...
       -> bir senaryoda birden fazla anatasyon olabilir ve birden fazla işaretleme yapılabilir...
       -> 'python3 -m pytest -vm smoke and elma' komutu ile anatasyonları farklı olan iki ayrı senaryo grubu çalıştırılabilir...
       
       
       
    'Fixture'lar paytestte testten önce ve sonrasında test ortamının hazırlanması veya dataların silinmesi gibi işlemleri yapmamızı sağlayan anatasyondur.
    
'''

sistem = "qa"
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


@pytest.mark.regresion
# skip anatasyonu bu testi atla anlamına gelir ve testi çalıştırmaz
@pytest.mark.skip(reason = "Testlerin neden skip edildiğine dair açıklama")
def test_toplama2():
    assert toplama(4, 7) == 12


# xfail anatasyonu bu testin başarısız olacağını gösteren anatasyon ve ignore edecektir
@pytest.mark.xfail(reason = "Testlerin neden xfail olarak işaretlendiğine dair açıklama")
def test_çarpma2():
    assert çarpma(12, 1.1) == 13


# skipif anatasyonu herhangi bir sebepten bir testin koşmaması ihtimali var ise ve koşumu engelleyen bir durum var ise
# skip edilmesi için verilen anatasyondur

@pytest.mark.elma
@pytest.mark.skipif(sistem == "qa", reason = "qa kodu hatalı olduğu için skip edildi")  # sistem elementi dev yapılır ise test pass olacaktır
def test_çarpma2():
    assert 12 == çarpma(3, 4)


# smoke anatasyonu testlere karışık olarak verilen spesifik bir anatasyon ve koşulması istenen bütün senaryolara verilerek
# terminalde 'python3 -m pytest -vm smoke' komutu ile sadece bu testler çalıştırılabilir
@pytest.mark.smoke
@pytest.mark.regresion
@pytest.mark.elma
def test_bölme2():
    assert 11.7 != bölme(36, 3)
