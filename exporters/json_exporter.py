# matriks/exporters/json_exporter.py
import json
from matriks import Matrix

def export_to_json(matrix: Matrix, filename: str):
    """
    Mengekspor data matriks ke file JSON.
    Fungsi ini kompatibel dengan Matrix biasa dan SparseMatrix.
    """
    # 1. Ubah data matriks menjadi format list of lists menggunakan .get_value()
    # Ini adalah langkah kunci agar kompatibel dengan semua jenis matriks.
    data_to_write = []
    for r in range(matrix.rows):
        row = [matrix.get_value(r, c) for c in range(matrix.cols)]
        data_to_write.append(row)

    # 3. Buka file dengan nama `filename` dalam mode tulis ('w')
    with open(filename, 'w') as json_file:
        # 2. & 4. Konversi data ke JSON dan tuliskan ke file
        # json.dump() melakukan kedua langkah ini sekaligus.
        # `indent=4` membuat file JSON lebih mudah dibaca manusia.
        json.dump(data_to_write, json_file, indent=4)

    # 5. Tampilkan pesan sukses
    print(f"Matriks berhasil diekspor ke {filename}")
