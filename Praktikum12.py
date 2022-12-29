print("___________ Khaerunnisa Isnaeni Lestari _____________")
print("_________________ Kelas TI 22 C1 ____________________")
print("__________________ 312210008 ________________________\n")

print("LATIHAN 1")
txt = 'Hello Word'
print(f"Text = {txt}")
print(f"Type class = {type(txt)}")
print(f"Menghitung jumlah karakter = {len(txt)}")

a = txt[2:6]
print("Menampilkan karakter index ke-2 sampai ke-6 =", a)

b = txt.replace(" ", "")
print("Menghilangkan spasi pada teks =",b)

c = txt.upper()
print("Mengubah karakter menjadi huruf besar =", c)

d = txt.lower()
print("Mengubah karakter menjadi huruf kecil =", d)

e = txt.replace("H", "J")
print("Mengubah karakter huruf H dengan J =",e)

print("\n")

print("LATIHAN 2")
umur = 24
txt = "Hello, nama saya John, dan umur saya adalah {0} tahun"
print(txt.format(umur))
