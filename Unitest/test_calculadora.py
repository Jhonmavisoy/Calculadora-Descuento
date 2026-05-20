import unittest
import testtools
from faker import Faker
from calculadora import calcular_precio_final


class TestCalculadoraDescuentosProfundo(testtools.TestCase):

    @classmethod
    def setUpClass(cls):
        """Inicialización del entorno global de QA"""
        # Inicializamos Faker para toda la clase de pruebas
        cls.fake = Faker()
        # Fijamos una semilla para garantizar la replicabilidad del análisis
        cls.seed_value = 42
        cls.fake.seed_instance(cls.seed_value)

    def test_analisis_valores_frontera_subtests(self):
        """[Unittest SubTests] -> Evaluación de límites exactos (0%, 79%, 80%, 100%)"""
        # Diseñamos una matriz de datos con los límites clave del algoritmo
        casos_limite = [
            {"escenario": "Límite inferior exacto (0%)", "precio": 100.0, "desc": 0, "esperado": 100.0},
            {"escenario": "Un paso antes del bono (79%)", "precio": 100.0, "desc": 79, "esperado": 21.0},
            {"escenario": "Aplicación exacta del bono (80%)", "precio": 100.0, "desc": 80, "esperado": 19.0},
            {"escenario": "Límite superior exacto (100%)", "precio": 100.0, "desc": 100, "esperado": 0.0}
        ]

        for caso in casos_limite:
            # Separamos el reporte interno para ver cada límite de forma independiente
            with self.subTest(escenario=caso["escenario"]):
                resultado = calcular_precio_final(caso["precio"], caso["desc"])
                self.assertEqual(resultado, caso["esperado"], f"Error crítico en: {caso['escenario']}")

    def test_descuento_estandar_exito_masivo(self):
        """[Faker + Unittest] -> Prueba de estrés iterativa con 20 transacciones aleatorias"""
        for i in range(20):
            precio_original = round(self.fake.pyfloat(left_digits=3, right_digits=2, min_value=1, max_value=500), 2)
            descuento = self.fake.pyint(min_value=0, max_value=79)
            esperado = round(precio_original * (1 - descuento / 100), 2)

            with self.subTest(iteracion=i, precio=precio_original, desc=descuento):
                resultado = calcular_precio_final(precio_original, descuento)
                self.assertEqual(resultado, esperado)

    def test_super_descuento_con_bono(self):
        """[Unittest] -> Verificación del caso especial de superdescuento >= 80% con bono del 5%"""
        precio_original = round(self.fake.pyfloat(left_digits=3, right_digits=2, min_value=1, max_value=500), 2)
        descuento = self.fake.pyint(min_value=80, max_value=100)

        precio_intermedio = precio_original * (1 - descuento / 100)
        esperado = round(precio_intermedio * 0.95, 2)

        resultado = calcular_precio_final(precio_original, descuento)
        self.assertEqual(resultado, esperado)

    def test_error_descuento_fuera_de_rango(self):
        """[TestTools Exceptions] -> Validación de captura de error para descuentos fuera de rango (0-100)"""
        precio_original = 100.0
        descuento_invalido = self.fake.random_element(elements=[-15, 101, 150, -1])

        with self.assertRaises(ValueError):
            calcular_precio_final(precio_original, descuento_invalido)

    def test_error_precio_no_positivo(self):
        """[TestTools Exceptions] -> Validación de restricción de robustez para precios menores o iguales a cero"""
        precio_invalido = self.fake.random_element(elements=[0, -10, -50.5])
        descuento = 20

        with self.assertRaises(ValueError):
            calcular_precio_final(precio_invalido, descuento)


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("      AUDITORÍA DE QA: DESGLOSE DETALLADO DE PRUEBAS UNITARIAS")
    print("=" * 80)

    # El truco: verbosity=2 obliga a Python a listar cada prueba con su estado individual
    unittest.main(verbosity=2)