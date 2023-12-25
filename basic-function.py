a = [3,4,5]
b = [6,5,4]
c = [[3,4,5],[6,5,4]]

def normalize_vector(vector_or_matrix):
    def normalize_single_vector(vector):
        norm = sum(x**2 for x in vector) ** 0.5
        if norm == 0:
            raise ValueError("Zero vectors cannot be normalized")
        return [x / norm for x in vector]

    if all(isinstance(elem, list) for elem in vector_or_matrix):
        return [normalize_single_vector(vector) for vector in vector_or_matrix]
    else:
        return normalize_single_vector(vector_or_matrix)

normalized_single_vector = normalize_vector(c)
print(normalized_single_vector)


def dot_product(vector_or_matrix1, vector_or_matrix2):
    def dot_single_vectors(v1, v2):
        if len(v1) != len(v2):
            raise ValueError("The vectors have different sizes.")
        return sum(x * y for x, y in zip(v1, v2))

    if (all(isinstance(elem, list) for elem in vector_or_matrix1) and
            all(isinstance(elem, list) for elem in vector_or_matrix2)):
        if len(vector_or_matrix1) != len(vector_or_matrix2):
            raise ValueError("The matrix sizes are different.")
        return [dot_single_vectors(v1, v2) for v1, v2 in zip(vector_or_matrix1, vector_or_matrix2)]
    else:
        return dot_single_vectors(vector_or_matrix1, vector_or_matrix2)


dot_product_matrix = dot_product(a, b)
print(dot_product_matrix)
