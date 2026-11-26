
# SIMULASI PERMAINAN BILYARD
# Tampilan mengikuti contoh praktikum Universitas Negeri Jakarta

import pygame
import math
import os

pygame.init()

# Ukuran layar dan warna (sama seperti contoh)
Lebar, Tinggi = 1050, 600
layar = pygame.display.set_mode((Lebar, Tinggi))
pygame.display.set_caption("LATIHAN")

white = (250, 250, 250)
whitedull = (243, 243, 242)
black = (70, 70, 70)
blue = (45, 127, 184)
gold = (248, 179, 35)
gray = (128, 128, 128)
green = (0, 128, 0)
red = (220, 40, 40)
yellow = (255, 255, 0)

# Font dan teks
font1 = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 25)
text1 = font1.render("SIMULASI BILYARD", True, white)
text2 = font2.render("Stick-bilyard", True, white)

# Suara boleh tidak ada; permainan tetap berjalan
click_sound = None
try:
    file_suara = os.path.join(os.path.dirname(__file__), "click.wav")
    if os.path.exists(file_suara):
        click_sound = pygame.mixer.Sound(file_suara)
except pygame.error:
    pass

# Koordinat 6 lubang (3 atas, 3 bawah)
lubang = [(55, 65), (520, 55), (995, 65),
          (55, 525), (520, 535), (995, 525)]
radius = 15

def buat_bola():
    return [
        {'x': 250, 'y': 295, 'vx': 0, 'vy': 0, 'warna': white, 'aktif': True},
        {'x': 640, 'y': 295, 'vx': 0, 'vy': 0, 'warna': red, 'aktif': True},
        {'x': 676, 'y': 275, 'vx': 0, 'vy': 0, 'warna': yellow, 'aktif': True},
        {'x': 676, 'y': 315, 'vx': 0, 'vy': 0, 'warna': blue, 'aktif': True}
    ]

bola = buat_bola()
menarik = False
fpsclock = pygame.time.Clock()

def bola_berhenti():
    return all(not b['aktif'] or math.hypot(b['vx'], b['vy']) < 0.08 for b in bola)

def gerakkan_bola():
    # Dua langkah kecil per frame supaya tumbukan lebih stabil
    for langkah in range(2):
        for b in bola:
            if not b['aktif']:
                continue

            b['x'] += b['vx'] / 2
            b['y'] += b['vy'] / 2

            # Bola masuk lubang
            if any(math.hypot(b['x'] - x, b['y'] - y) < 23 for x, y in lubang):
                b['aktif'] = False
                b['vx'] = b['vy'] = 0
                continue

            # Pantulan di keempat sisi meja
            if b['x'] < 65 or b['x'] > 985:
                b['x'] = max(65, min(985, b['x']))
                b['vx'] *= -0.92

            if b['y'] < 75 or b['y'] > 515:
                b['y'] = max(75, min(515, b['y']))
                b['vy'] *= -0.92

        # Tumbukan bola dengan bola: massa dianggap sama
        for i in range(len(bola)):
            for j in range(i + 1, len(bola)):
                a, b = bola[i], bola[j]
                if not a['aktif'] or not b['aktif']:
                    continue

                dx, dy = b['x'] - a['x'], b['y'] - a['y']
                jarak = math.hypot(dx, dy)
                if 0 < jarak < 2 * radius:
                    nx, ny = dx / jarak, dy / jarak
                    geser = (2 * radius - jarak) / 2
                    a['x'] -= nx * geser
                    a['y'] -= ny * geser
                    b['x'] += nx * geser
                    b['y'] += ny * geser

                    # Perubahan momentum dengan koefisien pantul 0.97
                    v = (b['vx'] - a['vx']) * nx + (b['vy'] - a['vy']) * ny
                    if v < 0:
                        impuls = -(1 + 0.97) * v / 2
                        a['vx'] -= impuls * nx
                        a['vy'] -= impuls * ny
                        b['vx'] += impuls * nx
                        b['vy'] += impuls * ny

    # Gesekan meja membuat bola pelan-pelan berhenti
    for b in bola:
        if b['aktif']:
            b['vx'] *= 0.991
            b['vy'] *= 0.991
            if math.hypot(b['vx'], b['vy']) < 0.08:
                b['vx'] = b['vy'] = 0

# Program utama Pygame
selesai = False
while not selesai:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            selesai = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            bola = buat_bola()
            menarik = False

        # Mulai menarik stik dari dekat bola putih
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            putih = bola[0]
            if (putih['aktif'] and bola_berhenti()
                    and math.hypot(x - putih['x'], y - putih['y']) < 30):
                menarik = True

        # Lepas mouse untuk memukul (arah berlawanan dengan tarikan)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and menarik:
            menarik = False
            x, y = event.pos
            putih = bola[0]
            dx, dy = putih['x'] - x, putih['y'] - y
            panjang = math.hypot(dx, dy)
            if panjang > 8:
                tenaga = min(17, panjang * 0.09)
                putih['vx'] = dx / panjang * tenaga
                putih['vy'] = dy / panjang * tenaga
                if click_sound:
                    click_sound.play()

    gerakkan_bola()

    # Mengembalikan bola putih bila masuk lubang
    if not bola[0]['aktif'] and bola_berhenti():
        bola[0].update(x=250, y=295, vx=0, vy=0, aktif=True)

    # Tampilan mengikuti contoh program asli
    layar.fill(green)
    pygame.draw.rect(layar, white, [50, 60, 950, 470], 4)
    layar.blit(text1, [360, 10])
    layar.blit(text2, [50, 575])

    for x, y in lubang:
        pygame.draw.circle(layar, whitedull, (x, y), 25)

    # Stik bawah seperti contoh
    pygame.draw.rect(layar, gray, [50, 555, 105, 3], 3)

    # Tampilkan stik yang diarahkan dengan mouse saat ditarik
    if menarik and bola[0]['aktif']:
        putih = bola[0]
        mx, my = pygame.mouse.get_pos()
        dx, dy = mx - putih['x'], my - putih['y']
        panjang = math.hypot(dx, dy)
        if panjang > 0:
            nx, ny = dx / panjang, dy / panjang
            awal = (int(putih['x'] + nx * 23), int(putih['y'] + ny * 23))
            akhir = (int(putih['x'] + nx * (130 + min(panjang, 150))),
                     int(putih['y'] + ny * (130 + min(panjang, 150))))
            pygame.draw.line(layar, gray, awal, akhir, 7)
            pygame.draw.line(layar, gold, awal,
                             (int(putih['x'] + nx * 38),
                              int(putih['y'] + ny * 38)), 4)

            # Garis bantu arah bola melaju
            tujuan = (int(putih['x'] - nx * 90),
                      int(putih['y'] - ny * 90))
            pygame.draw.line(layar, white,
                             (int(putih['x']), int(putih['y'])), tujuan, 1)

    for b in bola:
        if b['aktif']:
            pygame.draw.circle(layar, b['warna'],
                               (int(b['x']), int(b['y'])), radius)

    pygame.display.flip()
    fpsclock.tick(120)

pygame.quit()
