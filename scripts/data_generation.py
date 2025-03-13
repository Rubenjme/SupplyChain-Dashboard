import os
from datetime import datetime, timedelta
import random
import pandas as pd

script_dir = os.path.dirname(__file__)            # Carpeta base del script
data_dir = os.path.join(script_dir, '..', 'data') # Ruta a la carpeta "data" (subiendo un nivel y luego /data)
os.makedirs(data_dir, exist_ok=True)              # Me aseguro de que la carpeta existe

num_registros = 5000 # Número de registros a generar

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
    order_date = random_date(start_date, end_date)
    lead_time = random.randint(5, 30)
    delivery_date = order_date + timedelta(days=lead_time)
    on_time = random.choice(["Sí", "No"])
    quality_score = round(random.uniform(7.0, 10.0), 1)
    cost = round(random.uniform(1000, 10000), 2)
    data.append({
        "OrderID": i,                                           # ID del pedido
        "SupplierID": f"S{random.randint(1,10)}",               # ID del proveedor
        "PartNumber": f"P{random.randint(100,999)}",            # PartNumber
        "OrderDate": order_date.strftime("%Y-%m-%d"),           # Fecha del pedido (YYYY-MM-DD)
        "DeliveryDate": delivery_date.strftime("%Y-%m-%d"),     # Fecha de entrega (YYYY-MM-DD)
        "OnTimeDelivery": on_time,                              # ¿Entrega a tiempo? (Sí/No)
        "LeadTime": lead_time,                                  # Tiempo de entrega (días)
        "QualityScore": quality_score,                          # Calidad (7.0 - 10.0)
        "Cost": cost                                            # Coste del pedido de compra ($)
    })


df = pd.DataFrame(data) # Creo un DataFrame con los datos generados

csv_path = os.path.join(data_dir, 'supply_chain_data.csv')  # Ruta al archivo CSV de datos generados (data/supply_chain_data.csv)
df.to_csv(csv_path, index=False)                            # Guardo el DataFrame en un archivo CSV
print(f"Datos generados y guardados en {csv_path}")         # Imprimo la ruta del archivo generado como referencia
