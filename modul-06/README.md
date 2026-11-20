Modul [06] - [Simulasi Bola Jatuh Bebas]
Nama: [Jesica Elisabeth Hasibuan]
NIM: [1306625013]
Kelas: [Fisika C]

1. Problem Statement
Membuat Gerak jatuh bebas merupakan gerakan benda yang jatuh dari ketinggian tertentu akibat pengaruh gaya gravitasi. Pada praktikum ini, dibuat program simulasi bola jatuh bebas menggunakan Python dan library Pygame untuk menggambarkan pergerakan bola dari posisi awal hingga menyentuh lantai.

Parameter yang digunakan meliputi posisi awal bola, kecepatan awal, percepatan gravitasi sebesar \(10\ \text{m/s}^2\), dan koefisien pantulan. Tujuan praktikum ini adalah memahami hubungan antara waktu, kecepatan, dan posisi benda serta menerapkannya dalam simulasi visual

2. Mathematical Equation
a. Persamaan kecepatan
\[
v = v_0 + gt
\]

b. Persamaan posisi
\[
y = y_0 + v_0t + \frac{1}{2}gt^2
\]

Karena bola dijatuhkan tanpa kecepatan awal:
\[
v_0 = 0
\]

Maka:
\[
y = y_0 + \frac{1}{2}gt^2
\]

c. Persamaan pantulan
\[
v_{\text{baru}} = -e \cdot v_{\text{sebelum}}
\]

Keterangan:
- \(v\) = kecepatan bola
- \(v_0\) = kecepatan awal
- \(g\) = gravitasi (10 m/s²)
- \(t\) = waktu
- \(y\) = posisi bola
- \(e\) = koefisien pantulan
- 
3. Algorithm
1.Mulai program.
2.Import library Pygame.
3.Inisialisasi Pygame dan tentukan ukuran layar serta warna background.
4.Tentukan parameter bola, posisi awal, kecepatan awal, gravitasi, dan koefisien pantulan.
5.Buat objek bola dan tentukan posisi lantai.
6.Jalankan perulangan utama (game loop).
7.Hitung perubahan kecepatan dan posisi bola berdasarkan gravitasi.
8.Perbarui posisi bola setiap frame.
9.Periksa apakah bola menyentuh lantai.
10.Jika menyentuh lantai, ubah arah kecepatan berdasarkan koefisien pantulan
11.Tampilkan bola, garis lantai berwarna hitam, dan koordinat bola pada layar.
12.Perbarui tampilan simulasi.
13.Jika jendela ditutup, hentikan program.
14.Selesai.
