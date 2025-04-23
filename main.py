import tensorflow as tf

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

matriz_a = tf.random.uniform(shape = (filas, columnas), minval = 1, maxval = 21, dtype = tf.int32)
matriz_b = tf.random.uniform(shape = (filas, columnas), minval = 1, maxval = 21, dtype = tf.int32)

print("\nMatriz A:")
print(matriz_a.numpy())

print("\nMatriz B:")
print(matriz_b.numpy())

suma = tf.add(matriz_a, matriz_b)
print("\nLa suma de A + B:")
print(suma.numpy())

multiplicacion = tf.multiply(matriz_a, matriz_b)
print("\nMultiplicacion A * B:")
print(multiplicacion.numpy())

