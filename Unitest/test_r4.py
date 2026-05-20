import unittest
from calculadora import calcular_precio_final

class TestR4(unittest.TestCase):
    def test_redondeo(self):
        # 50.55 * 0.85 = 42.9675 -> 42.97
        self.assertEqual(calcular_precio_final(50.55, 15), 42.97)

if __name__ == '__main__':
    unittest.main()
