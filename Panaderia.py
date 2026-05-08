import random
import statistics

dias = 30
pieza_docena = 420
pieza_liquidacion = 216

docenas_lista = list(range(2,10))
random.shuffle(docenas_lista)

for docenas in docenas_lista:
    ganancia_del_mes = []

    for _ in range(dias):
        pedidos = random.uniform(3,7)
        venta = min(docenas, pedidos)

        ganancias_i = venta * pieza_docena
        sobrante = docenas - venta

        liquidacion_venta = sobrante * 0.70
        ganancia_dia = ganancias_i + liquidacion_venta * pieza_liquidacion

        ganancia_del_mes.append(ganancia_dia)

    promedio = sum(ganancia_del_mes) / dias
    desvi = statistics.stdev(ganancia_del_mes)

  print(f"\nproduccion: {docenas} docenas")
    print(f"promedio: ${promedio:.2f}")
    print(f"desviacion_estandar: ${desvi:.2f}")

