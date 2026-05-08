mport random

# 1. Generar datos usando el módulo 'random' (estándar en Python)
# La función gauss(media, desviación) genera la distribución normal
media = 0
desviacion = 1
n_datos = 2000
datos = [random.gauss(media, desviacion) for _ in range(n_datos)]

# 2. Crear el histograma manualmente
n_barras = 20  # Número de filas en el histograma de texto
min_val = min(datos)
max_val = max(datos)
ancho_rango = (max_val - min_val) / n_barras

# Contar cuántos números caen en cada "barra" (bin)
conteos = [0] * n_barras
for d in datos:
    indice = int((d - min_val) / ancho_rango)
    if indice == n_barras: # Para el valor máximo exacto
        indice -= 1
    conteos[indice] += 1

# 3. Dibujar el histograma en la terminal usando caracteres ASCII
print(f"\nHistograma Gaussiano (n={n_datos})")
print("-" * 50)
max_conteo = max(conteos)
factor_escala = 40 # Ancho máximo de la barra en caracteres

for i in range(n_barras):
    rango_inicio = min_val + i * ancho_rango
    barra = "*" * int((conteos[i] / max_conteo) * factor_escala)
    print(f"{rango_inicio:6.2f} | {barra} ({conteos[i]})")

print("-" * 50)
