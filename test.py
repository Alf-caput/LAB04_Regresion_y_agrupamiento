def hamming_distance(one_hot1, one_hot2):
    """Calcula la distancia de Hamming entre dos vectores one-hot."""
    return sum(v1 != v2 for v1, v2 in zip(one_hot1, one_hot2))

# Ejemplo de uso
vector1 = [0, 1, 0, 0]  # Representa una clase
vector2 = [1, 0, 0, 0]  # Representa otra clase
distance = hamming_distance(vector1, vector2)
print(distance)