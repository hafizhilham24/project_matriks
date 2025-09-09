# validators/is_symmetric.py

def is_symmetric(matrix):
    """
    Memeriksa apakah sebuah matriks simetris.
    Matriks simetris adalah matriks yang sama dengan transposenya.
    
    Args:
        matrix: Objek Matrix yang akan diperiksa
        
    Returns:
        bool: True jika matriks simetris, False jika tidak
    """
    # 1. Periksa apakah matriks adalah matriks persegi
    if matrix.rows != matrix.cols:
        return False
    
    # 2. Periksa apakah elemen (i, j) sama dengan elemen (j, i)
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            if matrix.data[i][j] != matrix.data[j][i]:
                return False
    
    # 3. Jika semua elemen sesuai, matriks adalah simetris
    return True
