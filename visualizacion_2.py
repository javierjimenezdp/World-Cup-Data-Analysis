import pandas as pd
import matplotlib.pyplot as plt
import os

# Crear la carpeta 'resultados' si no existe
if not os.path.exists('resultados'):
    os.makedirs('resultados')

# Ruta de los datos
ruta = "C:/Users/USER/Desktop/AnalisisDatos_UFPS/Archivos/MundialesFutbol.xlsx"
df = pd.read_excel(ruta)

# Graficar el segundo gráfico (por ejemplo, la cantidad de mundiales ganados por cada país)
plt.figure(figsize=(10,6))
df['País Campeón'].value_counts().plot(kind='bar', color='green')
plt.title("Número de Mundiales Ganados por País")
plt.xlabel("País")
plt.ylabel("Número de Mundiales Ganados")

# Guardar el gráfico como una imagen en la carpeta 'resultados'
plt.savefig('resultados/visualizacion_2.png')

# Mostrar el gráfico (opcional)
plt.show()