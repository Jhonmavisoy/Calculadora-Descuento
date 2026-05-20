import unittest
import io
import os
import sys
from datetime import datetime
from fpdf import FPDF

def generar_pdf(total_run, successes, failures, errors, details):
    pdf = FPDF()
    pdf.add_page()
    
    # Título
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Reporte de Pruebas Automaticas (TDD)", ln=1, align='C')
    
    # Fecha
    pdf.set_font("Arial", 'I', 10)
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    pdf.cell(200, 10, f"Fecha de generacion: {fecha_actual}", ln=1, align='C')
    pdf.ln(10)
    
    # Resumen
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, "Resumen de Ejecucion:", ln=1)
    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, f"Total de Pruebas Ejecutadas: {total_run}", ln=1)
    pdf.cell(200, 10, f"Pruebas Exitosas: {successes}", ln=1)
    pdf.cell(200, 10, f"Pruebas Fallidas: {failures}", ln=1)
    pdf.cell(200, 10, f"Errores en Pruebas: {errors}", ln=1)
    
    pdf.ln(10)
    
    # Estado General
    pdf.set_font("Arial", 'B', 14)
    if failures == 0 and errors == 0:
        pdf.set_text_color(0, 128, 0)
        pdf.cell(200, 10, "ESTADO GENERAL: TODO FUNCIONA CORRECTAMENTE [ OK ]", ln=1)
    else:
        pdf.set_text_color(255, 0, 0)
        pdf.cell(200, 10, "ESTADO GENERAL: SE ENCONTRARON ERRORES [ FAIL ]", ln=1)
    
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    
    # Detalle de errores
    if details:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(200, 10, "Detalle de Errores y Fallos (Evidencia):", ln=1)
        pdf.set_font("Arial", '', 10)
        
        for idx, det in enumerate(details, 1):
            try:
                texto = det.encode('latin-1', 'replace').decode('latin-1')
            except:
                texto = det
            pdf.multi_cell(0, 6, f"{idx}. {texto}")
            pdf.ln(4)
            
    # Guardar PDF
    output_path = os.path.join(os.path.dirname(__file__), "Reporte_TDD_Automatico.pdf")
    pdf.output(output_path)
    return output_path

if __name__ == "__main__":
    print("=========================================")
    print("   GENERADOR DE REPORTE TDD (PDF)        ")
    print("=========================================")
    
    # 1. Buscamos y ejecutamos todos los archivos test_*.py en la carpeta del script
    test_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(test_dir)
    
    if test_dir not in sys.path:
        sys.path.insert(0, test_dir)
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
        
    loader = unittest.TestLoader()
    suite = loader.discover(test_dir, pattern='test_r*.py')
    
    stream = io.StringIO()
    runner = unittest.TextTestRunner(stream=stream, verbosity=2)
    result = runner.run(suite)
    
    # 2. Cálculos para el reporte
    total_failures = len(result.failures)
    total_errors = len(result.errors)
    total_successes = result.testsRun - total_failures - total_errors
    
    print(f"\n> Se ejecutaron {result.testsRun} pruebas en total.")
    
    details = []
    
    if result.wasSuccessful():
        print("\n[ OK ] ESTADO: TODO FUNCIONA CORRECTAMENTE. (0 errores)")
    else:
        total_issues = total_failures + total_errors
        print(f"\n[FAIL] ESTADO: SE ENCONTRARON {total_issues} ERRORES.")
        print("\n--- LISTA DE ERRORES ACTUALIZADOS ---")
        
        for i, (test, trace) in enumerate(result.failures + result.errors, 1):
            test_name = test.id().split('.')[-1]
            lineas = trace.strip().split('\n')
            mensaje_error = lineas[-1] if lineas else "Error desconocido"
            
            error_texto = f"Prueba: {test_name}\nDetalle: {mensaje_error}"
            details.append(error_texto)
            print(f"\n{i}. Falló el requerimiento en: {test_name}")
            print(f"   -> {mensaje_error}")
            
    print("\nGenerando reporte PDF...")
    pdf_path = generar_pdf(result.testsRun, total_successes, total_failures, total_errors, details)
    print(f"Reporte generado exitosamente en: {pdf_path}")
    print("\n=========================================")
