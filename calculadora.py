def calcular_precio_final(precio_original, descuento):
    if not (0 <= descuento <= 100):
        raise ValueError("El descuento debe estar entre 0 y 100")
    if precio_original <= 0:
        raise ValueError("El precio original debe ser positivo")
        
    precio_final = precio_original * (1 - descuento / 100)
    
    if descuento >= 80:
        precio_final = precio_final * (1 - 0.05)
        
    return round(precio_final, 2)

if __name__ == "__main__":
    print("=========================================")
    print("  Calculadora de Descuentos Interactiva  ")
    print("=========================================")
    print("Escribe 'salir' en cualquier momento para terminar.\n")
    
    while True:
        try:
            precio_input = input("Ingresa el precio original: ")
            if precio_input.lower() == 'salir':
                break
            precio = float(precio_input)
            
            descuento_input = input("Ingresa el porcentaje de descuento: ")
            if descuento_input.lower() == 'salir':
                break
            descuento = float(descuento_input)
            
            resultado = calcular_precio_final(precio, descuento)
            print(f">>> Precio final a cobrar: {resultado}\n")
            
        except ValueError as e:
            print(f">>> [ERROR]: {e}\n")
