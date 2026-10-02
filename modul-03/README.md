# Modul [03] - [Trigonometri]

**Nama:** [Jesica Elisabeth Hasibuan]  
**NIM:** [1306625013]  
**Kelas:** [Fisika c]  



## 1. Problem Statement
> Membuat program untuk menghitung nilai sin dan cos dengan pendekatan deret Mc Laurin
## 2. Mathematical Equation
Berikut adalah isi lengkap untuk bagian **2. Mathematical Equation** yang menggunakan simbol sigma ($\sum$) dan rumus persentase error $\frac{\vert{}AV - TV\vert{}}{TV} \times 100\%$:

```markdown
Deret Maclaurin merupakan kasus khusus dari deret Taylor yang diekspansi di sekitar titik $x = 0$.

### a. Konversi Satuan Sudut
Sebelum dihitung menggunakan deret Maclaurin, sudut $x$ dalam satuan derajat ($\text{deg}$) dikonversi ke satuan radian ($\text{rad}$):
$$x_{\text{rad}} = x_{\text{deg}} \times \frac{\pi}{180}$$

---

### b. Deret Maclaurin untuk Sinus ($\sin x$)
Persamaan analitik deret Maclaurin untuk fungsi sinus disajikan dalam bentuk deret/sigma:
$$\sin(x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots$$

**Formulasi Rekursif Numerik:**
$$u_n = -u_{n-1} \times \frac{x^2}{2n(2n+1)}$$
dengan suku awal $u_0 = x$.

---

### c. Deret Maclaurin untuk Kosinus ($\cos x$)
Persamaan analitik deret Maclaurin untuk fungsi kosinus disajikan dalam bentuk deret/sigma:
$$\cos(x) = \sum_{n=0}^{\infty} (-1)^n \frac{x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots$$

**Formulasi Rekursif Numerik:**
$$v_n = -v_{n-1} \times \frac{x^2}{(2n-1)2n}$$
dengan suku awal $v_0 = 1$.

---

### d. Perhitungan Galat Relatif (Persentase Error)
Perhitungan persentase galat (*error*) antara nilai hasil aproksimasi deret (*Actual Value* / $AV$) dan nilai eksak pustaka (*True Value* / $TV$):
$$\text{Error (\%)} = \left\vert{} \frac{AV - TV}{TV} \right\vert{} \times 100\%$$

**Keterangan:**
* $AV$ (*Actual Value*) = Nilai aproksimasi hasil perhitungan deret Maclaurin.
* $TV$ (*True Value*) = Nilai eksak dari fungsi bawaan pustaka Python (`math.sin` atau `math.cos`).

```

Salin teks di atas dan tempelkan tepat di bawah baris `## 2. Mathematical Equation` (baris 11) pada editor GitHub kamu.



## 3. Algorithm
> Tuliskan langkah-langkah logika penyelesaian masalah secara sistematis sebelum diimplementasikan ke dalam kode Python (`main.py`).
