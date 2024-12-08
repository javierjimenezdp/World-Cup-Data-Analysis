import pandas as pd

# Cargar los datos
ruta = "C:/Users/USER/Desktop/AnalisisDatos_UFPS/Archivos/MundialesFutbol.xlsx"
df = pd.read_excel(ruta)

# Llamar a cada script para generar los gráficos
# Asegúrate de que los scripts de los gráficos estén en la misma carpeta que este archivo
import visualizacion_1
import visualizacion_2
import visualizacion_3
