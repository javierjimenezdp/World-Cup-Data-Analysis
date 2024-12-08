import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear la carpeta 'resultados' si no existe
if not os.path.exists('resultados'):
    os.makedirs('resultados')

# Ruta de los datos
ruta = "C:/Users/USER/Desktop/AnalisisDatos_UFPS/Archivos/MundialesFutbol.xlsx"
df = pd.read_excel(ruta)

# Graficar el tercer gráfico (por ejemplo, distribución de países anfitriones)
plt.figure(figsize=(10,6))
df['País Anfitrión'].value_counts().plot(kind='bar', color='red')
plt.title("Número de Mundiales por País Anfitrión")
plt.xlabel("País Anfitrión")
plt.ylabel("Número de Mundiales")

# Guardar el gráfico como una imagen en la carpeta 'resultados'
plt.savefig('resultados/visualizacion_3.png')

# Mostrar el gráfico (opcional)
plt.show()
