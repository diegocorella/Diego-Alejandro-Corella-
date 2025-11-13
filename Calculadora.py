def pedir_operacion():
    print("\nOperaciones disponibles: suma, resta, multiplicacion, division")
    print("Tambien puedes usar +, -, *, /")
    op = input("Escribe la operacion (o 'salir' para terminar): ").strip().lower()
    return op

def pedir_numero(etiqueta):
    while True:
        dato = input(f"Ingresa {etiqueta}: ").strip().replace(",", ".")
        try:
            return float(dato)
        except ValueError:
            print("Eso no parece numero. Intenta de nuevo.")

def main():
    operaciones = {
        "suma": lambda a, b: a + b,
        "+": lambda a, b: a + b,
        "resta": lambda a, b: a - b,
        "-": lambda a, b: a - b,
        "multiplicacion": lambda a, b: a * b,
        "*": lambda a, b: a * b,
        "division": lambda a, b: a / b,
        "/": lambda a, b: a / b,
    }

    print("===Calculadora simple===")
    while True:
        op = pedir_operacion()
        if op == "salir":
            print("Hasta luego!")
            break

        if op not in operaciones:
            print("Operacion no valida. Intenta otra vez.")
            continue

        a = pedir_numero("el primer numero")
        b = pedir_numero("el segundo numero")

        try:
            resultado = operaciones[op](a, b)
            print(f"Resultado: {resultado}")
        except ZeroDivisionError:
            print("No se puede dividir entre cero.")

if __name__ == "__main__":
    main()

