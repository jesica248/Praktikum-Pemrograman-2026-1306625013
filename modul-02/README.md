# Modul [02] - [Mencari Faktor Bilangan]

**Nama:** [Jesica Elisabeth Hasibuan]  
**NIM:** [1306625013]  
**Kelas:** [Fisika C]  

---

## 1. Problem Statement
> Membuat program untuk mencari faktor dari suatu bilangan bulat positif kurang dari 100. Program berjalan berulang: pengguna memasukkan sebuah bilangan, lalu program menampilkan semua faktornya dalam bentuk list. Program berhenti saat pengguna memasukkan angka 0. Contoh: bilangan 15 → faktornya [1, 3, 5, 15], bilangan 24 → faktornya [1, 2, 3, 4, 6, 8, 12, 24].

## 2. Mathematical Equation
> Bilangan $f$ adalah faktor dari bilangan $n$ jika sisa hasil bagi $n$ dengan $f$ sama dengan nol:

$$n \bmod f = 0, \quad 1 \le f \le n$$

Himpunan faktor dari $n$:

$$F(n) = \{\, f \in \mathbb{Z}^{+} \mid 1 \le f \le n,\ n \bmod f = 0 \,\}$$

Contoh: $15 \bmod 3 = 0$ maka 3 adalah faktor 15, sedangkan $15 \bmod 4 = 3 \neq 0$ maka 4 bukan faktor 15.
## 3. Algorithm
> 1. Mulai
2. Print "Program Faktor Bilangan"
3. Print "Nama : Jesica Elisabeth Hasibuan"
4. Print "NIM : 1306625013"
5. Ulangi terus-menerus (while True):
   5.1 Input data: "Masukan sembarang bilangan < 100 ( masukan 0 untuk selesai) : "
   5.2 Jika data bukan bilangan bulat: Print "Input tidak valid", kembali ke langkah 5 (konektor A)
   5.3 Ubah data menjadi bilangan bulat: n = int(data)
   5.4 Jika n = 0: Print "SELESAI", keluar dari loop (break)
   5.5 Jika n < 0 atau n ≥ 100: Print pesan kesalahan, kembali ke langkah 5 (konektor A)
   5.6 Buat list kosong: faktor = [ ], dan f = 1
   5.7 Selama f ≤ n:
     5.7.1 Jika n mod f = 0: tambahkan f ke list faktor (faktor.append(f))
     5.7.2 f = f + 1
     5.7.3 Print "Bilangan n → Faktornya = faktor", lalu kembali ke langkah 5 (konektor A)
6. Print "Selesai"
7. Selesai
