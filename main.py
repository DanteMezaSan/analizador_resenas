import pandas as pd
from src.preprocess import limpiar_texto
from src.sentiment import analizar_sentimiento

# Cargar el dataset 
ruta_dataset = "data/dataset_resenas.csv"
df = pd.read_csv(ruta_dataset)

# Mostrar primeras reseñas originales
print("Primeras reseñas originales:\n")
print(df.head(), "\n")

# Crear nuevas columnas para texto limpio y sentimiento detectado
df['resena_limpia'] = df['resena'].apply(limpiar_texto)
df['sentimiento_detectado'] = df['resena_limpia'].apply(analizar_sentimiento)

# Mostrar resultados
print("Primeras reseñas procesadas:\n")
print(df[['resena', 'resena_limpia', 'sentimiento', 'sentimiento_detectado']].head())

# Guardar resultados en un nuevo archivo CSV
df.to_csv("data/dataset_resenas_procesadas.csv", index=False)

print("\nProceso terminado. Resultados guardados en 'data/dataset_resenas_procesadas.csv'.")
