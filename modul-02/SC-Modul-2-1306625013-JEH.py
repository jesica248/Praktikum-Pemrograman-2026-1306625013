#identitas
print("Program Faktor Bilangan")
print("Nama : Jesica Elisabeth Hasibuan")
print("NIM : 1306625013")
print()

#program
while True: 
    hasil =[]
    n = int(input("Masukkan bilangan <100 (selesai = 0) ="))
    if n== 0:
        break
    for i in range (1, n + 1):
        if n % i == 0:
            hasil.append(i)
    print("Bilangan", i, 'Faktornya', hasil )
print("SELESAI")
