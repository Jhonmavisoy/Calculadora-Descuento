import unittest
from calculadora import calcular_precio_final

class TestR2(unittest.TestCase):
    def test_precio_cero(self):
        with self.assertRaises(ValueError):
            calcular_precio_final(0, 20)

    def test_precio_negativo(self):
        with self.assertRaises(ValueError):
            calcular_precio_final(-50, 20)

if __name__ == '__main__':
    unittest.main()
