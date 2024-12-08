import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear la carpeta 'resultados' si no existe
if not os.path.exists('resultados'):
    os.makedirs('resultados')

# Ruta de los datos
ruta = "C:/Users/USER/Desktop/AnalisisDatos_UFPS/Archivos/MundialesFutbol.xlsx"
df = pd.read_excel(ruta)

# Graficar el primer gráfico
plt.figure(figsize=(10,6))
plt.hist(df['Año'], bins=20, color='blue', edgecolor='black')
plt.title("Distribución de Años de los Mundiales de Fútbol")
plt.xlabel("Año")
plt.ylabel("Frecuencia")

# Guardar el gráfico como una imagen en la carpeta 'resultados'
plt.savefig('resultados/visualizacion_1.png')

# Mostrar el gráfico (opcional)
plt.show()
