
import pandas as pd
from pathlib import Path


def hitung_grade(na):
    if na >= 86:
        return "A"
    elif na >= 81:
        return "A-"
    elif na >= 76:
        return "B+"
    elif na >= 71:
        return "B"
    elif na >= 66:
        return "B-"
    elif na >= 61:
        return "C+"
    elif na >= 56:
        return "C"
    else:
        return "TL"


def main():
    # Identitas mahasiswa
    print("Program Grading")
    print("Nama : Jesica Elisabeth Hasibuan")
    print("NIM  : 1306625013")
    print("\nLAPORAN GRADING MAHASISWA")

    # Membaca file Excel dari folder yang sama
    folder = Path(__file__).resolve().parent
    pilihan_file = [
        folder / "DataNilai.xlsx",
        folder / "DataNilai(2).xlsx"
    ]

    file_excel = next(
        (file for file in pilihan_file if file.exists()),
        None
    )

    if file_excel is None:
        print("File Excel tidak ditemukan!")
        print("Periksa nama dan lokasi file Excel.")
        return

    try:
        df = pd.read_excel(file_excel)
    except ImportError:
        print("Library openpyxl belum terpasang.")
        print("Jalankan: python -m pip install openpyxl")
        return

    # Mengambil kolom sesuai urutan dalam Excel
    col_nama = df.columns[0]
    col_lain = df.columns[2]
    col_uts = df.columns[3]
    col_uas = df.columns[4]

    # Menghapus baris yang tidak memiliki nilai lengkap
    df = df.dropna(
        subset=[col_nama, col_lain, col_uts, col_uas]
    ).reset_index(drop=True)

    # Menyiapkan rekapitulasi
    rekap = {
        "A": 0,
        "A-": 0,
        "B+": 0,
        "B": 0,
        "B-": 0,
        "C+": 0,
        "C": 0,
        "TL": 0
    }

    # Header tabel
    lebar = 55
    garis = "-" * lebar

    print(garis)
    print(
        f"{'No':<5}|"
        f"{'Nama Mahasiswa':<25}|"
        f"{'Nilai Akhir':<14}|"
        f"{'Grade':<7}|"
    )
    print(garis)

    # Menghitung nilai dan grade setiap mahasiswa
    for i, (_, row) in enumerate(df.iterrows(), start=1):
        nama = str(row[col_nama])
        nilai_lain = float(row[col_lain])
        nilai_uts = float(row[col_uts])
        nilai_uas = float(row[col_uas])

        nilai_akhir = (
            0.30 * nilai_lain
            + 0.35 * nilai_uts
            + 0.35 * nilai_uas
        )

        grade = hitung_grade(nilai_akhir)
        rekap[grade] += 1

        print(
            f"{i:<5}|"
            f"{nama[:24]:<25}|"
            f"{nilai_akhir:<14.2f}|"
            f"{grade:<7}|"
        )

    print(garis)

    # Rekapitulasi grade
    print("\nRekapitulasi :")
    print(f"Grade A         = {rekap['A']}")
    print(f"Grade A-        = {rekap['A-']}")
    print(f"Grade B+        = {rekap['B+']}")
    print(f"Grade B         = {rekap['B']}")
    print(f"Grade B-        = {rekap['B-']}")
    print(f"Grade C+        = {rekap['C+']}")
    print(f"Grade C         = {rekap['C']}")
    print(f"Tidak Lulus (TL)= {rekap['TL']}")
    print(f"Total Mahasiswa = {len(df)}")
    print("\nselesai")


if __name__ == "__main__":
    main()
