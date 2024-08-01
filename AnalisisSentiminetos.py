from textblob import TextBlob

# Textos de ejemplo
textos = [
    "I absolutely adore this product, it's outstanding.",
    "I don't enjoy this product, it's terrible.",
    "The product is the same as the others."
]

# Procesar y mostrar resultados para cada texto
for texto in textos:
    # Crear un objeto TextBlob
    blob = TextBlob(texto)

    # Obtener la polaridad del sentimiento (-1 a 1)
    polaridad = blob.sentiment.polarity

    # Etiquetar el sentimiento
    if polaridad > 0:
        etiqueta = "positivo"
    elif polaridad < 0:
        etiqueta = "negativo"
    else:
        etiqueta = "neutral"

    # Imprimir los resultados
    print("Texto:", texto)
    print("Polaridad del sentimiento:", polaridad)
    print("Etiqueta del sentimiento:", etiqueta)
