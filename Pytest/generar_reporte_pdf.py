import os
import sys
from fpdf import FPDF
from datetime import datetime

class ReportPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("Arial", 'I', 8)
            self.set_text_color(120, 120, 120)
            self.cell(0, 10, "Informe Avanzado de Aseguramiento de Calidad - Pytest & CI", 0, 0, 'R')
            self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", 'I', 8)
        self.set_text_color(120, 120, 120)
        self.cell(0, 10, f"Pagina {self.page_no()}", 0, 0, 'C')

def crear_pdf():
    pdf = ReportPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    def encode_text(t):
        return t.encode('latin-1', 'replace').decode('latin-1')

    # ---------------------------------------------------------
    # PAGINA 1: PORTADA
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.ln(35)
    
    pdf.set_font("Arial", 'B', 22)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 15, "INFORME AVANZADO DE CALIDAD", ln=1, align='C')
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 12, "Calculadora de Descuentos con Pytest y CI", ln=1, align='C')
    
    pdf.ln(5)
    pdf.set_draw_color(31, 78, 121)
    pdf.set_line_width(1.5)
    pdf.line(30, 85, 180, 85)
    
    pdf.ln(45)
    pdf.set_font("Arial", '', 11.5)
    pdf.set_text_color(60, 60, 60)
    pdf.cell(0, 8, "Tecnologias: Pytest 9.0.3, Faker, Coverage y GitHub Actions", ln=1, align='C')
    pdf.cell(0, 8, f"Fecha: {datetime.now().strftime('%d de mayo de 2026')}", ln=1, align='C')
    pdf.cell(0, 8, "Elaborado por: Equipo de Desarrollo (Desarrollador & Antigravity)", ln=1, align='C')
    
    # ---------------------------------------------------------
    # PAGINA 2: INTRODUCCIÓN Y ¿QUÉ ES PYTEST?
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.set_font("Arial", 'B', 15)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "1. ¿Que es Pytest y por que lo usamos?", ln=1)
    pdf.ln(4)
    
    pdf.set_font("Arial", '', 11)
    pdf.set_text_color(40, 40, 40)
    pytest_intro = (
        "Pytest es una herramienta automatizada que actúa como un supervisor para nuestro código. "
        "En lugar de que tengamos que abrir la calculadora y probar números a mano cada vez que hacemos un cambio, "
        "escribimos pruebas automáticas (tests) y Pytest las ejecuta por nosotros en milisegundos.\n\n"
        "Esto nos garantiza que, si en el futuro modificamos la lógica del negocio, sabremos de inmediato si "
        "rompimos alguna regla matemática sin necesidad de volver a probar todo manualmente."
    )
    pdf.multi_cell(0, 6, encode_text(pytest_intro))
    pdf.ln(6)
    
    pdf.set_font("Arial", 'B', 13)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 8, "Leyendo los resultados de la terminal de forma sencilla:", ln=1)
    pdf.ln(2)
    
    terminal_explicacion = (
        "- 'collected 14 items': Encontró 14 escenarios de prueba listos para ejecutarse.\n"
        "- 'PASSED' (en verde): La prueba se superó exitosamente. El código dio el resultado correcto.\n"
        "- 'FAILED' (en rojo): La prueba falló. Hubo un error de cálculo o el programa se detuvo inesperadamente.\n"
        "- '14 passed in 0.05s': Resumen: todas las 14 pruebas se aprobaron con éxito en 0.05 segundos."
    )
    pdf.set_font("Arial", '', 10.5)
    pdf.multi_cell(0, 5.5, encode_text(terminal_explicacion))
    pdf.ln(6)
    
    pdf.set_font("Arial", 'I', 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, "Evidencia 1: Ejecucion inicial basica en Pytest (1 prueba superada)", ln=1, align='C')
    pdf.ln(2)
    
    img1_path = r"C:\Users\jhonm\.gemini\antigravity\brain\e16d3154-bac8-4d48-994c-0737e264081a\media__1779283849804.png"
    if os.path.exists(img1_path):
        pdf.image(img1_path, x=20, w=170)
        
    # ---------------------------------------------------------
    # PAGINA 3: LAS PRUEBAS AUTOMATIZADAS (14 CASOS)
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.set_font("Arial", 'B', 15)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "2. Explicacion Simple de los 14 Casos del Negocio", ln=1)
    pdf.ln(4)
    
    pdf.set_font("Arial", '', 11)
    pdf.set_text_color(40, 40, 40)
    casos_intro = (
        "Para garantizar la exactitud de la calculadora, diseñamos 14 exámenes automáticos "
        "agrupados en cuatro categorías muy fáciles de entender:"
    )
    pdf.multi_cell(0, 6, encode_text(casos_intro))
    pdf.ln(4)
    
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 6, encode_text("- Operaciones Normales (4 casos):"), ln=1)
    pdf.set_font("Arial", '', 10.5)
    pdf.multi_cell(0, 5.5, encode_text("  Calcula descuentos tradicionales (ej. restar 20% a $100 da $80) y valida que los centavos se redondeen correctamente a dos decimales."))
    pdf.ln(2)
    
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 6, encode_text("- Limites de Descuento (4 casos):"), ln=1)
    pdf.set_font("Arial", '', 10.5)
    pdf.multi_cell(0, 5.5, encode_text("  Evita que se ingresen descuentos ilógicos. Si alguien pone un descuento menor a 0% o mayor a 100%, el sistema lo bloquea automáticamente."))
    pdf.ln(2)
    
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 6, encode_text("- Limites de Precio (3 casos):"), ln=1)
    pdf.set_font("Arial", '', 10.5)
    pdf.multi_cell(0, 5.5, encode_text("  Asegura que no se calculen descuentos para productos gratis ($0) o con precios negativos."))
    pdf.ln(2)
    
    pdf.set_font("Arial", 'B', 11)
    pdf.cell(0, 6, encode_text("- Super Promocion (3 casos):"), ln=1)
    pdf.set_font("Arial", '', 10.5)
    pdf.multi_cell(0, 5.5, encode_text("  Verifica la regla especial: si el descuento es de 80% o más, la calculadora le regala automáticamente al cliente un 5% de descuento extra sobre lo restante."))
    pdf.ln(6)
    
    pdf.set_font("Arial", 'I', 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, "Evidencia 2: Resultado de la suite completa con 14 aprobaciones exitosas", ln=1, align='C')
    pdf.ln(2)
    
    img2_path = r"C:\Users\jhonm\.gemini\antigravity\brain\e16d3154-bac8-4d48-994c-0737e264081a\media__1779283875799.png"
    if os.path.exists(img2_path):
        pdf.image(img2_path, x=20, w=170)

    # ---------------------------------------------------------
    # PAGINA 4: DEPURACIÓN Y ERRORES
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.set_font("Arial", 'B', 15)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "3. ¿Como nos ayuda Pytest cuando algo falla?", ln=1)
    pdf.ln(4)
    
    pdf.set_font("Arial", '', 11)
    pdf.set_text_color(40, 40, 40)
    errores_intro = (
        "El verdadero valor de un sistema de pruebas se demuestra cuando detecta un error. "
        "Forzamos fallos intencionales para evaluar la capacidad de respuesta y depuración de Pytest. "
        "Cuando el sistema detecta que algo anda mal, detiene la prueba y nos muestra un reporte detallado:\n\n"
        "- AssertionError: Ocurre cuando el resultado obtenido no es igual al esperado "
        "(ej. la calculadora arrojó $80 pero le dijimos que debía dar $50).\n"
        "- TypeError: Ocurre si ingresamos un tipo de dato equivocado (ej. intentar calcular "
        "el descuento usando una palabra de texto como 'cien' en lugar del número 100)."
    )
    pdf.multi_cell(0, 6, encode_text(errores_intro))
    pdf.ln(6)
    
    pdf.set_font("Arial", 'I', 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, "Evidencia 3: Detalle de errores y fallos controlados en consola roja de Pytest", ln=1, align='C')
    pdf.ln(2)
    
    img_err_path = r"C:\Users\jhonm\.gemini\antigravity\brain\e16d3154-bac8-4d48-994c-0737e264081a\media__1779284994942.png"
    if os.path.exists(img_err_path):
        pdf.image(img_err_path, x=20, w=170)

    # ---------------------------------------------------------
    # PAGINA 5: COBERTURA Y DATOS DINÁMICOS CON FAKER
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.set_font("Arial", 'B', 15)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "4. Cobertura de Codigo y Datos Dinamicos con Faker", ln=1)
    pdf.ln(4)
    
    pdf.set_font("Arial", '', 11)
    pdf.set_text_color(40, 40, 40)
    cobertura_faker_txt = (
        "Para robustecer aún más el sistema de calidad, implementamos dos mejoras avanzadas:\n\n"
        "1. Reporte de Cobertura Automatica (coverage.py): El script mide qué tanto del motor "
        "de la calculadora está protegido por las pruebas. Los resultados indican un 36% de cobertura total, "
        "lo que representa el 100% de la lógica matemática interna (el resto son menús visuales).\n\n"
        "2. Simulacion Inteligente con Faker (test_faker.py): En lugar de usar números fijos, Faker genera "
        "en cada ejecución 50 combinaciones de precios y descuentos aleatorios realistas para estresar a la "
        "calculadora y asegurar que se comporte de forma estable ante cualquier dato."
    )
    pdf.multi_cell(0, 6, encode_text(cobertura_faker_txt))
    pdf.ln(6)
    
    pdf.set_font("Arial", 'I', 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, "Evidencia 4: Tabla de cobertura e informe de ejecucion de pruebas de estres", ln=1, align='C')
    pdf.ln(2)
    
    img_cov_path = r"C:\Users\jhonm\.gemini\antigravity\brain\e16d3154-bac8-4d48-994c-0737e264081a\media__1779284994945.png"
    if os.path.exists(img_cov_path):
        pdf.image(img_cov_path, x=30, w=150)

    # ---------------------------------------------------------
    # PAGINA 6: INTEGRACIÓN CONTINUA Y PRUEBAS MANUALES
    # ---------------------------------------------------------
    pdf.add_page()
    pdf.set_font("Arial", 'B', 15)
    pdf.set_text_color(31, 78, 121)
    pdf.cell(0, 10, "5. Integracion Continua (CI) y Pruebas Manuales", ln=1)
    pdf.ln(4)
    
    pdf.set_font("Arial", '', 11)
    pdf.set_text_color(40, 40, 40)
    ci_txt = (
        "1. Integracion Continua (CI) con GitHub Actions: Creamos el archivo de configuracion "
        "'.github/workflows/pytest-ci.yml'. Ahora, cada vez que subas cambios a GitHub, un servidor en la "
        "nube instalará automaticamente Pytest, Faker y medirá la cobertura para certificar que tu calculadora "
        "sigue funcionando perfectamente sin errores antes de ser desplegada.\n\n"
        "2. Validacion Manual Interactiva: Comprobamos el correcto funcionamiento de la interfaz de consola "
        "con entradas de datos reales, verificando la captura segura de errores y los cálculos correctos."
    )
    pdf.multi_cell(0, 6, encode_text(ci_txt))
    pdf.ln(6)
    
    pdf.set_font("Arial", 'I', 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 6, "Evidencia 5: Captura del flujo interactivo manual con control seguro de errores", ln=1, align='C')
    pdf.ln(2)
    
    img_man_path = r"C:\Users\jhonm\.gemini\antigravity\brain\e16d3154-bac8-4d48-994c-0737e264081a\media__1779283895140.png"
    if os.path.exists(img_man_path):
        pdf.image(img_man_path, x=45, w=120)

    # Guardar PDF
    out_dir = r"C:\Antigravity\Pytest"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Reporte_Final_Pruebas.pdf")
    pdf.output(out_path)
    print(f"PDF generado con exito en: {out_path}")

if __name__ == "__main__":
    crear_pdf()
