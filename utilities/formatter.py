# matriks/utilities/formatter.py

def print_matrix(matrix):
    """
    Mencetak matriks ke konsol dengan format yang rapi.
    Fungsi ini tidak mengembalikan nilai (return None).
    """
    # Membuat list yang berisi string dari setiap baris
    lines = []
    for row in matrix.data:
        # Mengubah setiap angka di baris menjadi string, lalu menggabungkannya dengan spasi
        lines.append(" ".join(map(str, row)))
    
    # Menggabungkan semua baris menjadi satu string besar dengan pemisah baris baru
    # lalu mencetaknya ke konsol
    formatted_output = "\n".join(lines)
    print(formatted_output)
