import random

# Data nama buah sesuai modul
databuah = [
    'anggur', 'apel', 'aprikot', 'asam', 'atap', 'arbei', 'abiu',
    'alpukat', 'anjeng', 'bacang', 'baguk', 'belimbing', 'bengkuang',
    'benda', 'binjai', 'bisbul', 'blueberry', 'burahol', 'blewah',
    'bit', 'cempedak', 'ceplukan', 'cermai', 'ceri', 'cokelat',
    'delima', 'duku', 'durian', 'duwet', 'enau', 'enamenam',
    'frambos', 'hamoi', 'hamlam', 'holdi', 'jamblang', 'jambuair',
    'jambubatu', 'jambubol', 'jambumawar', 'jambumede', 'jengkol',
    'jeruk', 'jerukbali', 'jerukkeprok', 'jerukkingkit',
    'jeruknipis', 'jerukpurut', 'kapulasan', 'kawista', 'kecapi',
    'kedondong', 'kelapa', 'kelengkeng', 'kelubi', 'ketela',
    'kemang', 'kepel', 'kersen', 'kesemek', 'kokosan', 'kiwi',
    'koldi', 'kurma', 'kelawi', 'kenitu', 'lai', 'langsat',
    'lemon', 'leci', 'lobak', 'maja', 'malaka', 'mangga',
    'manggis', 'markisa', 'melon', 'mengkudu', 'menteng',
    'matoa', 'mentimun', 'namnam', 'nanas', 'nangka', 'naga',
    'nona', 'pepaya', 'persik', 'pir', 'pisang', 'pete',
    'rambai', 'rambusa', 'rambutan', 'rukem', 'sawo',
    'semangka', 'sirsak', 'siwalan', 'srikaya', 'stroberi',
    'sukun', 'terap', 'terong', 'tomat', 'timunsuri',
    'ubi', 'waluh', 'wuni', 'zaitun'
]


def main():

    print("Permainan Tebak Nama Buah")
    print("Oleh : Jesica Elisabeth Hasibuan")
    print("NIM : 1306625013")
    print()

    # Urutan buah mengikuti contoh pada modul
    contoh_buah = ['lai', 'persik']

    putaran = 0

    while putaran < 2:

        buah = contoh_buah[putaran]
        nyawa = len(buah)
        huruf_tebakan = []

        print("Komputer sedang memikirkan nama     buah terdiri dari",
              len(buah), "huruf.")

        print("Nama buah :", " ".join("-" for huruf in buah))
        print()

        # Proses menebak huruf
        while nyawa > 0:

            print("Anda memiliki", nyawa,
                  "kesempatan untuk menebak huruf buah tersebut")

            tebakan = input("Tebakan anda ? ").lower()

            # Memeriksa tebakan huruf
            if tebakan in buah:
                print("Benar. Huruf", tebakan,
                      "ada dalam nama buah tersebut.")
                huruf_tebakan.append(tebakan)

            else:
                print("Sayang sekali. Huruf", tebakan,
                      "tidak ada dalam nama buah tersebut.")
                nyawa -= 1
                huruf_tebakan.append(tebakan)

            print()

            # Membentuk tampilan nama buah
            tampilan = []

            for huruf in buah:
                if huruf in huruf_tebakan:
                    tampilan.append(huruf)
                else:
                    tampilan.append("-")

            # Memeriksa apakah semua huruf sudah ditemukan
            if all(huruf in huruf_tebakan for huruf in buah):
                print("Nama buah :", " ".join(tampilan))
                print()
                print("SELAMAT.   Anda   berhasil    !!")
                break

            # Jika kesempatan masih ada, tampilkan nama buah
            elif nyawa > 0:
                print("Nama buah :", " ".join(tampilan))
                print()

        # Jika pemain kehabisan kesempatan
        if nyawa == 0:
            print("Anda kalah !!.")
            print("Nama buah tersebut:", " ".join(buah))
            print()

        # Menanyakan apakah ingin bermain lagi
        ulang = input("Mau   main lagi (y/t) ?   ").lower()
        print()

        if ulang != 'y':
            break

        putaran += 1

    print("# SELESAI #")


if __name__ == "__main__":
    main()