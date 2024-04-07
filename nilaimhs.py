nama=input("Nama = ")
nim=input("Nim = ")
absen=int(input("Masukan nilai Absen= "))
uts=int(input("Masukan nilai UTS= "))
uas=int(input("Masukan nilai UAS= "))
print(" ")
standar=50
jumlah=absen+uts+uas
rata_rata= jumlah/3

print("===="*11)
Sprint("Nilai yang diperoleh oleh :")
print("Nama = ",nama)
print("Nim = ",nim)
print(" ")
print("Jumlah nilai yang didapatkan = ", jumlah)
print("Nilai rata-rata yang didapatkan = ", rata_rata)


if rata_rata >= 90:
    indeks = 'A'
elif rata_rata >= 80:
    indeks = 'B+'
elif rata_rata >= 70:
    indeks = 'B'
elif rata_rata >= 60:
    indeks = 'C+'
elif rata_rata >=50:
    indeks = 'C'
else :
    indeks = 'D'
print('predikat : ',indeks)



if rata_rata>=standar:
    print("------"*8)
    print('        "SELAMAT ANDA DINYATAKAN LULUS"       ')
    print("------"*8)
else:
    print("------"*12)
    print('"MAAF ANDA TIDAK DINYATAKAN LULUS, SILAHKAN BERJUANG LEBIH KERAS LAGI"')
    print("------"*12)
