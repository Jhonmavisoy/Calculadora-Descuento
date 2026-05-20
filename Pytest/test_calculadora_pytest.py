import sys
import os
import pytest

# Agregamos el directorio principal al PATH para poder importar "calculadora" desde la carpeta Pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculadora import calcular_precio_final

# 1. Pruebas de cálculo de descuento estándar (Requisito 3 y Requisito 6 decimales)
@pytest.mark.parametrize("precio, descuento, resultado_esperado", [
    (100, 20, 80.0),        # Descuento normal entero
    (100, 0, 100.0),        # Sin descuento
    (100, 33.33, 66.67),    # Descuento con decimales (R6 exitoso)
    (50.55, 15, 42.97),     # Precio con decimales y redondeo (R4)
])
def test_calculo_descuento_exitoso(precio, descuento, resultado_esperado):
    """Verifica que el cálculo del precio final con descuento sea correcto y redondeado a 2 decimales."""
    assert calcular_precio_final(precio, descuento) == resultado_esperado

# 2. Pruebas de límites de descuento inválidos (Requisito 1)
@pytest.mark.parametrize("descuento", [
    -1,     # Por debajo del mínimo (0)
    -0.01,  # Por debajo del mínimo decimal
    101,    # Por encima del máximo (100)
    100.1,  # Por encima del máximo decimal
])
def test_descuento_fuera_de_rango(descuento):
    """Verifica que se lance un ValueError si el descuento no está entre 0 y 100."""
    with pytest.raises(ValueError, match="El descuento debe estar entre 0 y 100"):
        calcular_precio_final(100, descuento)

# 3. Pruebas de límites de precio inválidos (Requisito 2)
@pytest.mark.parametrize("precio", [
    0,      # Límite inferior (cero)
    -1,     # Precio negativo
    -0.01,  # Precio negativo decimal
])
def test_precio_invalido(precio):
    """Verifica que se lance un ValueError si el precio original no es mayor que cero."""
    with pytest.raises(ValueError, match="El precio original debe ser positivo"):
        calcular_precio_final(precio, 10)

# 4. Pruebas de la promoción especial de descuento >= 80% (Requisito 5)
@pytest.mark.parametrize("precio, descuento, resultado_esperado", [
    (1000, 80, 190.0),   # 1000 * 0.20 = 200; 200 * 0.95 = 190.0
    (100, 90, 9.5),      # 100 * 0.10 = 10; 10 * 0.95 = 9.5
    (100, 79.9, 20.1),   # 79.9% de descuento (sin promo adicional)
])
def test_promocion_descuento_alto(precio, descuento, resultado_esperado):
    """Verifica que se aplique un 5% de descuento adicional acumulado si el descuento es >= 80%."""
    assert calcular_precio_final(precio, descuento) == resultado_esperado
