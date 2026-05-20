from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import subprocess
import re


# =========================
# EJECUTAR PYTEST LIMPIO
# =========================
def ejecutar_pytest():
    resultado = subprocess.run(
        ["python", "-m", "pytest", "-q"],
        capture_output=True,
        text=True
    )

    salida = resultado.stdout + "\n" + resultado.stderr
    return salida


# =========================
# EXTRAER ESTADÍSTICAS REALES
# =========================
def extraer_stats(texto):
    # ejemplo: "8 passed, 4 failed"
    passed = 0
    failed = 0

    match_passed = re.search(r"(\d+)\s+passed", texto)
    match_failed = re.search(r"(\d+)\s+failed", texto)

    if match_passed:
        passed = int(match_passed.group(1))

    if match_failed:
        failed = int(match_failed.group(1))

    total = passed + failed
    porcentaje = (passed / total * 100) if total > 0 else 0

    return passed, failed, total, porcentaje


# =========================
# CREAR PDF PROFESIONAL
# =========================
def generar_pdf(texto, stats):
    passed, failed, total, porcentaje = stats

    archivo = "REPORTE_TDD_FINAL.pdf"
    c = canvas.Canvas(archivo, pagesize=letter)
    width, height = letter

    # ================= PORTADA =================
    c.setFont("Helvetica-Bold", 20)
    c.drawString(120, height - 80, "REPORTE DE PRUEBAS TDD")

    c.setFont("Helvetica", 12)
    c.drawString(120, height - 110, f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    c.setFont("Helvetica", 11)
    c.drawString(120, height - 140, "Proyecto: Calculadora de Descuentos")

    c.setFont("Helvetica-Bold", 12)
    c.drawString(450, height - 80, "QA REPORT")

    c.showPage()

    # ================= RESUMEN =================
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 60, "RESUMEN DE RESULTADOS")

    c.setFont("Helvetica", 12)
    c.drawString(50, height - 100, f"Total pruebas: {total}")
    c.drawString(50, height - 120, f"Aprobadas: {passed}")
    c.drawString(50, height - 140, f"Fallidas: {failed}")
    c.drawString(50, height - 160, f"Porcentaje éxito: {porcentaje:.2f}%")

    estado = "EXCELENTE" if porcentaje >= 90 else "ACEPTABLE" if porcentaje >= 70 else "CRÍTICO"
    c.drawString(50, height - 190, f"Estado del sistema: {estado}")

    c.showPage()

    # ================= DETALLE =================
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 50, "DETALLE DE PYTEST")

    c.setFont("Courier", 8)

    y = height - 80
    for linea in texto.split("\n"):
        if y < 40:
            c.showPage()
            y = height - 50
            c.setFont("Courier", 8)

        c.drawString(40, y, linea[:120])
        y -= 10

    c.save()
    print("✅ PDF generado correctamente: REPORTE_TDD_FINAL.pdf")


# =========================
# MAIN
# =========================
if __name__ == "__main__":
    print("Ejecutando pruebas TDD...")

    salida = ejecutar_pytest()
    stats = extraer_stats(salida)

    print("Generando PDF profesional...")
    generar_pdf(salida, stats)