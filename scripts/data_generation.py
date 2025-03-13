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


order_date = random_date(start_date, end_date)
print(order_date)
