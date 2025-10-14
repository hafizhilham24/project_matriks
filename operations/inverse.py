# operations/inverse.py

from matriks import Matrix

def inverse_matrix(matrix):
    """
    Menghitung invers dari matriks 2x2 yang diberikan.
    """
    if matrix.rows != matrix.cols:
        raise ValueError("Hanya matriks persegi yang bisa diinvers.")
    
    if matrix.rows != 2:
        raise NotImplementedError("Fungsi invers saat ini hanya mendukung matriks 2x2.")

    a = matrix.data[0][0]
    b = matrix.data[0][1]
    c = matrix.data[1][0]
    d = matrix.data[1][1]

    determinant = a * d - b * c
    if determinant == 0:
        raise ValueError("Matriks ini tidak memiliki invers (determinan adalah 0).")

    inv_det = 1 / determinant
    inverse_data = [
        [d * inv_det, -b * inv_det],
        [-c * inv_det, a * inv_det]
    ]

    return Matrix(inverse_data)
