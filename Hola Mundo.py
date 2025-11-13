print("Hola, Cursor")
for i in range(5):
    print(i)
print("Fin del programa")
print ("el archivo esta cerrado")
try:
    with open('archivo.txt', 'r') as archivo:
        contenido = archivo.read()
        print(contenido)
except FileNotFoundError:
    print("El archivo 'archivo.txt' no existe.")
except Exception as e:
    print(f"Error al leer el archivo: {e}")
finally:
    print("Archivo cerrado (o nunca se abrió)")    

# crea una lista con los cuadros en los n primeros numeros naturales
def cuadros (n):
    return [i**2 for i in range(1, n+1)]
print(cuadros(5))

# Nota: Este programa imprime "Hola, Cursor", luego muestra los números del 0 al 4, y finalmente imprime "Fin del programa".