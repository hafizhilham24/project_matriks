# matriks.py

class Matrix:
    """
    Kelas ini merepresentasikan sebuah matriks.
    Tugasnya adalah menyimpan data matriks dan dimensinya.
    """
    def __init__(self, data):
        # Validasi bahwa input adalah list of lists
        if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
            raise TypeError("Data input harus berupa list of lists.")

        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

        # Validasi bahwa semua baris memiliki panjang yang sama
        if not all(len(row) == self.cols for row in data):
            raise ValueError("Semua baris dalam matriks harus memiliki jumlah kolom yang sama.")
    def get_value(self, row, col):
        """Mengambil nilai dari koordinat (row, col) pada matriks biasa."""
        return self.data[row][col]
    def __str__(self):
        """
        Method ini akan dipanggil saat kita melakukan print() pada objek Matrix.
        Ini cara yang lebih baik daripada membuat fungsi print_matrix terpisah.
        """
        if not self.data:
            return "[]"
        return '\n'.join(['[' + ', '.join(map(str, row)) + ']' for row in self.data])
