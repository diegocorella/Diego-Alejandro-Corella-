import re
from collections import Counter

archivo = input("Introduce la ruta del archivo de texto: ")
try:
    with open(archivo, "r", encoding="utf-8") as f:
        texto=f.read()
except FileNotFoundError:
    print("El archivo especificado no existe.")
    exit(1)
palabras= re.findall(r"\w+", texto.lower())
total_palabras = len(palabras)
print(f"Total palabras: {total_palabras}")
contador = Counter(palabras)
mas_comunes=contador.most_common(10)
print("Palabras mas frecuentes:")
for palabra, freq in mas_comunes:
    print(f"{palabra}: {freq}")



