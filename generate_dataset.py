import numpy as np
import pandas as pd

np.random.seed(42)
n = 600

distance_km = np.round(np.random.uniform(1.0, 150.0, n), 2)

base_time = 5.0
time_per_km = 0.45
noise = np.random.normal(0, 3, n)
delivery_time_min = np.round(base_time + time_per_km * distance_km + noise, 2)
delivery_time_min = np.maximum(delivery_time_min, 2.0)

df = pd.DataFrame({
    'distance_km': distance_km,
    'delivery_time_min': delivery_time_min
})

df.to_csv('data/delivery_dataset.csv', index=False)
print(f"Dataset generado con {len(df)} registros.")
print(df.head(10))
print(f"\nEstadisticas:\n{df.describe()}")
