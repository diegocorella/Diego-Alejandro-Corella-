import pandas as pd
import matplotlib.pyplot as plt
import os

# Obtener la ruta del directorio donde está este script
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "data.csv")

# Leer el CSV con manejo de errores
try:
    data = pd.read_csv(csv_path)
except FileNotFoundError:
    print(f"Error: No se encontró el archivo '{csv_path}'")
    exit(1)
except Exception as e:
    print(f"Error al leer el archivo CSV: {e}")
    exit(1)

# Limpiar nombres de columnas: eliminar espacios en blanco
data.columns = data.columns.str.strip()

# Validar que el DataFrame no esté vacío
if data.empty:
    print("Error: El archivo CSV está vacío")
    exit(1)

# Validar que existan las columnas necesarias
if 'x' not in data.columns or 'y' not in data.columns:
    print(f"Error: El archivo CSV debe contener las columnas 'x' y 'y'")
    print(f"Columnas encontradas: {list(data.columns)}")
    exit(1)

# Limpiar datos: eliminar filas con valores NaN (líneas en blanco)
data = data.dropna()

# Convertir columnas a numérico (por si vienen como texto)
data['x'] = pd.to_numeric(data['x'], errors='coerce')
data['y'] = pd.to_numeric(data['y'], errors='coerce')

# Eliminar filas que no pudieron convertirse a numérico o tienen NaN
data = data.dropna()

# Validar que después de limpiar aún haya datos
if data.empty:
    print("Error: No hay datos numéricos válidos en el archivo CSV")
    exit(1)

# Calcular estadísticas
media_x = data['x'].mean()
media_y = data['y'].mean()
mediana_x = data['x'].median()
mediana_y = data['y'].median()
std_x = data['x'].std()
std_y = data['y'].std()

# Imprimir resultados
print("Estadísticas de la columna X:")
print(f"Media: {media_x}")
print(f"Mediana: {mediana_x}")
print(f"Desviación estándar: {std_x}")

print("\nEstadísticas de la columna Y:")
print(f"Media: {media_y}")
print(f"Mediana: {mediana_y}")
print(f"Desviación estándar: {std_y}")

# Gráfica de dispersión
plt.scatter(data['x'], data['y'])
plt.title("Scatter Plot de X vs Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()

