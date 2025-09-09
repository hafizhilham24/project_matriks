# operations/determinant.py
from ..utilities.validators import is_square

def find_determinant(matrix):
    """
    Menghitung determinan dari matriks persegi.
    Hanya untuk matriks 2x2 sebagai contoh sederhana.
    """
    if not is_square(matrix):
        raise ValueError("Determinan hanya bisa dihitung untuk matriks persegi")
    
    if matrix.rows == 1:
        return matrix.data[0][0]
    elif matrix.rows == 2:
        return (matrix.data[0][0] * matrix.data[1][1]) - (matrix.data[0][1] * matrix.data[1][0])
    else:
        raise NotImplementedError("Determinan untuk matriks > 2x2 belum diimplementasikan")
