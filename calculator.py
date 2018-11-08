print ("====================")
print ("Simple Calculator")
print ("By : mhfgeek")
print ("====================")
print ("1. Pertambahan")
print ("2. Pengurangan")
print ("3. Perkalian")
print ("4. Pembagian")
pilih = input("Pilih no 1-4 = ")
if pilih=="1":
    print ("==============")
    print ("Pertambahan")
    print ("==============")
    x = int(input("Masukan Angka Pertama ="))
    z = int(input("Masukan Angka Kedua ="))
    hasil = x+z
    print ("Hasilnya adalah =",  hasil)
elif pilih=="2":
    print ("==============")
    print ("Pengurangan")
    print ("==============")
    x = int(input("Masukan Angka Pertama ="))
    z = int(input("Masukan Angka Kedua ="))
    hasil = x-z
    print ("Hasilnya adalah =",  hasil)
elif pilih=="3":
    print ("==============")
    print ("Perkalian")
    print ("==============")
    x = int(input("Masukan Angka Pertama ="))
    z = int(input("Masukan Angka Kedua ="))
    hasil = x*z
    print ("Hasilnya adalah =",  hasil)
elif pilih=="4":
    print ("==============")
    print ("Pembagian")
    print ("==============")
    x = int(input("Masukan Angka Pertama ="))
    z = int(input("Masukan Angka Kedua ="))
    hasil = x/z
    print ("Hasilnya adalah =",  hasil)
else:
   print("Tidak ada GBLK!!!!") 

