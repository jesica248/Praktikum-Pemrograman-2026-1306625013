import math


def main():
    print("=" * 65)
    print("PEMROGRAMAN SINUS-COSINUS".center(65))
    print("Nama : Jesica Elisabeth Hasibuan")
    print("NIM  : 1306625013")
    print("=" * 65)

    while True:
        sudut_deg = float(input("\nMasukkan besaran sudut (derajat) = "))
        x_rad = math.radians(sudut_deg)

        
        tv_sin = round(math.sin(x_rad), 2)
        tv_cos = round(math.cos(x_rad), 2)

        print(f"\nTrue Value Sin ({sudut_deg:.1f}) = {tv_sin:.2f}")
        print(f"True Value Cos ({sudut_deg:.1f}) = {tv_cos:.2f}")

        garis = "-" * 65
        print(garis)
        print(
            f"{'Jumlah':<11} | {'AV':^10} | {'ER':^10} | "
            f"{'AV':^12} | {'ER':^10}"
        )
        print(
            f"{'Suku':<11} | {'sinus':^10} | {'sinus':^10} | "
            f"{'cosinus':^12} | {'cosinus':^10}"
        )
        print(garis)

        suku = 1
        av_sin = 0.0
        av_cos = 0.0

        while True:
            
            term_sin = (
                (-1) ** (suku - 1) * x_rad ** (2 * suku - 1)
                / math.factorial(2 * suku - 1)
            )
            term_cos = (
                (-1) ** (suku - 1) * x_rad ** (2 * suku - 2)
                / math.factorial(2 * suku - 2)
            )

            av_sin += term_sin
            av_cos += term_cos

            
            av_sin_tampil = round(av_sin, 2)
            av_cos_tampil = round(av_cos, 2)

            er_sin = (
                abs((av_sin_tampil - tv_sin) / tv_sin) * 100
                if tv_sin != 0 else 0.0
            )
            er_cos = (
                abs((av_cos_tampil - tv_cos) / tv_cos) * 100
                if tv_cos != 0 else 0.0
            )

            er_sin_tampil = f"{er_sin:.0f}%"
            er_cos_tampil = f"{er_cos:.0f}%"

            print(
                f"{suku:<11} | {av_sin_tampil:^10.2f} | "
                f"{er_sin_tampil:^10} | {av_cos_tampil:^12.2f} | "
                f"{er_cos_tampil:^10}"
            )

            if er_sin < 5 and er_cos < 5:
                break

            suku += 1

        print(garis)
        ulang = input("\nIngin menghitung lagi (yay/nay)? ").strip().lower()

        if ulang != "yay":
            print("\nSelesai")
            break


if __name__ == "__main__":
    main()
