# operations/multiply_matrices.py

# 1. IMPOR DIPERBAIKI: Menggunakan impor absolut dari root proyek.
from matriks import Matrix

def multiply_matrices(matrix1, matrix2):
    """
    Melakukan operasi perkalian pada dua objek matriks.
    """
    # LOGIKA KONDISI: Pengecekan ini sudah benar.
    if matrix1.cols != matrix2.rows:
        raise ValueError("Jumlah kolom matriks pertama harus sama dengan jumlah baris matriks kedua untuk perkalian.")

    # LOGIKA INISIALISASI: Pembuatan matriks hasil sudah benar.
    result_data = [[0 for _ in range(matrix2.cols)] for _ in range(matrix1.rows)]

    # LOGIKA PERKALIAN: Algoritma perkalian matriks dengan tiga loop ini sudah benar.
    for i in range(matrix1.rows):
        for j in range(matrix2.cols):
            for k in range(matrix1.cols): # atau bisa juga matrix2.rows
                result_data[i][j] += matrix1.data[i][k] * matrix2.data[k][j]

    # 2. INDENTASI DIPERBAIKI: 'return' harus berada di dalam function.
    return Matrix(result_data)
