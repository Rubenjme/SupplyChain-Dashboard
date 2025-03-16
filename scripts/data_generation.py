import os
from datetime import datetime, timedelta
import random
import pandas as pd
import numpy as np

script_dir = os.path.dirname(__file__)            # Carpeta base del script
data_dir = os.path.join(script_dir, '..', 'data') # Ruta a la carpeta "data" (subiendo un nivel y luego /data)
os.makedirs(data_dir, exist_ok=True)              # Me aseguro de que la carpeta existe

num_registros = 10000 # Número de registros a generar

# Función para generar fechas aleatorias entre 2 fechas dadas
def random_date(start, end):
    delta = end - start
    random_days = random.randrange(delta.days)
    return start + timedelta(days=random_days)

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Genero los datos de forma aleatoria
data = []
for i in range(1, num_registros+1):
    
    order_date = random_date(start_date, end_date)                      # Fecha de pedido
    lead_time = int(np.clip(np.random.normal(8, 7), 3, 30))             #  Distribución normal para el lead time (media=8, std=7), acotado entre 3 y 30
    delivery_date = order_date + timedelta(days=lead_time)
    on_time = np.random.choice(["Sí", "No"], p=[0.8, 0.2])              # OnTimeDelivery con probabilidad 80% "Sí" y 20% "No"
    quality_score = float(np.clip(np.random.normal(4, 2), 1, 5))      # Calidad con distribución normal (media=4, std=2), acotado entre 1 y 5
    cost = float(np.clip(np.random.normal(7500, 5000), 500, 20000))     # Coste con distribución normal (media=7500, std=5000), acotado entre 500 y 20000
    
    data.append({
        "OrderID": i,                                           # ID del pedido
        "SupplierID": f"S{random.randint(1,10)}",               # ID del proveedor
        "PartNumber": f"P{random.randint(100,999)}",            # PartNumber
        "OrderDate": order_date.strftime("%Y-%m-%d"),           # Fecha del pedido (YYYY-MM-DD)
        "DeliveryDate": delivery_date.strftime("%Y-%m-%d"),     # Fecha de entrega (YYYY-MM-DD)
        "OnTimeDelivery": on_time,                              # ¿Entrega a tiempo? (Sí/No)
        "LeadTime": lead_time,                                  # Tiempo de entrega (días)
        "QualityScore": quality_score,                          # Calidad (1 - 5)
        "Cost": cost                                            # Coste del pedido de compra ($)
    })


df = pd.DataFrame(data) # Creo un DataFrame con los datos generados

csv_path = os.path.join(data_dir, 'supply_chain_data.csv')  # Ruta al archivo CSV de datos generados (data/supply_chain_data.csv)
df.to_csv(csv_path, index=False, float_format="%.2f", sep=';', decimal=',')       # Guardo el DataFrame en un archivo CSV
print(f"Datos generados y guardados en {csv_path}")         # Imprimo la ruta del archivo generado como referencia
