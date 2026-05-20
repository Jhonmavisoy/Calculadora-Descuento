# Informe General de Aseguramiento de Calidad: Calculadora de Descuentos

**Elaborado por:** Equipo de Desarrollo (Desarrollador & Antigravity)  
**Fecha de emision:** 20 de mayo de 2026  
**Proyecto:** Calculadora de Descuentos con Pruebas Automatizadas  
**Repositorio Oficial:** [Jhonmavisoy/Calculadora-Descuento](https://github.com/Jhonmavisoy/Calculadora-Descuento)  

---

## 📋 1. Introduccion y Requerimientos de la Calculadora

Este proyecto consiste en una **Calculadora de Descuentos** interactiva (`calculadora.py`) programada en Python. Su objetivo es calcular cuanto debe pagar un cliente despues de aplicar un descuento. 

Para asegurar que los calculos sean 100% correctos y que el sistema no se caiga ante errores de los usuarios, se diseñaron pruebas bajo los siguientes requerimientos de negocio:
*   **R1 (Limite de Descuento):** El descuento debe estar estrictamente entre 0% y 100%. Si se ingresa un porcentaje menor a 0 o mayor a 100, la calculadora debe bloquear el calculo.
*   **R2 (Limite de Precio):** El precio original de los productos debe ser mayor a $0. No se permiten precios negativos ni productos gratis ($0).
*   **R3 (Descuento Estandar):** El calculo basico debe restar el porcentaje indicado (ej. un 20% de descuento a un producto de $100 nos da $80).
*   **R4 (Redondeo Preciso):** El precio final cobrado debe redondearse automaticamente a dos decimales (ej. $42.97) para evitar errores con los centavos.
*   **R5 (Super Promocion):** Si se aplica un descuento muy alto (de 80% o mas), el sistema le regala al cliente un **5% de descuento adicional acumulado** sobre lo restante.
*   **R6 (Soporte Decimal):** La calculadora debe permitir decimales tanto en los precios como en los porcentajes de descuento.

### Herramientas utilizadas en el proyecto:
*   **Python:** Lenguaje principal de programacion.
*   **Pytest:** Framework para automatizar y agrupar las pruebas de forma moderna y rapida.
*   **Coverage.py:** Herramienta para medir que tanto codigo esta vigilado por las pruebas.
*   **Faker:** Generador de datos aleatorios para pruebas de estres.
*   **Git & GitHub:** Herramientas para el control de versiones y almacenamiento del codigo en la nube.
*   **GitHub Actions:** Servidor en la nube para ejecutar pruebas de forma automatica (Integracion Continua).

---

## 🧪 2. Pruebas Automatizadas con Pytest

**Pytest** es la herramienta principal que usamos para automatizar los examenes del codigo. En lugar de crear complejas clases orientadas a objetos, nos permite escribir funciones de prueba muy directas y legibles utilizando la palabra clave de Python `assert`.

Diseñamos una suite centralizada (`test_calculadora_pytest.py`) que evalua **14 casos distintos** parametrizados para probar cada limite y regla de negocio en cuestion de milisegundos.

### Explicacion de los resultados de la terminal:
*   **`collected 14 items`**: Pytest leyo los archivos y encontro 14 examenes listos para ejecutarse.
*   **`PASSED` (en verde)**: Significa que la prueba paso con exito y el programa respondio bien.
*   **`FAILED` (en rojo)**: Significa que algo fallo en los calculos o el programa se detuvo abruptamente.
*   **`14 passed in 0.05s`**: Indica que los 14 examenes fueron exitosos en solo 5 centesimas de segundo.

### 📸 Evidencia 2.1: Primera Prueba Basica
Empezamos con una prueba inicial simple para validar que Pytest y la calculadora se comunicaban correctamente.
![Primera Prueba Simple](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779283849804.png)

### 📸 Evidencia 2.2: Suite Completa de 14 Casos Aprobados
Ejecutamos la suite de 14 escenarios que abarcan todas las reglas de redondeo, precios y descuentos invalidos, y la super promocion.
![Suite de 14 Casos](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779283875799.png)

### 📸 Evidencia 2.3: Depuracion ante Fallos (Errores Controlados)
Para demostrar la capacidad de reporte de Pytest, forzamos errores intencionales. Cuando algo falla, Pytest muestra con exactitud que linea causo el problema:
*   `AssertionError`: El resultado matematico no coincide con el esperado.
*   `TypeError`: Se intento usar texto en lugar de numeros.
![Depuracion de Errores](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779284994942.png)

---

## 📝 3. ESPACIO RESERVADO: Pruebas con Unittest

> [!NOTE]
> *Espacio reservado para agregar la informacion, codigos y explicaciones sobre las pruebas escritas usando la libreria estándar `unittest`.*

**[ESPACIO_RESERVADO_TEXTO_Y_EXPLICACION_UNITTEST]**

### 📸 Evidencia: Pruebas de Unittest
**[INSERTAR_CAPTURA_EVIDENCIA_UNITTEST]**

---

## 🛠️ 4. ESPACIO RESERVADO: Desarrollo Guiado por Pruebas (TDD)

> [!NOTE]
> *Espacio reservado para detallar el ciclo Red-Green-Refactor (Escribir prueba -> Verla fallar -> Hacer que pase -> Limpiar codigo) implementado en el desarrollo de la calculadora.*

**[ESPACIO_RESERVADO_TEXTO_Y_EXPLICACION_TDD]**

### 📸 Evidencia: Pruebas y Ciclos TDD
**[INSERTAR_CAPTURA_EVIDENCIA_TDD]**

---

## ⚡ 5. ESPACIO RESERVADO: Pruebas PyTDD

> [!NOTE]
> *Espacio reservado para detallar la metodologia y ejecucion de pruebas de PyTDD especificas para este proyecto.*

**[ESPACIO_RESERVADO_TEXTO_Y_EXPLICACION_PYTDD]**

### 📸 Evidencia: Ejecucion de PyTDD
**[INSERTAR_CAPTURA_EVIDENCIA_PYTDD]**

---

## 📊 6. Medicion de Cobertura (Coverage)

La cobertura nos dice que tanto porcentaje de nuestro archivo principal de codigo (`calculadora.py`) esta protegido y vigilado por las pruebas automatizadas.

Creamos el script `coverage.py` para correr las pruebas y generar un reporte interactivo en HTML que se puede abrir en el navegador.
*   **Porcentaje de cobertura:** El reporte marca un **36%**. Esto representa el **100% del motor matematico** y logica de calculo de la calculadora. El porcentaje restante no cubierto corresponde exclusivamente a la interfaz de terminal interactiva que manejamos a mano.

### 📸 Evidencia 6.1: Reporte de Cobertura en Consola
![Reporte de Cobertura](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779286583985.png)

---

## 🎲 7. Generacion de Datos de Prueba (Faker)

En lugar de usar numeros estaticos escritos a mano, implementamos la libreria **Faker** en el archivo `test_faker.py`.

*   **¿Como funciona?** Faker simula en cada ejecucion **50 casos de compras reales con precios y descuentos aleatorios**.
*   **Objetivo:** Funciona como una prueba de estres. Comprueba que sin importar que numero aleatorio se le inyecte, la calculadora jamas de precios negativos, nunca supere el valor original y capture de forma segura los valores limites.

### 📸 Evidencia 7.1: Ejecucion de Pruebas de Estres con Faker
![Pruebas con Faker](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779286611022.png)

---

## ☁️ 8. Subida a GitHub / Control de Versiones

Para almacenar y versionar el proyecto de forma profesional, inicializamos Git, creamos un archivo `.gitignore` para evitar archivos innecesarios, y lo subimos a GitHub en la ruta oficial.

*   Ademas, implementamos **GitHub Actions** (`pytest-ci.yml`) para Integracion Continua. Cada vez que subas cambios, un servidor web correra tus pruebas de forma automatica para verificar que todo este sano.
*   *Nota: Queda pendiente la captura general de GitHub Actions para cuando se agreguen los demas tests del proyecto.*

### 📸 Evidencia 8.1: Estructura del Proyecto Subida a GitHub (Carpeta Pytest)
![GitHub Folder Pytest](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779286646289.png)

---

## 📈 9. Conclusiones Generales

La implementación de pruebas automatizadas y analisis de calidad en la Calculadora de Descuentos nos permite concluir que:
1.  **Robustez matematica:** La logica de calculo basico, control de decimales y redondeo es 100% segura frente a errores.
2.  **Seguridad y Control:** Las restricciones de precios (R2) y descuentos (R1) funcionan como un escudo, impidiendo que datos incorrectos rompan la aplicacion.
3.  **Mantenibilidad a largo plazo:** El uso de Pytest, Cobertura y GitHub Actions facilita que cualquier desarrollador pueda cambiar o mejorar el programa en el futuro sin temor a dañar lo que ya funciona.
