import unittest
from calculadora import calcular_precio_final

class TestR1(unittest.TestCase):
    def test_descuento_negativo(self):
        with self.assertRaises(ValueError):
            calcular_precio_final(100, -5)

    def test_descuento_mayor_100(self):
        with self.assertRaises(ValueError):
            calcular_precio_final(100, 105)

if __name__ == '__main__':
    unittest.main()
