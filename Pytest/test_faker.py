import sys
import os
from faker import Faker

# Agregar el directorio principal al PATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from calculadora import calcular_precio_final

fake = Faker()

def test_calculos_aleatorios_con_faker():
    """Genera 50 casos de prueba aleatorios y validos usando Faker para estresar la calculadora."""
    for _ in range(50):
        # Faker genera un precio original aleatorio entre 1 y 10,000 con 2 decimales
        precio = float(fake.pydecimal(left_digits=4, right_digits=2, min_value=1))
        
        # Faker genera un descuento valido entre 0 y 100% con 2 decimales
        descuento = float(fake.pydecimal(left_digits=2, right_digits=2, min_value=0, max_value=100))
        
        # Ejecutamos la calculadora con estos datos dinamicos
        precio_final = calcular_precio_final(precio, descuento)
        
        # Validaciones de consistencia logica:
        # 1. El precio final nunca puede ser negativo
        assert precio_final >= 0
        
        # 2. El precio final no puede ser mayor que el precio original
        assert precio_final <= precio
        
        # 3. Si el descuento es del 0%, el precio final debe ser identico al original redondeado
        if descuento == 0:
            assert precio_final == round(precio, 2)
            
        # 4. Si el descuento es del 100%, el precio final debe ser 0.0
        if descuento == 100:
            assert precio_final == 0.0
