#variabel
nilai_tugas=int(input("Nilai Tugas="))
nilai_uts=int(input("Nilai UTS="))
nilai_uas=int (input("Nilai UAS="))

nilai_total=nilai_tugas + nilai_uts + nilai_uas
print("Total Nilai yang didapatkan =", nilai_total)
nilai_rata=(nilai_tugas + nilai_uts + nilai_uas)/3
print("Nilai Rata-Rata Adalah=", nilai_rata)

if nilai_rata >=95:
    print("Mendapatkan Predikat=A")
elif nilai_rata >=90:
    print("Mendapatkan Prdiksi=B+")
elif nilai_rata >=85:
    print("Mendapatkan Prdiksi=B")
elif nilai_rata >=80:
    print("Mendapatkan Prdiksi=B-")
elif nilai_rata >=75:
    print("Mendapatkan Prdiksi=C+")
elif nilai_rata >=70:
    print("Mendapatkan Prdiksi=C")
elif nilai_rata >=65:
    print("Mendapatkan Prdiksi=C-")
elif nilai_rata >=60:
    print("Mendapatkan Prdiksi=D")

else:
    print("Silahkan Anda Coba Lagi")
