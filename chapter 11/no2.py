#chapter 11
#no 02

from datetime import *

import os

if(os.path.exists("hasilPinjaman.txt")):
    fileMode ='a'
else:
    fileMode = 'W'
file = open("hasi1Pinjaman.txt", fileMode)

while True:

    kode = input ("Masukkan kode Member : ")
    nama = input ("Masukkan Nama Member : ")
    judul = input("Masukkan Judul Buku : ")

    tglHariIni = date.today()
    tglKembali = tglHariIni + timedelta (days = 7)

    hasilPinjaman = [kode, nama, judul, str(tglHariIni), str(tglKembali)+ '\n']
    file.write('|'.join(hasilPinjaman))

    lagi = input("\nulangi lagi (y/n): ")

    if(lagi.lower() == 'y'):
        continue

    elif(lagi.lover()== 'n') :
        break
    else:
        print("Inputnya invalid")
        break

file.close()
