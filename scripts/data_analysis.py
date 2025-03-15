import os
import pandas as pd

script_dir = os.path.dirname(__file__)                     # Carpeta base del script
data_dir = os.path.join(script_dir, '..', 'data')          # Ruta a la carpeta "data" (subiendo un nivel y luego /data)
csv_path = os.path.join(data_dir, 'supply_chain_data.csv') # Obtengo la ruta del archivo CSV generado por data_generation.py

df = pd.read_csv(csv_path, sep=';', decimal=',', encoding='utf-8') # Leo el CSV

# Cálculo de KPIs
total_orders = len(df)
on_time_orders = len(df[df["OnTimeDelivery"] == "Sí"])
on_time_percentage = (on_time_orders / total_orders) * 100
avg_lead_time = df["LeadTime"].mean()
avg_quality = df["QualityScore"].mean()
avg_cost = df["Cost"].mean()


kpis = { # Diccionario con los KPIs
    "Total Orders": round(total_orders, 2),
    "On Time Delivery (%)": round(on_time_percentage, 2),
    "Average Lead Time (days)": round(avg_lead_time, 2),
    "Average Quality Score": round(avg_quality, 2),
    "Average Cost": round(avg_cost, 2)
}

kpi_df = pd.DataFrame(list(kpis.items()), columns=["KPI", "Value"]) # Creo un DataFrame con los KPIs


kpi_csv_path = os.path.join(data_dir, 'supply_chain_kpis.csv') # Ruta al archivo CSV de KPIs (data/supply_chain_kpis.csv)
kpi_df.to_csv(kpi_csv_path, index=False, decimal=",")          # Guardo el DataFrame en un archivo CSV, se usa la "," como separador decimal
print("Análisis completado. KPIs guardados en:", kpi_csv_path) # Imprimo la ruta del archivo generado como referencia

