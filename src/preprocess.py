import re
import string
import nltk
from nltk.corpus import stopwords

# Descargar stopwords si es la primera vez que usas nltk
nltk.download('stopwords')

# Lista de palabras vacías en español
stop_words = set(stopwords.words('spanish'))

def limpiar_texto(texto):
    """
    Función para limpiar el texto de una reseña.
    1. Convierte a minúsculas
    2. Elimina signos de puntuación
    3. Elimina palabras vacías
    4. Elimina espacios extra
    """
    
    # Convertir a minúsculas
    texto = texto.lower()
    
    # Eliminar signos de puntuación
    texto = texto.translate(str.maketrans('', '', string.punctuation))
    
    # Eliminar números
    texto = re.sub(r'\d+', '', texto)

    # Eliminar espacios adicionales
    texto = re.sub(r'\s+', ' ', texto).strip()

    # Eliminar stopwords
    palabras = texto.split()
    palabras_limpias = [palabra for palabra in palabras if palabra not in stop_words]
    
    # Reconstruir el texto
    texto_limpio = ' '.join(palabras_limpias)

    return texto_limpio

# Ejemplo rápido
if __name__ == "__main__":
    ejemplo = "La batería de este teléfono es excelente y dura todo el día!"
    print("Texto original:", ejemplo)
    print("Texto limpio:", limpiar_texto(ejemplo))
