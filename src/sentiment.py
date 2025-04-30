from transformers import pipeline

# Cargamos un pipeline preentrenado para análisis de sentimientos
# Vamos a usar un modelo multilingüe para que entienda español

modelo_sentimiento = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

def analizar_sentimiento(texto):
    """
    Función que analiza el sentimiento de un texto.
    Retorna 'positivo', 'negativo' o 'neutro'.
    """
    resultado = modelo_sentimiento(texto)
    etiqueta = resultado[0]['label']
    
    # Interpretar etiquetas del modelo:
    if etiqueta in ['4 stars', '5 stars']:
        return 'positivo'
    elif etiqueta in ['1 star', '2 stars']:
        return 'negativo'
    else:
        return 'neutro'

# Ejemplo rápido
if __name__ == "__main__":
    ejemplo = "La calidad de la pantalla no es la mejor, esperaba más."
    print("Texto:", ejemplo)
    print("Sentimiento:", analizar_sentimiento(ejemplo))
