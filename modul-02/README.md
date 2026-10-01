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
>
1.Mulai
2.Print judul "Program Faktor Bilangan"
3.Print "Nama: Jesica Elisabeth Hasibuan"
4.Print "NIM: 1306625013"
5.Input $n$ ("Masukan sembarang bilangan < 100 (masukan 0 untuk selesai)")
6.Selama $n \neq 0$, ulangi langkah 7 sampai 12
7.Buat list kosong faktor = []
8.Set $d = 1$
9.Selama $d \le n$: jika $n \bmod d = 0$, tambahkan $d$ ke faktor
10.Naikkan $d$ sebesar 1 ($d = d + 1$), kembali ke langkah 9 sampai $d > n$
11.Print "Bilangan $n$ → Faktornya = faktor"
12.Input $n$ berikutnya
13.Jika $n = 0$, keluar dari perulangan, print "*SELESAI*"
14.Selesai
