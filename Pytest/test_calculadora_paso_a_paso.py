import sys
import os
import pytest

# Agregar el directorio principal al PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculadora import calcular_precio_final

# ==============================================================================
# PASO 2: PRUEBAS DE CÁLCULO DE DESCUENTO ESTÁNDAR
# ==============================================================================

def test_calculo_descuento_basico():
    """Paso 2: Comprobar el cálculo de descuento básico sin promociones especiales."""
    # $100 con 20% de descuento -> $80.0
    assert calcular_precio_final(100, 20) == 80.0

def test_calculo_sin_descuento():
    """Paso 2: Comprobar que si el descuento es 0%, el precio se mantiene igual."""
    # $100 con 0% de descuento -> $100.0
    assert calcular_precio_final(100, 0) == 100.0


# ==============================================================================
# PASO 4: PRUEBAS DE LÍMITES DE DESCUENTO INVÁLIDOS (ValueError)
# ==============================================================================

def test_descuento_negativo():
    """Paso 4: Comprobar que un descuento negativo lanza ValueError."""
    with pytest.raises(ValueError, match="El descuento debe estar entre 0 y 100"):
        calcular_precio_final(100, -5)

def test_descuento_mayor_cien():
    """Paso 4: Comprobar que un descuento superior al 100% lanza ValueError."""
    with pytest.raises(ValueError, match="El descuento debe estar entre 0 y 100"):
        calcular_precio_final(100, 105)


# ==============================================================================
# PASO 5: PRUEBAS DE LÍMITES DE PRECIO INVÁLIDOS (ValueError)
# ==============================================================================

def test_precio_original_cero():
    """Paso 5: Comprobar que un precio original de 0 lanza ValueError."""
    with pytest.raises(ValueError, match="El precio original debe ser positivo"):
        calcular_precio_final(0, 10)

def test_precio_original_negativo():
    """Paso 5: Comprobar que un precio original negativo lanza ValueError."""
    with pytest.raises(ValueError, match="El precio original debe ser positivo"):
        calcular_precio_final(-50, 10)


# ==============================================================================
# PASO 6: PRUEBAS DE CARACTERÍSTICAS AVANZADAS (Redondeo y Promociones Especiales)
# ==============================================================================

def test_redondeo_dos_decimales():
    """Paso 6: Comprobar que los resultados con decimales largos se redondean a 2 decimales."""
    # $50.55 con 15% de descuento -> $42.9675 -> Redondea a $42.97
    assert calcular_precio_final(50.55, 15) == 42.97

def test_descuento_con_decimales_exitoso():
    """Paso 6: Comprobar que se pueden procesar descuentos decimales con éxito."""
    # $100 con 33.33% de descuento -> $66.67
    assert calcular_precio_final(100, 33.33) == 66.67

def test_promocion_descuento_alto_80():
    """Paso 6: Comprobar promoción especial: 5% de descuento acumulado si descuento >= 80%."""
    # $1000 con 80% de descuento básico -> $200
    # $200 con 5% de descuento adicional acumulado -> $190.0
    assert calcular_precio_final(1000, 80) == 190.0

def test_promocion_descuento_alto_90():
    """Paso 6: Comprobar promoción especial con un descuento del 90%."""
    # $100 con 90% de descuento básico -> $10
    # $10 con 5% de descuento adicional acumulado -> $9.5
    assert calcular_precio_final(10, 90) == 0.95  # 10 * 0.10 = 1 * 0.95 = 0.95 (basado en $10)
    # Si probamos $100 con 90% de descuento:
    assert calcular_precio_final(100, 90) == 9.5
