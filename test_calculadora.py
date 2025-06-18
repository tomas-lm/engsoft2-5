import pytest
from calculadora import soma, subtrai, multiplica, divide, quadrado

def test_soma():
    assert soma(2, 3) == 5

def test_subtrai():
    assert subtrai(5, 3) == 2

def test_multiplica():
    assert multiplica(4, 3) == 12

def test_divide():
    assert divide(10, 2) == 5

def test_divide_por_zero():
    import pytest
    with pytest.raises(ValueError):
        divide(10, 0)

def test_quadrado():
    assert quadrado(4) == 16
