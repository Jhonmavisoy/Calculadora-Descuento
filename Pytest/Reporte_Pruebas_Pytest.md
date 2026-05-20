# Reporte de Pruebas Unitarias con Pytest (Calculadora de Descuentos)

Este documento detalla la transición, el diseño y los resultados de la implementación de pruebas unitarias utilizando **Pytest** para la calculadora de descuentos en `calculadora.py`.

---

## 1. ¿Por qué cambiar a Pytest?

Aunque la suite de pruebas original estaba escrita en `unittest` (el módulo estándar de Python), **Pytest** ofrece ventajas significativas en términos de legibilidad, mantenibilidad y concisión.

### Tabla Comparativa: `unittest` vs. `pytest`

| Característica | `unittest` (Antiguo) | `pytest` (Nuevo) | Beneficio con Pytest |
| :--- | :--- | :--- | :--- |
| **Sintaxis de Aserción** | Requiere métodos específicos como `self.assertEqual(...)` o `self.assertRaises(...)` | Utiliza la palabra clave nativa de Python `assert` y `pytest.raises(...)` | Mucho más natural de leer y escribir; no requiere memorizar docenas de métodos. |
| **Estructura del Test** | Obliga a usar clases orientadas a objetos heredando de `unittest.TestCase` | Permite escribir funciones independientes simples o clases si se prefiere | Código más limpio, directo y con menos boilerplate (código repetitivo). |
| **Pruebas Parametrizadas** | Requiere subtests complejos o bucles manuales propensos a ocultar fallos | Decorador `@pytest.mark.parametrize` nativo | Permite probar decenas de casos de borde en una sola función con reportes individuales impecables. |
| **Salida en Consola** | Salida estándar en blanco y negro, a veces difícil de leer en fallos complejos | Reportes altamente visuales a color con reconstrucción detallada del fallo | Diagnóstico y depuración extremadamente rápidos. |

---

## 2. Estructura de las Pruebas Creadas

Hemos creado un archivo de pruebas unificado y moderno: **`Pytest/test_calculadora_pytest.py`**. Este archivo reemplaza y optimiza la lógica dispersa en múltiples archivos `test_r*.py`, reduciendo drásticamente la duplicación de código usando **parametrización**.

### Código de Pruebas (`Pytest/test_calculadora_pytest.py`)

A continuación se muestra un resumen de la implementación:

```python
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from calculadora import calcular_precio_final

# 1. Pruebas de cálculo de descuento estándar (R3 y R6)
@pytest.mark.parametrize("precio, descuento, resultado_esperado", [
    (100, 20, 80.0),        # Descuento normal entero
    (100, 0, 100.0),        # Sin descuento
    (100, 33.33, 66.67),    # Descuento con decimales (R6 exitoso)
    (50.55, 15, 42.97),     # Precio con decimales y redondeo (R4)
])
def test_calculo_descuento_exitoso(precio, descuento, resultado_esperado):
    """Verifica que el cálculo sea correcto y redondeado a 2 decimales."""
    assert calcular_precio_final(precio, descuento) == resultado_esperado

# 2. Pruebas de límites de descuento inválidos (R1)
@pytest.mark.parametrize("descuento", [-1, -0.01, 101, 100.1])
def test_descuento_fuera_de_rango(descuento):
    """Verifica que se lance ValueError si el descuento está fuera de [0, 100]."""
    with pytest.raises(ValueError, match="El descuento debe estar entre 0 y 100"):
        calcular_precio_final(100, descuento)

# 3. Pruebas de límites de precio inválidos (R2)
@pytest.mark.parametrize("precio", [0, -1, -0.01])
def test_precio_invalido(precio):
    """Verifica que se lance ValueError si el precio original <= 0."""
    with pytest.raises(ValueError, match="El precio original debe ser positivo"):
        calcular_precio_final(precio, 10)

# 4. Pruebas de la promoción especial >= 80% (R5)
@pytest.mark.parametrize("precio, descuento, resultado_esperado", [
    (1000, 80, 190.0),   # 1000 * 0.20 = 200; 200 * 0.95 = 190.0
    (100, 90, 9.5),      # 100 * 0.10 = 10; 10 * 0.95 = 9.5
    (100, 79.9, 20.1),   # 79.9% de descuento (sin promo adicional)
])
def test_promocion_descuento_alto(precio, descuento, resultado_esperado):
    """Verifica el 5% de descuento adicional acumulado para descuentos >= 80%."""
    assert calcular_precio_final(precio, descuento) == resultado_esperado
```

---

## 3. Resultados de la Ejecución

Ejecutamos la suite utilizando el comando:
```bash
python -m pytest Pytest/test_calculadora_pytest.py -v
```

### Evidencia de la Consola

```text
============================= test session starts =============================
platform win32 -- Python 3.10.11, pytest-9.0.3, pluggy-1.6.0
cachedir: .pytest_cache
rootdir: C:\Antigravity
collected 14 items

Pytest/test_calculadora_pytest.py::test_calculo_descuento_exitoso[100-20-80.0] PASSED [  7%]
Pytest/test_calculadora_pytest.py::test_calculo_descuento_exitoso[100-0-100.0] PASSED [ 14%]
Pytest/test_calculadora_pytest.py::test_calculo_descuento_exitoso[100-33.33-66.67] PASSED [ 21%]
Pytest/test_calculadora_pytest.py::test_calculo_descuento_exitoso[50.55-15-42.97] PASSED [ 28%]
Pytest/test_calculadora_pytest.py::test_descuento_fuera_de_rango[-1] PASSED     [ 35%]
Pytest/test_calculadora_pytest.py::test_descuento_fuera_de_rango[-0.01] PASSED  [ 42%]
Pytest/test_calculadora_pytest.py::test_descuento_fuera_de_rango[101] PASSED    [ 50%]
Pytest/test_calculadora_pytest.py::test_descuento_fuera_de_rango[100.1] PASSED  [ 57%]
Pytest/test_calculadora_pytest.py::test_precio_invalido[0] PASSED               [ 64%]
Pytest/test_calculadora_pytest.py::test_precio_invalido[-1] PASSED              [ 71%]
Pytest/test_calculadora_pytest.py::test_precio_invalido[-0.01] PASSED           [ 78%]
Pytest/test_calculadora_pytest.py::test_promocion_descuento_alto[1000-80-190.0] PASSED [ 85%]
Pytest/test_calculadora_pytest.py::test_promocion_descuento_alto[100-90-9.5] PASSED [ 92%]
Pytest/test_calculadora_pytest.py::test_promocion_descuento_alto[100-79.9-20.1] PASSED [100%]

============================= 14 passed in 0.06s ==============================
```

> [!NOTE]
> **Pytest ejecutó 14 casos de prueba distintos**, cubriendo exhaustivamente todos los escenarios positivos, límites negativos y condiciones promocionales del sistema. Todas pasaron exitosamente (`PASSED`) en apenas **0.06 segundos**.

---

## 4. Cómo continuar usando Pytest en este proyecto

Puedes ejecutar tus pruebas de diferentes maneras desde la terminal en el directorio raíz (`C:\Antigravity`):

*   **Ejecutar solo el archivo de Pytest en la carpeta específica:**
    ```bash
    python -m pytest Pytest/test_calculadora_pytest.py -v
    ```

*   **Ejecutar el paso a paso en la carpeta específica:**
    ```bash
    python -m pytest Pytest/test_calculadora_paso_a_paso.py -v
    ```
