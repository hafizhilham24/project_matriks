# operations/transpose.py

# Kita perlu mengimpor kelas Matrix untuk bisa membuat objek Matrix baru
from matriks import Matrix

def transpose_matrix(matrix):
    """
    Menghasilkan matriks baru yang merupakan transpose dari matriks yang diberikan.
    """
    # Membuat kerangka matriks baru dengan dimensi terbalik
    transposed_data = [[0 for _ in range(matrix.rows)] for _ in range(matrix.cols)]

    # Mengisi data ke matriks baru
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            transposed_data[j][i] = matrix.data[i][j]
    
    # Mengembalikan objek Matrix baru
    return Matrix(transposed_data)
