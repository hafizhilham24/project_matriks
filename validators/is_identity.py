# validators/is_identity.py

def is_identity(matrix):
    """
    Memeriksa apakah sebuah matriks adalah matriks identitas.
    Matriks identitas adalah matriks persegi dimana semua elemen pada 
    diagonal utama adalah 1 dan elemen lainnya adalah 0.
    
    Args:
        matrix: Objek Matrix yang akan diperiksa
        
    Returns:
        bool: True jika matriks identitas, False jika tidak
    """
    # 1. Periksa apakah matriks adalah matriks persegi
    if matrix.rows != matrix.cols:
        return False
    
    # 2. Periksa elemen-elemen matriks
    for i in range(matrix.rows):
        for j in range(matrix.cols):
            # Periksa elemen diagonal
            if i == j:
                if matrix.data[i][j] != 1:
                    return False
            # Periksa elemen non-diagonal
            else:
                if matrix.data[i][j] != 0:
                    return False
    
    # 3. Jika semua elemen sesuai, matriks adalah identitas
    return True
