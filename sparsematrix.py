# matriks/sparsematrix.py

# 1. IMPOR DIPERBAIKI: Menggunakan nama file yang benar ('matriks')
from matriks import Matrix

class SparseMatrix(Matrix):
    """
    Representasi matriks jarang (sparse) yang lebih efisien.
    Mematuhi LSP karena dapat menggantikan Matrix biasa.
    """
    def __init__(self, data):
        # Memanggil konstruktor kelas induk (Matrix) untuk validasi awal
        super().__init__(data)
        
        # Menyimpan data dalam format dictionary yang efisien
        self._sparse_data = {}
        for r, row_data in enumerate(data):
            for c, value in enumerate(row_data):
                if value != 0:
                    self._sparse_data[(r, c)] = value
    
    # Override metode get_value untuk mengambil data dari dictionary
    def get_value(self, row, col):
        """Mengambil nilai dari koordinat (row, col), mengembalikan 0 jika tidak ada."""
        return self._sparse_data.get((row, col), 0)

    # 2. OPTIMALISASI __str__: Metode __str__ dibuat lebih efisien
    def __str__(self):
        """Mengembalikan representasi string dari matriks."""
        all_rows = []
        for r in range(self.rows):
            row_str_list = [str(self.get_value(r, c)) for c in range(self.cols)]
            all_rows.append(" ".join(row_str_list))
        return "\n".join(all_rows)
