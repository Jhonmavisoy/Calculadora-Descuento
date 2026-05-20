from calculadora import calcular_precio_final

def test_descuento_basico():
    assert calcular_precio_final(100, 10) == 90