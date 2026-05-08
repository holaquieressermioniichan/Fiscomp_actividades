import random

n_puntos = 10000  # Cuantos más puntos, más precisión
radio = 1
puntos_dentro = 0

# Generamos puntos aleatorios en un cuadrado que va de -1 a 1
# Visualización rápida de la precisión
error = abs(area_aprox - (3.14159 * radio**2))
print(f"Error estimado: {error:.5f}")
"""
import random

n_puntos = 10000  # Cuantos más puntos, más precisión
radio = 1

while
for _ in range(n_puntos):
    # Coordenadas aleatorias entre -1 y 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Ecuación de la circunferencia: x^2 + y^2 <= r^2
    if x**2 + y**2 <= radio**2:
        puntos_dentro += 1

# El área del cuadrado es 2*2 = 4
# El área del círculo aproximada es:
area_aprox = (puntos_dentro / n_puntos) * 4

print(f"\nSimulación de Montecarlo (n={n_puntos} puntos)")
print("-" * 45)
print(f"Puntos que cayeron dentro: {puntos_dentro}")
print(f"Área aproximada calculada: {area_aprox:.5f}")
print(f"Área real (PI * r^2):	   {3.14159 * radio**2:.5f}")
print("-" * 45)

# Visualización rápida de la precisión
error = abs(area_aprox - (3.14159 * radio**2))
print(f"Error estimado: {error:.5f}")
