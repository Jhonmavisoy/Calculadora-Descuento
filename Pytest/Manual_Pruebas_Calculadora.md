# Manual de Pruebas: Calculadora de Descuentos
Este manual te guiará paso a paso para realizar pruebas **automatizadas** y **manuales** de la calculadora de descuentos (`calculadora.py`), registrando los resultados de cada ejecución como evidencia de calidad.

---

## 🛠️ PARTE 1: Pruebas Automatizadas con Pytest

Ya tienes a tu disposición una suite de pruebas totalmente implementada en **`Pytest/test_calculadora_pytest.py`** y **`Pytest/test_calculadora_paso_a_paso.py`**.

### Cómo ejecutar las pruebas automatizadas y ver la evidencia:

1.  **Abre tu terminal** en el directorio raíz del proyecto (`C:\Antigravity`).
2.  **Ejecuta el siguiente comando** para correr la suite completa con máximo detalle:
    ```bash
    python -m pytest Pytest/test_calculadora_pytest.py -v
    ```
3.  **Ejecuta el paso a paso detallado:**
    ```bash
    python -m pytest Pytest/test_calculadora_paso_a_paso.py -v
    ```

### Qué debes observar (Evidencia):
Verás una lista verde con el estado de las pruebas. Cada una representa una regla de negocio que se verifica en milisegundos:
*   `test_calculo_descuento_exitoso[...] PASSED` (Verifica cálculos básicos y redondeo).
*   `test_descuento_fuera_de_rango[...] PASSED` (Verifica límites de descuento).
*   `test_precio_invalido[...] PASSED` (Verifica límites de precios).
*   `test_promocion_descuento_alto[...] PASSED` (Verifica el descuento acumulado del 5% adicional si descuento >= 80%).

---

## 💻 PARTE 2: Pruebas Manuales Paso a Paso

Para probar el programa manualmente mediante la **interfaz interactiva de consola**, sigue estos pasos.

### Preparación:
1.  En la terminal, ejecuta el programa interactivo:
    ```bash
    python calculadora.py
    ```
2.  Verás la cabecera interactiva:
    ```text
    =========================================
      Calculadora de Descuentos Interactiva  
    =========================================
    Escribe 'salir' en cualquier momento para terminar.
    ```

---

### 📋 Bitácora de Casos de Prueba Manuales

Sigue esta secuencia exacta ingresando los datos solicitados. Anota los resultados y compáralos con el comportamiento esperado:

#### **Caso de Prueba 1: Cálculo de Descuento Básico**
*   **Propósito:** Verificar que descuenta correctamente un porcentaje entero normal.
*   **Entradas:**
    *   Precio original: `100`
    *   Porcentaje de descuento: `20`
*   **Comportamiento Esperado:**
    ```text
    >>> Precio final a cobrar: 80.0
    ```
*   **Tu Evidencia (¿Pasó?):** [  ] Sí / [  ] No

---

#### **Caso de Prueba 2: Sin Descuento (0%)**
*   **Propósito:** Probar que el precio original no varía si el descuento es cero.
*   **Entradas:**
    *   Precio original: `100`
    *   Porcentaje de descuento: `0`
*   **Comportamiento Esperado:**
    ```text
    >>> Precio final a cobrar: 100.0
    ```
*   **Tu Evidencia (¿Pasó?):** [  ] Sí / [  ] No

---

#### **Caso de Prueba 3: Límite de Descuento Negativo (Error)**
*   **Propósito:** Validar que el sistema rechace descuentos menores a 0%.
*   **Entradas:**
    *   Precio original: `100`
    *   Porcentaje de descuento: `-5`
*   **Comportamiento Esperado (Mensaje de Error):**
    ```text
    >>> [ERROR]: El descuento debe estar entre 0 y 100
    ```
*   **Tu Evidencia (¿Pasó?):** [  ] Sí / [  ] No

---

#### **Caso de Prueba 4: Límite de Descuento Excesivo (Error)**
*   **Propósito:** Validar que el sistema rechace descuentos mayores a 100%.
*   **Entradas:**
    *   Precio original: `100`
    *   Porcentaje de descuento: `105`
*   **Comportamiento Esperado (Mensaje de Error):**
    ```text
    >>> [ERROR]: El descuento debe estar entre 0 y 100
    ```
*   **Tu Evidencia (¿Pasó?):** [  ] Sí / [  ] No

---

#### **Caso de Prueba 5: Precio Original Inválido (Error)**
*   **Propósito:** Validar que el precio de entrada deba ser positivo (mayor que 0).
*   **Entradas:**
    *   Precio original: `0` (o `-25`)
    *   Porcentaje de descuento: `10`
*   **Comportamiento Esperado (Mensaje de Error):**
    ```text
    >>> [ERROR]: El precio original debe ser positivo
    ```
*   **Tu Evidencia (¿Pasó?):** [  ] Sí / [  ] No

---

#### **Caso de Prueba 6: Redondeo a 2 Decimales**
*   **Propósito:** Validar que el resultado final se limite estrictamente a 2 decimales.
*   **Entradas:**
    *   Precio original: `50.55`
    *   Porcentaje de descuento: `15`
*   **Comportamiento Esperado:**
    *   Cálculo: `50.55 * (1 - 0.15) = 42.9675` -> Redondeado a 2 decimales.
    ```text
    >>> Precio final a cobrar: 42.97
    ```
*   **Tu Evidencia (¿Pasó?):** [  ] Sí / [  ] No

---

#### **Caso de Prueba 7: Promoción Especial de Descuento Alto (Descuento >= 80%)**
*   **Propósito:** Validar el descuento acumulado del 5% adicional para descuentos >= 80%.
*   **Entradas:**
    *   Precio original: `1000`
    *   Porcentaje de descuento: `80`
*   **Comportamiento Esperado:**
    *   Descuento del 80%: `$1000 -> $200`.
    *   Descuento adicional del 5% sobre los $200: `$200 * 0.95 = $190.0`.
    ```text
    >>> Precio final a cobrar: 190.0
    ```
*   **Tu Evidencia (¿Pasó?):** [  ] Sí / [  ] No

---

#### **Caso de Prueba 8: Salida del Programa**
*   **Propósito:** Terminar la sesión interactiva correctamente.
*   **Entradas:**
    *   Escribe `salir` en cualquiera de las solicitudes.
*   **Comportamiento Esperado:** El bucle se rompe y el programa finaliza regresando a la consola normal del sistema.
*   **Tu Evidencia (¿Pasó?):** [  ] Sí / [  ] No
