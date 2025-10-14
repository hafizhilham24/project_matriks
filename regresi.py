# regresi.py (untuk coffee_shop_revenue.csv)

import csv
from matriks import Matrix
from operations.multiply_matrices import multiply_matrices
from operations.transpose import transpose_matrix
from operations.inverse import inverse_matrix

def muat_data_regresi(nama_file: str, daftar_kolom_fitur: list, nama_kolom_target: str):
    """Memuat data dari CSV untuk regresi linear berganda."""
    fitur_data = []
    target_data = []
    
    with open(nama_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Ambil semua nilai fitur untuk satu baris
                satu_baris_fitur = [float(row[kolom]) for kolom in daftar_kolom_fitur]
                fitur_data.append(satu_baris_fitur)
                
                # Ambil nilai target
                target_data.append(float(row[nama_kolom_target]))
            except (ValueError, KeyError) as e:
                print(f"Peringatan: Melewati baris karena error data: {e} -> {row}")
                continue
            
    # Menambahkan kolom bias (angka 1) ke setiap baris data fitur
    data_X = [[1] + baris for baris in fitur_data]
    
    # Membuat matriks y (vektor kolom)
    data_y = [[target] for target in target_data]
    
    X = Matrix(data_X)
    y = Matrix(data_y)
    
    return X, y, daftar_kolom_fitur

if __name__ == "__main__":
    # --- KONFIGURASI ANALISIS ---
    file_data_input = 'coffee_shop_revenue.csv'

    # 6 kolom fitur yang akan digunakan untuk prediksi
    nama_kolom_fitur = [
        'Number_of_Customers_Per_Day', 
        'Average_Order_Value', 
        'Operating_Hours_Per_Day', 
        'Number_of_Employees', 
        'Marketing_Spend_Per_Day', 
        'Location_Foot_Traffic'
    ]
    
    # Kolom target yang ingin diprediksi
    nama_kolom_target = 'Daily_Revenue'
    # --------------------------

    # 1. Muat dan siapkan data
    X, y, fitur_terpakai = muat_data_regresi(file_data_input, nama_kolom_fitur, nama_kolom_target)
    
    print(f"--- Menganalisis {file_data_input} untuk memprediksi '{nama_kolom_target}' ---")
    
    try:
        # 2. Terapkan Normal Equation: theta = inv(X^T * X) * X^T * y
        X_transpose = transpose_matrix(X)
        XT_X = multiply_matrices(X_transpose, X)
        XT_X_inv = inverse_matrix(XT_X) 
        XT_y = multiply_matrices(X_transpose, y)
        theta = multiply_matrices(XT_X_inv, XT_y)
        
        print("\nKoefisien (theta) berhasil dihitung:")
        print(theta)

        # 3. Menampilkan model regresi yang mudah dibaca
        intercept = theta.get_value(0, 0)
        model_str = f"{nama_kolom_target} = {intercept:.2f}"
        for i, nama in enumerate(fitur_terpakai):
            koefisien = theta.get_value(i + 1, 0)
            model_str += f" + ({koefisien:.2f} * {nama})"
        
        print("\nModel Regresi Linear:")
        print(model_str)

    except Exception as e:
        print(f"\n[ERROR] Terjadi error saat menghitung regresi: {e}")
