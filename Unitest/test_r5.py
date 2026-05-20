import unittest
from calculadora import calcular_precio_final

class TestR5(unittest.TestCase):
    def test_promo_80(self):
        # 1000 * 0.20 = 200 -> 200 * 0.95 = 190.0
        self.assertEqual(calcular_precio_final(1000, 80), 190.0)

if __name__ == '__main__':
    unittest.main()
