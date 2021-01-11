#chapter 11
#no 03

from datetime import *

def getLate(harikembali) :
    hariIni = datetime.date(datetime.now())
    hariKembali = datetime.strptime (harikembali, "%Y-%m-%d").date()
    return int((hariIni - hariKembali).days)

file = open("hasilPinjaman.txt", "r")

isiFile = file.readlines()
kode = input ("Masukkan Kode Member  :")

for x in range (len(isiFile)):
    if(kode in isiFile[x]) :

        diSplit = isiFile[x].split('|')
        status = 'ada'
        break

    else :
        status = 'tidak ada'
        continue

if(status == 'ada') :

    maksPinjam = diSplit[4].rstrip('\n')
    late = getLate(maksPinjam)

    if(late <= 0) :
        textLate    = "Tidak Terlambat"
        denda       = "Tidak Di Denda"

    elif(late > 0) :
        textLate    = str(late) + " hari "
        denda       = "Rp " + str(late*2000)
        
    print("\nData Peminjaman Buku")
    print("Kode Member              : ", diSplit[0])
    print("Nama Member              : ", diSplit[1])
    print("Judul Buku               : ", diSplit[2])
    print ("Tanggal Mulai Peminjaman: ", diSplit[3])
    print ("Tanggal Maks Peminjaman : ", maksPinjam)
    print ("Tanggal Pengembalian    : ", datetime.date(datetime.now()))
    print("Terlambat                : ", textLate)
    print ("Denda                    : ", denda)

else :
    print("Data Peminjaman Tidak Dapat Ditemukan")

