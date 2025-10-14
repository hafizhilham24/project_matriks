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
    
    # Return raw data points along with matrices
    return X, y, fitur_data, target_data, daftar_kolom_fitur

def run_regression_and_get_results():
    """Runs the regression analysis and returns results including data for plotting."""
    # --- KONFIGURASI ANALISIS ---
    file_data_input = 'coffee_shop_revenue.csv'
    nama_kolom_fitur = [
        'Number_of_Customers_Per_Day', 'Average_Order_Value', 'Operating_Hours_Per_Day',
        'Number_of_Employees', 'Marketing_Spend_Per_Day', 'Location_Foot_Traffic'
    ]
    nama_kolom_target = 'Daily_Revenue'
    # --------------------------

    try:
        # 1. Muat dan siapkan data
        X, y, raw_features, raw_target, fitur_terpakai = muat_data_regresi(file_data_input, nama_kolom_fitur, nama_kolom_target)

        # 2. Terapkan Normal Equation: theta = inv(X^T * X) * X^T * y
        X_transpose = transpose_matrix(X)
        XT_X = multiply_matrices(X_transpose, X)
        XT_X_inv = inverse_matrix(XT_X)
        XT_y = multiply_matrices(X_transpose, y)
        theta = multiply_matrices(XT_X_inv, XT_y)
        
        # 3. Menampilkan model regresi yang mudah dibaca
        intercept = theta.get_value(0, 0)
        model_str = f"{nama_kolom_target} = {intercept:.2f}"
        for i, nama in enumerate(fitur_terpakai):
            koefisien = theta.get_value(i + 1, 0)
            model_str += f" + ({koefisien:.2f} * {nama})"

        return {
            "model_str": model_str,
            "raw_features": raw_features,
            "raw_target": raw_target,
            "theta": theta,
            "target_name": nama_kolom_target,
            "feature_names": fitur_terpakai,
        }
    except Exception as e:
        return {"error": f"[ERROR] Terjadi error saat menghitung regresi: {e}"}

# Main guard remains for CLI execution if needed
if __name__ == "__main__":
    result = run_regression_and_get_results()
    if "error" in result:
        print(result["error"])
    else:
        print("\nKoefisien (theta) berhasil dihitung:")
        print(result["theta"])
        print("\nModel Regresi Linear:")
        print(result["model_str"])
