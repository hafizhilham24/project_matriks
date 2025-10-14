# main.py
import time
from matriks import Matrix 
from operations.add_matrices import add_matrices
from operations.multiply_matrices import multiply_matrices
from utilities.formatter import print_matrix
from sparsematrix import SparseMatrix
from exporters.csv_exporter import export_to_csv
from exporters.json_exporter import export_to_json
from operations.transpose import transpose_matrix
from operations.inverse import inverse_matrix

def create_sparse_data(size):
    """Fungsi untuk membuat data matriks jarang (sparse)."""
    data = [[0] * size for _ in range(size)]
    data[0][0] = 1
    data[size-1][size-1] = 1
    return data

# Semua eksekusi digabungkan dalam satu blok utama
if __name__ == "__main__":
    
    # --- Uji Coba Penjumlahan dan Perkalian Dasar ---
    matriks_a = Matrix([[1, 2], [3, 4]])
    matriks_b = Matrix([[5, 6], [7, 8]])

    print("Hasil Penjumlahan:")
    hasil_penjumlahan = add_matrices(matriks_a, matriks_b)
    print_matrix(hasil_penjumlahan)

    print("\nHasil Perkalian:")
    hasil_perkalian = multiply_matrices(matriks_a, matriks_b)
    print_matrix(hasil_perkalian)

    # --- Uji Coba Ekspor Data ---
    # Variabel matriks_demo sekarang sudah didefinisikan
    matriks_demo = Matrix([[10, 20], [30, 40]]) 
    
    print("\nMengekspor matriks ke format CSV...")
    export_to_csv(matriks_demo, "matriks_output.csv")
    print("File 'matriks_output.csv' berhasil dibuat.")

    print("\nMengekspor matriks ke format JSON...")
    export_to_json(matriks_demo, "matriks_output.json")
    print("File 'matriks_output.json' berhasil dibuat.")

    # --- Uji Coba Penjumlahan Matriks Biasa dan Sparse ---
    print("\n--- Pembuktian OCP dengan Penjumlahan ---")
    matriks_padat = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matriks_jarang = SparseMatrix([[1, 0, 0], [0, 5, 0], [7, 0, 9]])
    
    hasil_penjumlahan_ocp = add_matrices(matriks_padat, matriks_jarang)
    print("Hasil Penjumlahan Matriks Biasa dan Sparse:")
    # Menggunakan print biasa karena print_matrix mungkin tidak dirancang untuk objek hasil campuran
    print(hasil_penjumlahan_ocp)

    print("\n--- Menguji Performa dengan SparseMatrix (Solusi) ---")
    sparse_data_1000 = create_sparse_data(100)
    # Membuat objek menggunakan kelas SparseMatrix yang efisien
    sparse_mat_a = SparseMatrix(sparse_data_1000)
    sparse_mat_b = SparseMatrix(sparse_data_1000)

    start_time_sparse = time.time()
    
    # Fungsi multiply_matrices yang sama, tapi sekarang dengan objek sparse
    product_sparse = multiply_matrices(sparse_mat_a, sparse_mat_b)
    
    end_time_sparse = time.time()
    
    print(f"Waktu perkalian dengan SparseMatrix: {end_time_sparse - start_time_sparse:.4f} detik")
    print("\n--- Menguji Transpose dan Invers (Gaya Fungsional) ---")
    
    mat_uji = Matrix([[1, 2], [3, 4]])
    print("Matriks Asli:")
    print(mat_uji)

    # 2. Ubah cara pemanggilan fungsi
    try:
        mat_transpose = transpose_matrix(mat_uji) # <- Diubah
        print("\nHasil Transpose:")
        print(mat_transpose)
    except Exception as e:
        print(f"Error saat transpose: {e}")
    
    try:
        mat_invers = inverse_matrix(mat_uji) # <- Diubah
        print("\nHasil Invers:")
        print(mat_invers)
    except Exception as e:
        print(f"Error saat invers: {e}")
