# matriks/exporters/csv_exporter.py
import csv
from matriks import Matrix # Impor opsional, baik untuk type hinting

def export_to_csv(matrix: Matrix, filename: str):
    """
    Mengekspor data matriks ke file CSV.
    Fungsi ini kompatibel dengan Matrix biasa dan SparseMatrix.
    """
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Jangan akses .data secara langsung.
        # Kita buat ulang datanya menggunakan get_value agar berfungsi untuk semua tipe matriks.
        for r in range(matrix.rows):
            # Membuat satu baris data dengan mengambil setiap nilai dari matriks
            row_data = [matrix.get_value(r, c) for c in range(matrix.cols)]
            writer.writerow(row_data) # Menulis baris per baris
            
    print(f"Matriks berhasil diekspor ke {filename}")
