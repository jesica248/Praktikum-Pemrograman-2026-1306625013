# Modul [03] - [Trigonometri]

**Nama:** [Jesica Elisabeth Hasibuan]  
**NIM:** [1306625013]  
**Kelas:** [Fisika c]  

---

## 1. Problem Statement
> Membuat program untuk menghitung nilai sin dan cos dengan pendekatan deret Mc Laurin
## 2. Mathematical Equation
Di file **README.md** kamu saat ini, poin **a, b, dan c** terhapus secara tidak sengaja sehingga langsung melompat ke poin **d**.

Berikut adalah kode Markdown lengkap untuk bagian **2. Mathematical Equation** agar strukturnya utuh kembali:

```markdown
Deret Maclaurin merupakan kasus khusus dari deret Taylor yang diekspansi di sekitar titik $x = 0$.

### a. Konversi Satuan Sudut
Sebelum dihitung menggunakan deret Maclaurin, sudut $x$ dalam satuan derajat ($\text{deg}$) harus dikonversi ke satuan radian ($\text{rad}$):
$$x_{\text{rad}} = x_{\text{deg}} \times \frac{\pi}{180}$$

---

### b. Deret Maclaurin untuk Sinus ($\sin x$)
Persamaan analitik deret Maclaurin untuk fungsi sinus:
$$\sin(x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots$$

**Formulasi Rekursif Numerik:**
Untuk komputasi yang efisien, suku ke-$n$ ($u_n$) dihitung berdasarkan suku sebelumnya ($u_{n-1}$):
$$u_n = -u_{n-1} \times \frac{x^2}{2n(2n+1)}$$
dengan suku awal $u_0 = x$.

---

### c. Deret Maclaurin untuk Kosinus ($\cos x$)
Persamaan analitik deret Maclaurin untuk fungsi kosinus:
$$\cos(x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots$$

**Formulasi Rekursif Numerik:**
Suku ke-$n$ ($v_n$) dihitung berdasarkan suku sebelumnya ($v_{n-1}$):
$$v_n = -v_{n-1} \times \frac{x^2}{(2n-1)2n}$$
dengan suku awal $v_0 = 1$.

---

### d. Perhitungan Galat Relatif (Persentase Error)
Perhitungan galat relatif dilakukan untuk mengukur akurasi hasil pendekatan deret Maclaurin (*Actual Value* / $AV$) terhadap nilai persis dari fungsi pustaka (*True Value* / $TV$):
$$\text{Error (\%)} = \left\vert{} \frac{AV - TV}{TV} \right\vert{} \times 100\%$$

**Keterangan:**
* $AV$ (*Actual Value*) = Nilai aproksimasi deret Maclaurin hasil program.
* $TV$ (*True Value*) = Nilai eksak menggunakan fungsi pustaka Python (`math.sin` atau `math.cos`).

```

Kamu bisa menyalin seluruh blok kode di atas dan menempelkannya (*paste*) di antara baris `## 2. Mathematical Equation` dan `## 3. Algorithm` pada editor GitHub kamu.


### d. Perhitungan Galat Relatif (Persentase Error)
Perhitungan galat relatif dilakukan untuk mengukur akurasi hasil pendekatan deret Maclaurin (*Actual Value* / $AV$) terhadap nilai persis dari fungsi pustaka (*True Value* / $TV$):
$$\text{Error (\%)} = \left\vert{} \frac{AV - TV}{TV} \right\vert{} \times 100\%$$

**Keterangan:**
* $AV$ (*Actual Value*) = Nilai aproksimasi deret Maclaurin hasil program.
* $TV$ (*True Value*) = Nilai eksak menggunakan fungsi pustaka Python (`math.sin` atau `math.cos`).

```


## 3. Algorithm
> Tuliskan langkah-langkah logika penyelesaian masalah secara sistematis sebelum diimplementasikan ke dalam kode Python (`main.py`).
