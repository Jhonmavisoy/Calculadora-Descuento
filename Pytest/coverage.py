import subprocess
import sys
import os

def run_coverage():
    print("==================================================")
    print("   EJECUTANDO ANALISIS DE COBERTURA DE CODIGO   ")
    print("==================================================")
    
    # Obtener el directorio de este script (Pytest/)
    pytest_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Comando para ejecutar pytest midiendo la cobertura de calculadora
    cmd = [
        sys.executable, "-m", "pytest",
        os.path.join(pytest_dir, "test_calculadora_pytest.py"),
        "--cov=calculadora",
        "--cov-report=term-missing",
        f"--cov-report=html:{os.path.join(pytest_dir, 'htmlcov')}"
    ]
    
    print(f"Ejecutando comando: {' '.join(cmd)}\n")
    
    # Ejecutar
    result = subprocess.run(cmd)
    
    print("\n==================================================")
    if result.returncode == 0:
        print("[OK] Cobertura medida exitosamente.")
        print(f"Reporte HTML interactivo generado en:\n{os.path.join(pytest_dir, 'htmlcov', 'index.html')}")
    else:
        print("[ERROR] La ejecucion de las pruebas fallo o hubo un error al medir cobertura.")
    print("==================================================")

if __name__ == "__main__":
    run_coverage()
