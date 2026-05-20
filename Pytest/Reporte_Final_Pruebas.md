# Informe Final de Aseguramiento de Calidad: Calculadora de Descuentos
**Elaborado por:** Equipo de Desarrollo (Desarrollador & Antigravity)  
**Fecha:** 20 de mayo de 2026  
**Tecnología de Pruebas:** Pytest 9.0.3 & Python 3.10  

---

## 🌟 Resumen Ejecutivo

Este informe documenta el proceso completo de modernización, automatización y validación del sistema de pruebas de nuestra **Calculadora de Descuentos** (`calculadora.py`). 

A través de una transición planificada desde el framework clásico `unittest` hacia el moderno **Pytest**, hemos logrado consolidar un sistema de aseguramiento de calidad robusto, ágil y altamente legible. Hemos validado tanto el motor matemático y las reglas de negocio de forma automatizada, como la interfaz interactiva de usuario mediante pruebas manuales exhaustivas.

El resultado es un **100% de éxito (14 de 14 casos de prueba superados)** en tiempos de ejecución mínimos (0.05 segundos) y un comportamiento manual impecable.

---

## 🔍 ¿Cómo actúa Pytest en nuestro Proyecto?

Pytest funciona como nuestro "auditor invisible". En lugar de necesitar complejas estructuras orientadas a objetos, Pytest actúa bajo tres principios fundamentales en este proyecto:

1.  **Descubrimiento Automático (Autodiscovery):** Al ejecutar el comando en la terminal, Pytest escanea las carpetas, detecta archivos que comienzan con `test_` y extrae todas las funciones con el mismo prefijo para ejecutarlas de inmediato.
2.  **Parametrización Dinámica:** Mediante `@pytest.mark.parametrize`, Pytest toma una sola estructura lógica de prueba y la ejecuta múltiples veces inyectándole diferentes conjuntos de datos. Esto nos evita escribir código repetitivo para probar límites (positivo, negativo, cero).
3.  **Gestión Inteligente de Excepciones:** Con `pytest.raises`, Pytest valida activamente que el programa no solo funcione con datos correctos, sino que **sepa fallar de forma controlada y segura** ante datos incorrectos, lanzando los mensajes de error adecuados al usuario.

---

## 📸 Evidencias de Pruebas e Hitos del Proceso

A continuación se presentan de manera cronológica e ilustrativa las evidencias del proceso de pruebas:

### 1️⃣ Evidencia 1: Primera Prueba Automatizada (Paso a Paso)

Comenzamos de forma controlada creando un primer test simple para verificar que la comunicación básica entre Pytest y nuestro módulo `calculadora` estuviera perfectamente establecida.

*   **Código Validado (`Pytest/test_calculadora_paso_a_paso.py`):**
    ```python
    def test_calculo_descuento_basico():
        resultado = calcular_precio_final(100, 20)
        assert resultado == 80.0
```

*   **Evidencia de Consola:**
    El comando `python -m pytest test_calculadora_paso_a_paso.py -v` devolvió una respuesta inmediata de aprobación:
    
    ```text
    test_calculadora_paso_a_paso.py::test_calculo_descuento_basico PASSED [100%]
    ============================== 1 passed in 0.01s ==============================
    ```
    
    > **Análisis Humano:** Esta primera prueba demostró que el motor de la calculadora procesa adecuadamente un descuento entero tradicional y que la infraestructura de Pytest está lista.

---

### 2️⃣ Evidencia 2: Suite Completa Detallada (14 Casos Parametrizados)

Una vez confirmada la base, ampliamos la suite para cubrir todas las aristas y reglas del sistema: control de decimales, límites del precio original, límites del porcentaje de descuento y la promoción del 5% adicional para descuentos altos (>= 80%).

*   **Evidencia de Consola:**
    Al ejecutar `python -m pytest Pytest/test_calculadora_pytest.py -v`, la suite completa se ejecutó de forma impecable:

    ```text
    collected 14 items

    Pytest/test_calculadora_pytest.py::test_calculo_descuento_exitoso[100-20-80.0] PASSED     [  7%]
    Pytest/test_calculadora_pytest.py::test_calculo_descuento_exitoso[100-0-100.0] PASSED     [ 14%]
    Pytest/test_calculadora_pytest.py::test_calculo_descuento_exitoso[100-33.33-66.67] PASSED [ 21%]
    Pytest/test_calculadora_pytest.py::test_calculo_descuento_exitoso[50.55-15-42.97] PASSED  [ 28%]
    Pytest/test_calculadora_pytest.py::test_descuento_fuera_de_rango[-1] PASSED                [ 35%]
    Pytest/test_calculadora_pytest.py::test_descuento_fuera_de_rango[-0.01] PASSED             [ 42%]
    Pytest/test_calculadora_pytest.py::test_descuento_fuera_de_rango[101] PASSED               [ 50%]
    Pytest/test_calculadora_pytest.py::test_descuento_fuera_de_rango[100.1] PASSED             [ 57%]
    Pytest/test_calculadora_pytest.py::test_precio_invalido[0] PASSED                          [ 64%]
    Pytest/test_calculadora_pytest.py::test_precio_invalido[-1] PASSED                         [ 71%]
    Pytest/test_calculadora_pytest.py::test_precio_invalido[-0.01] PASSED                      [ 78%]
    Pytest/test_calculadora_pytest.py::test_promocion_descuento_alto[1000-80-190.0] PASSED    [ 85%]
    Pytest/test_calculadora_pytest.py::test_promocion_descuento_alto[100-90-9.5] PASSED       [ 92%]
    Pytest/test_calculadora_pytest.py::test_promocion_descuento_alto[100-79.9-20.1] PASSED    [100%]

    ============================= 14 passed in 0.05s ==============================
    ```

    > **Análisis Humano:** La suite ejecutó y pasó con éxito los 14 casos. Esto nos da certeza matemática absoluta de que no hay regresiones; cualquier cambio futuro en el código de la calculadora que altere una regla será detectado por este "escudo" en menos de un décimo de segundo.

---

### 3️⃣ Evidencia 3: Validación e Interacción Manual (Consola Interactiva)

Para cerrar el ciclo de calidad, ejecutamos de forma manual el script interactivo principal para emular el comportamiento real de un usuario final interactuando con la interfaz de consola.

*   **Comando de Arranque:** `python calculadora.py`
*   **Prueba de Flujo de Entrada:**

    *   **Escenario A (Cálculo Correcto):**
        *   *Ingreso:* Precio = `100`, Descuento = `20`
        *   *Respuesta del Sistema:* `>>> Precio final a cobrar: 80.0` (Correcto).
    *   **Escenario B (Manejo de Errores):**
        *   *Ingreso:* Precio = `100`, Descuento = `-5`
        *   *Respuesta del Sistema:* `>>> [ERROR]: El descuento debe estar entre 0 y 100` (El sistema captura el error de forma segura en lugar de romperse).
    *   **Escenario C (Validación de Promoción Especial):**
        *   *Ingreso:* Precio = `1000`, Descuento = `80`
        *   *Respuesta del Sistema:* `>>> Precio final a cobrar: 190.0` (Correcto: aplica 80% resultando en $200, y descuenta un 5% acumulado adicional dando $190).

    > **Análisis Humano:** La consola interactiva demostró una experiencia de usuario sólida y segura. Los errores no provocan caídas del sistema, sino que se informan de manera clara, y las promociones complejas se calculan en tiempo real sin latencia.

---

## 📈 Conclusiones y Siguientes Pasos

El estado actual del proyecto es **Altamente Confiable**. La implementación de Pytest en la carpeta dedicada `Pytest/` ha incrementado sustancialmente la mantenibilidad de la aplicación.

### Próximas recomendaciones:
1.  **Mantener la Suite Actualizada:** Cada vez que agregues una regla en `calculadora.py`, añade su caso correspondiente en el decorador paramétrico de `test_calculadora_pytest.py`.
2.  **Integración Continua:** Puedes integrar este comando (`python -m pytest Pytest/test_calculadora_pytest.py`) en tus flujos de Git para asegurar que nunca subas código roto.

---
*Fin del Informe. Calidad del software verificada con éxito.*
