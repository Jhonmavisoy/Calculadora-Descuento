import unittest
from calculadora import calcular_precio_final

class TestR6Evidencia(unittest.TestCase):
    def test_descuento_con_decimales_exitoso(self):
        # Prueba variada que pasa correctamente
        self.assertEqual(calcular_precio_final(100, 33.33), 66.67)

    def test_falla_intencional_evidencia_1(self):
        # Fallo de lógica matemática (AssertionError)
        self.assertEqual(calcular_precio_final(100, 20), 50.0, "Forzando error: Cálculo matemáticamente incorrecto")
        
    def test_falla_intencional_evidencia_2(self):
        # Error de tipo de datos (TypeError)
        calcular_precio_final("cien", 10)

    def test_falla_intencional_evidencia_3(self):
        # Fallo asumiendo un requerimiento inexistente de propina obligatoria
        self.assertEqual(calcular_precio_final(50, 0), 55.0, "Forzando error: Falta agregar la propina del 10% (no requerido)")
        
    def test_falla_intencional_evidencia_4(self):
        # Error de falta de parámetros (TypeError)
        calcular_precio_final()

if __name__ == '__main__':
    unittest.main()
