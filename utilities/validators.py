# utilities/validators.py

def is_square(matrix):
    """
    Memeriksa apakah matriks adalah matriks persegi.
    """
    return matrix.rows == matrix.cols

def is_symmetric(matrix):
    """
    Memeriksa apakah matriks adalah matriks simetris.
    """
    if not is_square(matrix):
        return False
    
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            if matrix.data[i][j] != matrix.data[j][i]:
                return False
    return True
