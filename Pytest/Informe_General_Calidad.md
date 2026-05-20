# Informe General de Aseguramiento de Calidad: Calculadora de Descuentos

**Elaborado por:** Equipo de Desarrollo (Desarrollador & Antigravity)  
**Fecha de emision:** 20 de mayo de 2026  
**Repositorio Oficial:** [Jhonmavisoy/Calculadora-Descuento](https://github.com/Jhonmavisoy/Calculadora-Descuento)  

---

## 🌟 1. Introduccion

Este documento es el **Informe General de Calidad** para el proyecto de la Calculadora de Descuentos. Centraliza todas las metodologias de validacion de software utilizadas, desde pruebas manuales y automatizadas hasta analisis de cobertura e integracion continua.

A continuacion, se detallan las secciones de pruebas con sus respectivas explicaciones sencillas y las capturas de pantalla de evidencia.

---

## 🧪 2. Pruebas Automatizadas con Pytest

Pytest es un framework de pruebas moderno que ejecuta examenes sobre el codigo en cuestion de milisegundos.

### Explicacion de los 14 Casos Aprobados:
1. **Operaciones Normales (4 casos):** Calcula sumas y restas de descuento tradicionales y asegura que los centavos se redondeen correctamente a dos decimales.
2. **Limites de Descuento (4 casos):** Valida que la calculadora bloquee descuentos ilogicos (menores a 0% o mayores a 100%).
3. **Limites de Precio (3 casos):** Verifica que no se procesen productos gratis ($0) o con precios negativos.
4. **Super Promocion (3 casos):** Comprueba que si el descuento es de 80% o mas, se le regale automaticamente un 5% de descuento extra sobre lo restante.

### Glosario de Terminos de Consola:
* **`collected 14 items`**: Pytest encontro 14 escenarios de prueba listos.
* **`PASSED` (en verde)**: La prueba paso con éxito; el codigo dio el resultado correcto.
* **`FAILED` (en rojo)**: La prueba fallo; hubo un error de calculo o el sistema se cayo.
* **`14 passed in 0.05s`**: Resumen final de exito en menos de una decima de segundo.

### 📸 Evidencia 1: Primera Prueba Simple
Se ejecuto una prueba basica inicial para comprobar la comunicacion con el modulo de la calculadora.
![Primera Prueba Simple](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779283849804.png)

### 📸 Evidencia 2: Suite Completa de 14 Casos
La ejecucion de los 14 casos de prueba de limites y comportamiento general.
![Suite de 14 Casos](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779283875799.png)

### 📸 Evidencia 3: Depuracion de Errores (Fallo Controlado)
Reporte detallado que ofrece Pytest cuando falla una asercion o tipo de dato.
![Depuracion de Errores](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779284994942.png)

---

## 🎲 4. Pruebas Dinamicas con Faker

Para estresar la calculadora, implementamos **Faker**, una herramienta que genera datos aleatorios realistas en cada ejecucion.

* **¿Que hace?** Genera en cada corrida 50 combinaciones de precios (de 1 a 10,000) y descuentos (de 0 a 100%) dinamicos para confirmar que el sistema nunca de precios negativos, nunca supere el valor original y calcule bien los limites.

### 📸 Evidencia 4: Pruebas con Faker Aprobadas
Ejecucion de la prueba de estres con datos generados por Faker en consola.
![Pruebas con Faker](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779286611022.png)

---

## 📊 5. Reporte de Cobertura de Codigo (Coverage)

La cobertura de codigo mide que tanto de nuestro codigo principal esta siendo vigilado y evaluado por los examenes automatizados.

* **Estado de la cobertura:** Obtuvimos un **36% de cobertura total**. Esto significa que el **100% de la logica de calculo del motor** esta completamente protegida. El 64% restante corresponde a las pantallas y menus interactivos visuales.

### 📸 Evidencia 5: Reporte de Cobertura en Terminal y Archivo Generado
Salida del script `coverage.py` con el resumen del porcentaje de cobertura.
![Reporte de Cobertura](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779286583985.png)

---

## ☁️ 6. Integracion Continua (GitHub Actions)

Configuramos **GitHub Actions** en el archivo `.github/workflows/pytest-ci.yml` para automatizar las pruebas en la nube.

* **Estructura subida:** Ya subimos a GitHub los scripts de prueba, cobertura y la configuracion del flujo de trabajo de integracion continua.
* **Nota:** Queda pendiente la captura general de GitHub Actions para cuando se agreguen los demas tests del proyecto.

### 📸 Evidencia 6: Estructura del Proyecto Subida a GitHub (Carpeta Pytest)
Verificacion de los archivos del proyecto subidos al repositorio en GitHub.
![GitHub Folder Pytest](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779286646289.png)

---

## 💻 7. Pruebas Manuales Interactivas

Ejecutamos el programa interactivo directamente en consola para comprobar la experiencia del usuario real.

* **Flujos validados:** Ingreso de precios y descuentos normales, calculo de la super promocion y captura de errores cuando se ingresan datos invalidos.

### 📸 Evidencia 7: Consola Interactiva de Usuario
Interaccion en vivo en terminal mostrando el comportamiento correcto ante datos correctos y erróneos.
![Pruebas Manuales](/C:/Users/jhonm/.gemini/antigravity/brain/e16d3154-bac8-4d48-994c-0737e264081a/media__1779283895140.png)

---

## 📝 8. ESPACIO RESERVADO: Pruebas Unitarias Clásicas (Unittest)

> [!NOTE]
> *Espacio reservado para agregar la informacion, codigos y explicaciones sobre las pruebas escritas usando la libreria estándar `unittest`.*

**[ESPACIO_RESERVADO_TEXTO_Y_EXPLICACION_UNITTEST]**

### 📸 Evidencia: Pruebas de Unittest
**[INSERTAR_CAPTURA_EVIDENCIA_UNITTEST]**

---

## 🛠️ 9. ESPACIO RESERVADO: Desarrollo Guiado por Pruebas (TDD)

> [!NOTE]
> *Espacio reservado para detallar el ciclo Red-Green-Refactor (Escribir prueba -> Verla fallar -> Hacer que pase -> Limpiar codigo) implementado en el desarrollo de la calculadora.*

**[ESPACIO_RESERVADO_TEXTO_Y_EXPLICACION_TDD]**

### 📸 Evidencia: Pruebas y Ciclos TDD
**[INSERTAR_CAPTURA_EVIDENCIA_TDD]**

---

## ⚡ 10. ESPACIO RESERVADO: Pruebas PyTDD

> [!NOTE]
> *Espacio reservado para detallar la metodologia y ejecucion de pruebas de PyTDD especificas para este proyecto.*

**[ESPACIO_RESERVADO_TEXTO_Y_EXPLICACION_PYTDD]**

### 📸 Evidencia: Ejecucion de PyTDD
**[INSERTAR_CAPTURA_EVIDENCIA_PYTDD]**

---
*Fin del Informe General de Aseguramiento de Calidad.*
