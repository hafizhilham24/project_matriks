# operations/inverse.py

from matriks import Matrix
import copy # Kita butuh ini untuk membuat salinan data matriks

def inverse_matrix(matrix):
    """
    Menghitung invers dari matriks persegi berukuran n x n
    menggunakan metode Eliminasi Gauss-Jordan.
    """
    # === LANGKAH 0: VALIDASI ===
    if matrix.rows != matrix.cols:
        raise ValueError("Hanya matriks persegi yang bisa diinvers.")
    
    n = matrix.rows
    
    # === LANGKAH 1: PERSIAPAN ===
    # Buat salinan data matriks agar tidak mengubah objek aslinya
    m_copy = copy.deepcopy(matrix.data)
    
    # Buat matriks identitas dengan ukuran yang sama
    identity = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        identity[i][i] = 1
        
    # === LANGKAH 2: PROSES ELIMINASI GAUSS-JORDAN ===
    
    # --- Bagian 1: Forward Elimination (Membuat matriks segitiga atas) ---
    for i in range(n):
        # Cari pivot (elemen terbesar di kolom) untuk stabilitas numerik
        pivot_row = i
        for j in range(i + 1, n):
            if abs(m_copy[j][i]) > abs(m_copy[pivot_row][i]):
                pivot_row = j
        
        # Tukar baris saat ini dengan baris pivot
        m_copy[i], m_copy[pivot_row] = m_copy[pivot_row], m_copy[i]
        identity[i], identity[pivot_row] = identity[pivot_row], identity[i]
        
        # Jika pivot adalah 0, matriks ini tidak punya invers
        pivot_val = m_copy[i][i]
        if pivot_val == 0:
            raise ValueError("Matriks ini tidak memiliki invers (singular).")
            
        # Buat pivot menjadi 1 dengan membagi seluruh barisnya dengan nilai pivot
        for j in range(n):
            m_copy[i][j] /= pivot_val
            identity[i][j] /= pivot_val
            
        # Buat elemen lain di kolom yang sama menjadi 0
        for j in range(n):
            if i != j:
                factor = m_copy[j][i]
                for k in range(n):
                    m_copy[j][k] -= factor * m_copy[i][k]
                    identity[j][k] -= factor * identity[i][k]
                    
    # === LANGKAH 3: KEMBALIKAN HASIL ===
    # Matriks 'identity' sekarang berisi invers dari matriks asli
    return Matrix(identity)
