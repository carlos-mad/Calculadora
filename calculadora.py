#calculadora operaciones basicas
def main():
    seguir = True
    while seguir:
        print("Bienvenido a la calculadora")
        print("Bienvenido a la calculadora")
        print("Seleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Ingrese su opción (1-5): ")
        print("opcion seleccionada:", opcion)
        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        seguir = opcion != "5"

if __name__ == "__main__":
    main()