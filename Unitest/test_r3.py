import unittest
from calculadora import calcular_precio_final

class TestR3(unittest.TestCase):
    def test_calculo_normal(self):
        self.assertEqual(calcular_precio_final(100, 20), 80.0)

if __name__ == '__main__':
    unittest.main()
