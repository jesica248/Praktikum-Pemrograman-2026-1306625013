Modul [07] - [Simulasi Permainan Mini Billyard] Nama: [Jesica Elisabeth Hasibuan] NIM: [1306625013] Kelas: [Fisika C]

Problem Statement 
Permainan mini billiard merupakan simulasi permainan bola yang menggunakan tongkat untuk memukul bola menuju lubang pada meja billiard. Pada praktikum ini, dibuat program permainan mini billiard menggunakan Python dan library Pygame untuk menggambarkan pergerakan bola ketika dipukul serta interaksi bola dengan dinding meja dan bola lainnya.

Parameter yang digunakan meliputi posisi bola, kecepatan bola, arah pukulan, gaya pukulan, dan koefisien pantulan. Tujuan praktikum ini adalah memahami konsep gerak, kecepatan, tumbukan, dan pantulan melalui simulasi permainan sederhana.

Mathematical Equation 
a. Komponen kecepatan bola
\[
v_x = v\cos\theta
\]

\[
v_y = v\sin\theta
\]

b. Persamaan posisi bola
\[
x = x_0 + v_xt
\]

\[
y = y_0 + v_yt
\]

c. Koefisien pantulan
\[
v_{\text{sesudah}} = -e \cdot v_{\text{sebelum}}
\]

d. Perlambatan akibat gesekan
\[
v = v_0 - at
\]

Keterangan:
- \(v\) = kecepatan bola
- \(v_0\) = kecepatan awal
- \(\theta\) = sudut pukulan
- \(x,y\) = posisi bola
- \(e\) = koefisien pantulan
- \(a\) = perlambatan akibat gesekan
- \(t\) = waktu
  
Algorithm 
1. Mulai program.
2. Import library Pygame dan inisialisasi program.
3. Tentukan ukuran layar, warna background, dan ukuran meja billiard.
4. Tentukan posisi awal bola putih dan bola target.
5. Tentukan parameter kecepatan, arah pukulan, dan koefisien pantulan.
6. Buat objek bola, tongkat billiard, dan lubang meja.
7. Jalankan perulangan utama (game loop).
8. Baca input mouse untuk menentukan arah dan kekuatan pukulan.
9. Gerakkan bola berdasarkan kecepatan dan waktu.
10. Periksa tumbukan antara bola dengan bola lainnya dan dinding meja.
11. Terapkan perubahan arah kecepatan ketika terjadi tumbukan.
12. Kurangi kecepatan bola akibat gesekan hingga bola berhenti.
13. Periksa apakah bola masuk ke dalam lubang.
14. Tampilkan seluruh objek permainan pada layar.
15. Perbarui tampilan permainan.
16. Jika permainan ditutup, hentikan program.
17. Selesai.
