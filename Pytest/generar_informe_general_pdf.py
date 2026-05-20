import os
import sys
from fpdf import FPDF
from datetime import datetime

class ReportPDF(FPDF):
    def header(self):
        # Encabezado para páginas posteriores a la portada
        if self.page_no() > 1:
            self.set_font("Arial", 'I', 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 10, "Informe General de Aseguramiento de Calidad - Calculadora de Descuentos", 0, 0, 'L')
            self.cell(0, 10, f"UPEC | Computacion | Septimo Nivel", 0, 1, 'R')
            self.set_draw_color(200, 200, 200)
            self.line(10, 20, 200, 20)
            self.ln(5)

    def footer(self):
        # Pie de página para todas las páginas
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.set_text_color(120, 120, 120)
        # Línea divisoria
        self.set_draw_color(220, 220, 220)
        self.line(10, 282, 200, 282)
        # Fecha a la izquierda, página a la derecha
        fecha_actual = datetime.now().strftime("%d/%m/%Y")
        self.cell(0, 10, f"Generado el: {fecha_actual} | QA Audit", 0, 0, 'L')
        self.cell(0, 10, f"Pagina {self.page_no()}", 0, 0, 'R')

def main():
    pdf = ReportPDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    
    # Directorios de imagenes
    img_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "extracted_images"))
    
    # Definición de rutas absolutas de las imágenes en el repositorio
    img_pytest_simple = os.path.join(img_dir, "media__1779283849804.png")
    img_pytest_14 = os.path.join(img_dir, "media__1779283875799.png")
    img_pytest_errors = os.path.join(img_dir, "media__1779284994942.png")
    img_manual = os.path.join(img_dir, "media__1779283895140.png")
    img_coverage = os.path.join(img_dir, "media__1779286583985.png")
    img_faker = os.path.join(img_dir, "media__1779286611022.png")
    img_github = os.path.join(img_dir, "media__1779286646289.png")
    
    img_pytdd_p1 = os.path.join(img_dir, "pytdd_p1_img1.png")
    img_pytdd_p2_a = os.path.join(img_dir, "pytdd_p2_img2.png")
    img_pytdd_p2_b = os.path.join(img_dir, "pytdd_p2_img3.png")
    img_pytdd_p2_c = os.path.join(img_dir, "pytdd_p2_img4.png")
    img_pytdd_p3 = os.path.join(img_dir, "pytdd_p3_img5.png")

    # ================= PAGINA 1: PORTADA =================
    pdf.add_page()
    
    # Decoración visual lateral
    pdf.set_fill_color(31, 78, 121) # Azul Premium
    pdf.rect(0, 0, 10, 297, 'F')
    
    pdf.set_xy(20, 40)
    pdf.set_font("Arial", 'B', 24)
    pdf.set_text_color(31, 78, 121)
    pdf.multi_cell(0, 12, "INFORME GENERAL DE\nASEGURAMIENTO DE CALIDAD")
    
    pdf.ln(5)
    pdf.set_font("Arial", '', 14)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, "Ecosistema Integral de Pruebas y Cobertura de Codigo", 0, 1, 'L')
    pdf.set_draw_color(31, 78, 121)
    pdf.line(20, 75, 120, 75)
    
    pdf.set_xy(20, 95)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(0, 8, "PROYECTO EVALUADO:", 0, 1, 'L')
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 8, "Calculadora de Descuentos Comercial (calculadora.py)", 0, 1, 'L')
    
    pdf.ln(5)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, "METODOLOGIAS APLICADAS:", 0, 1, 'L')
    pdf.set_font("Arial", '', 11)
    pdf.cell(0, 6, "- Pruebas Automatizadas con Pytest (14 casos parametrizados)", 0, 1, 'L')
    pdf.cell(0, 6, "- Pruebas Estructuradas con Unittest (testtools + Faker)", 0, 1, 'L')
    pdf.cell(0, 6, "- Ciclo de Desarrollo Guiado por Pruebas (TDD)", 0, 1, 'L')
    pdf.cell(0, 6, "- Integracion de PyTest y TDD (Suite PyTDD)", 0, 1, 'L')
    pdf.cell(0, 6, "- Analisis de Cobertura de Codigo (Coverage.py)", 0, 1, 'L')
    pdf.cell(0, 6, "- Generacion Masiva de Datos de Estres (Faker)", 0, 1, 'L')
    pdf.cell(0, 6, "- Integracion Continua remota (GitHub Actions CI)", 0, 1, 'L')
    
    pdf.set_xy(20, 210)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, "ELABORADO POR:", 0, 1, 'L')
    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 6, "Jhon Mavisoy, Kevin Anchundia, Milena Narvaez, Alex Moreno", 0, 1, 'L')
    pdf.cell(0, 6, "Equipo de Ingenieria en Computacion - UPEC (Septimo Nivel)", 0, 1, 'L')
    
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, "REPOSITORIO OFICIAL EN GITHUB:", 0, 1, 'L')
    pdf.set_font("Arial", 'I', 11)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 6, "github.com/Jhonmavisoy/Calculadora-Descuento", 0, 1, 'L')

    # ================= PAGINA 2: SECCION 1 =================
    pdf.add_page()
    pdf.set_xy(10, 25)
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "1. Introduccion y Requerimientos de la Calculadora", 0, 1, 'L')
    
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(50, 50, 50)
    intro_txt = (
        "El presente informe recopila las auditorias y ejecuciones de control de calidad sobre la "
        "Calculadora de Descuentos interactiva. Este software calcula el monto neto que debe pagar "
        "un usuario final aplicando porcentajes comerciales y capturando de forma segura cualquier ingreso erroneo.\n\n"
        "La validacion se realizo evaluando las 6 reglas de negocio clave (Requerimientos R1 a R6):"
    )
    pdf.multi_cell(0, 5, intro_txt)
    pdf.ln(3)
    
    reqs = [
        ("R1: Limite de Descuento", "El descuento debe estar estrictamente en el rango de [0, 100]. Valores menores o mayores disparan un error controlado."),
        ("R2: Limite de Precio original", "El precio del producto ingresado debe ser obligatoriamente mayor a $0. No se permiten articulos gratis o negativos."),
        ("R3: Descuento Estandar", "Se resta el porcentaje directo indicado sobre el precio (ej. 20% de descuento a un precio de $100 da $80)."),
        ("R4: Redondeo Preciso", "El precio final obtenido debe redondearse automaticamente a dos decimales exactos para evitar perdidas por centavos."),
        ("R5: Super Promocion Especial", "Si el descuento ingresado es de 80% o mas, se le otorga un 5% de descuento extra sobre el valor restante."),
        ("R6: Soporte Decimal Completo", "El sistema admite decimales tanto en el precio original como en el porcentaje de descuento.")
    ]
    
    for title, desc in reqs:
        pdf.set_font("Arial", 'B', 10)
        pdf.set_text_color(31, 78, 121)
        pdf.cell(50, 5, f"  * {title}: ", 0, 0)
        pdf.set_font("Arial", '', 10)
        pdf.set_text_color(50, 50, 50)
        pdf.multi_cell(0, 5, desc)
        pdf.ln(1)
        
    pdf.ln(4)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 8, "Ecosistema Tecnologico de Calidad Implementado:", 0, 1, 'L')
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(50, 50, 50)
    eco_txt = (
        "Para garantizar la calidad de la logica y el codigo, se estructuraron suites de pruebas unitarias "
        "con Pytest y Unittest, analisis de cobertura (Coverage.py), pruebas dinamicas de estres (Faker), "
        "y se subio el proyecto con pipelines de Integracion Continua (GitHub Actions) en la nube."
    )
    pdf.multi_cell(0, 5, eco_txt)

    # ================= PAGINA 3: SECCION 2 (PYTEST) =================
    pdf.add_page()
    pdf.set_xy(10, 25)
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "2. Pruebas Automatizadas con Pytest", 0, 1, 'L')
    
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(50, 50, 50)
    pytest_txt = (
        "Pytest es un framework moderno de testing en Python que simplifica la escritura de pruebas lógicas. "
        "Se utilizo la decoracion '@pytest.mark.parametrize' en 'test_calculadora_pytest.py' para automatizar "
        "14 casos de prueba distintos de forma simultanea sin repetir lineas de codigo.\n\n"
        "A continuacion se muestran los registros de ejecucion exitosa de las pruebas en consola:"
    )
    pdf.multi_cell(0, 5, pytest_txt)
    pdf.ln(3)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 5, "Evidencia 2.1: Primera corrida basica exitosa de Pytest", 0, 1, 'L')
    if os.path.exists(img_pytest_simple):
        pdf.image(img_pytest_simple, x=15, w=170, h=40)
        pdf.ln(43)
        
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 5, "Evidencia 2.2: Suite completa con los 14 casos parametrizados aprobados", 0, 1, 'L')
    if os.path.exists(img_pytest_14):
        pdf.image(img_pytest_14, x=15, w=170, h=42)
        pdf.ln(45)

    # ================= PAGINA 4: SECCION 2 CONT & SECCION 3 =================
    pdf.add_page()
    pdf.set_xy(10, 25)
    pdf.set_font("Arial", 'B', 10)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 5, "Evidencia 2.3: Visualizacion de Trazas ante Errores Controlados (AssertionError)", 0, 1, 'L')
    if os.path.exists(img_pytest_errors):
        pdf.image(img_pytest_errors, x=15, w=170, h=50)
        pdf.ln(53)
        
    pdf.ln(2)
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "3. Pruebas Estructuradas con Unittest", 0, 1, 'L')
    
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(50, 50, 50)
    unittest_txt = (
        "El modulo nativo Unittest se implemento en 'Unitest/test_calculadora.py' mediante una estructura "
        "de clases que heredan de 'testtools.TestCase' para aprovechar aserciones avanzadas. "
        "La suite profunda inicializa Faker con una semilla estatica (Seed: 42) e implementa bucles con "
        "'self.subTest()' para aislar el analisis de valores frontera (0%, 79%, 80% y 100% de descuento).\n\n"
        "La ejecucion del script de auditoria profunda e integracion de requisitos reporta exito absoluto:"
    )
    pdf.multi_cell(0, 5, unittest_txt)
    pdf.ln(3)
    
    # Caja de texto tipo consola
    pdf.set_fill_color(245, 245, 245)
    pdf.set_draw_color(200, 200, 200)
    pdf.rect(12, pdf.get_y(), 186, 45, 'FD')
    
    pdf.set_xy(15, pdf.get_y() + 2)
    pdf.set_font("Courier", '', 7.5)
    pdf.set_text_color(30, 30, 30)
    consola_unittest = (
        "PS C:\\Antigravity> python Unitest/test_calculadora.py\n"
        "test_analisis_valores_frontera_subtests (__main__.TestCalculadoraDescuentosProfundo) ... ok\n"
        "test_descuento_estandar_exito_masivo (__main__.TestCalculadoraDescuentosProfundo) ... ok\n"
        "test_error_descuento_fuera_de_rango (__main__.TestCalculadoraDescuentosProfundo) ... ok\n"
        "test_error_precio_no_positivo (__main__.TestCalculadoraDescuentosProfundo) ... ok\n"
        "test_super_descuento_con_bono (__main__.TestCalculadoraDescuentosProfundo) ... ok\n"
        "----------------------------------------------------------------------\n"
        "Ran 5 tests in 0.075s\n\n"
        "OK"
    )
    pdf.multi_cell(0, 4, consola_unittest)
    
    pdf.set_xy(10, pdf.get_y() + 8)
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(0, 5, "Adicionalmente, 'Unitest/Verificacion_Requisitos.py' valido de forma exitosa los requisitos individuales (test_r1 a test_r5) generando el reporte de QA 'Reporte_Pruebas.pdf' sin errores.")

    # ================= PAGINA 5: SECCION 4 & SECCION 5 =================
    pdf.add_page()
    pdf.set_xy(10, 25)
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "4. Desarrollo Guiado por Pruebas (TDD)", 0, 1, 'L')
    
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(50, 50, 50)
    tdd_txt = (
        "El ciclo TDD (Test Driven Development) consiste en guiar el desarrollo escribiendo primero los examenes. "
        "En 'Pruebas_tdd/test_calculadora_tdd.py' se trabajo bajo este flujo. Se creo el script 'reporte_TDD_pdf.py' "
        "para ejecutar de forma silenciosa la suite y compilar en caliente 'REPORTE_TDD_FINAL.pdf'.\n\n"
        "El script lee el resultado de Pytest y genera una portada profesional, un resumen de metricas y el "
        "estado general de salud del software."
    )
    pdf.multi_cell(0, 5, tdd_txt)
    pdf.ln(4)
    
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "5. Integracion PyTDD (PyTest & TDD)", 0, 1, 'L')
    
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(50, 50, 50)
    pytdd_txt = (
        "En la suite 'PyTDD/' se valido la integracion directa de PyTest bajo la filosofia TDD mediante "
        "el modulo 'test_demo_tdd.py'. A continuacion se detallan las evidencias visuales extraidas "
        "del reporte de implementacion, mostrando la estructura del proyecto y los resultados obtenidos:"
    )
    pdf.multi_cell(0, 5, pytdd_txt)
    pdf.ln(3)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 5, "Evidencia 5.1: Estructura del subproyecto PyTDD subido", 0, 1, 'L')
    if os.path.exists(img_pytdd_p1):
        pdf.image(img_pytdd_p1, x=15, w=170, h=40)
        pdf.ln(43)

    # ================= PAGINA 6: SECCION 5 CONT =================
    pdf.add_page()
    pdf.set_xy(10, 25)
    pdf.set_font("Arial", 'B', 10)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 5, "Evidencia 5.2: Corrida automatica de Pytest buscando modulos en PyTDD", 0, 1, 'L')
    if os.path.exists(img_pytdd_p2_a):
        pdf.image(img_pytdd_p2_a, x=15, w=170, h=40)
        pdf.ln(43)
        
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 5, "Evidencia 5.3: Detalle de error logico forzado (AssertionError) capturado por PyTest", 0, 1, 'L')
    if os.path.exists(img_pytdd_p2_b):
        pdf.image(img_pytdd_p2_b, x=15, w=170, h=40)
        pdf.ln(43)
        
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 5, "Evidencia 5.4: Detalle de error de tipo de entrada (TypeError) bloqueado por Pytest", 0, 1, 'L')
    if os.path.exists(img_pytdd_p2_c):
        pdf.image(img_pytdd_p2_c, x=15, w=170, h=40)
        pdf.ln(43)
        
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 5, "Evidencia 5.5: Pantalla de resumen final de la practica de PyTDD", 0, 1, 'L')
    if os.path.exists(img_pytdd_p3):
        pdf.image(img_pytdd_p3, x=15, w=170, h=40)
        pdf.ln(43)

    # ================= PAGINA 7: SECCION 6 & SECCION 7 =================
    pdf.add_page()
    pdf.set_xy(10, 25)
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "6. Medicion de Cobertura (Coverage)", 0, 1, 'L')
    
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(50, 50, 50)
    cov_txt = (
        "La cobertura mide el porcentaje de lineas de codigo que han sido ejecutadas por la suite de pruebas. "
        "Se ejecuto el script 'Pytest/coverage.py' para compilar el reporte en consola y en HTML. "
        "El 36% obtenido representa el 100% de la logica comercial y aritmetica de la calculadora, "
        "mientras que el porcentaje restante corresponde unicamente al menu interactivo manual de consola."
    )
    pdf.multi_cell(0, 5, cov_txt)
    pdf.ln(2)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 5, "Evidencia 6.1: Corrida de Cobertura y reporte en terminal", 0, 1, 'L')
    if os.path.exists(img_coverage):
        pdf.image(img_coverage, x=15, w=170, h=55)
        pdf.ln(58)
        
    pdf.ln(2)
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "7. Generacion de Datos de Prueba (Faker)", 0, 1, 'L')
    
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(50, 50, 50)
    faker_txt = (
        "Para evitar la monotonía de datos escritos a mano, se implemento 'Faker' en 'Pytest/test_faker.py'. "
        "Faker simula 50 combinaciones de compras reales y validas en cada ejecucion, inyectando precios "
        "flotantes aleatorios y porcentajes al azar. Sirve como prueba de estres para asegurar estabilidad matematica."
    )
    pdf.multi_cell(0, 5, faker_txt)
    pdf.ln(2)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 5, "Evidencia 7.1: Ejecucion de pruebas estresadas mediante Faker en consola", 0, 1, 'L')
    if os.path.exists(img_faker):
        pdf.image(img_faker, x=15, w=170, h=30)
        pdf.ln(33)

    # ================= PAGINA 8: SECCION 8, SECCION 9 & CONCLUSIONES =================
    pdf.add_page()
    pdf.set_xy(10, 25)
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "8. Control de Versiones e Integracion Continua (GitHub)", 0, 1, 'L')
    
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(50, 50, 50)
    git_txt = (
        "El proyecto completo fue subido a GitHub bajo el repositorio 'Calculadora-Descuento'. "
        "Se configuro GitHub Actions ('.github/workflows/pytest-ci.yml') para levantar servidores virtuales "
        "con Linux, instalar las dependencias y correr toda la suite de pruebas unitarias con cada push, "
        "garantizando que el codigo no sufra regresiones logicas."
    )
    pdf.multi_cell(0, 5, git_txt)
    pdf.ln(2)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 5, "Evidencia 8.1: Estructura del proyecto sincronizado en GitHub", 0, 1, 'L')
    if os.path.exists(img_github):
        pdf.image(img_github, x=15, w=170, h=40)
        pdf.ln(43)
        
    pdf.ln(2)
    pdf.set_font("Arial", 'B', 14)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "9. Conclusiones Generales", 0, 1, 'L')
    
    pdf.set_font("Arial", '', 10)
    pdf.set_text_color(50, 50, 50)
    conclusiones = (
        "1. Calidad y Robustez: La Calculadora de Descuentos cuenta con un motor matematico solido "
        "capaz de manejar redondeos precisos y bloquear valores invalidos en base a sus 6 requerimientos.\n"
        "2. Multimetodologia de Pruebas: La suite cubre testing con frameworks modernos (Pytest), tradicionales "
        "(Unittest), de estres masivo (Faker), desarrollo guiado por pruebas (TDD) e integraciones directas (PyTDD).\n"
        "3. Automatizacion de Calidad: La medicion de cobertura y la configuracion de pipelines remotos en "
        "GitHub Actions aseguran que la salud del codigo se mantenga estable a lo largo de futuras actualizaciones."
    )
    pdf.multi_cell(0, 5, conclusiones)
    
    # Guardar PDF
    out_pdf_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "Informe_General_Calidad.pdf"))
    pdf.output(out_pdf_path)
    print(f"✅ PDF generado exitosamente en: {out_pdf_path}")

if __name__ == "__main__":
    main()
