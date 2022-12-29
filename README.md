# Praktikum_12
## Apa Itu String?
String dalam bahasa pemrograman Python disebut sebagai kumpulan karakter yang dikelilingi oleh tanda kutip tunggal, tanda kutip ganda bahkan tanda kutip tiga. Komputer tidak memahami karakter. Secara internal, tipe string ini menyimpan karakter yang dimanipulasi sebagai kombinasi dari 0 dan 1. Setiap karakter dikodekan dalam karakter ASCII atau Unicode. Dapat disimpulkan bahwa string Python juga disebut kumpulan karakter unicode. Berikut adalah contoh dari string pada Python.
## Fungsi String
String dalam pyhton juga memiliki banyak fungsi antara lain :
1. Escape Karakter/Karakter Escape Python
tabel dari daftar karakter escape atau karakter non-printable yang dapat diwakili/ditulis dengan awalan notasi backslash contoh, \n,\s,\nnn,\r.
2. Operator Special String Python
Asumsikan variabel string adalah 'Belajar' dan variabel b adalah 'Python', lalu dibawah ini adalah operator yang bisa dipakai pada kedua string di variabel tersebut. a = "Belajar" b = "Python".
3. Operator Format String Python
Salah satu fitur Python yang paling keren adalah format string operator %. Operator ini unik untuk string dan membuat paket memiliki fungsi dari keluarga printf C () C. berikut adalah contoh sederhananya : print ("My name is %s and weight is %d kg!" % ('Zara', 21)).
4. String Unicode Python 
Pada Python 3, semua string diwakili dalam Unicode. Sedangkan pada Python 2 disimpan secara internal sebagai 8-bit ASCII, maka diperlukanlampiran 'u' untuk membuatnya menjadi Unicode. Tetapi hal ini tidak lagi diperlukan sekarang.
## Source code
![carbon(11)](https://user-images.githubusercontent.com/115929351/209909318-154db88f-b675-4308-a463-838fbc2d93f0.png)
## Penjelasan Latihan 1
Pada praktikun string kali ini saya membuat latihan tentang mencoba berbagai macam method yang ada pada string mulai dari menampilkan index sampai mengubah huruf besar dan kecil.

1. Menghitung jumlah karakter, disini saya menggunakan method len, untuk menghitung jumlah karakter yang saya buat 
2. Mengambil karakter terakhir, saya memakai indek yang berkurang 1
3. Menampilkan karakter indek ke-2 sampai ke-4 (llo), saya memasukkan variabel dan memakai indek untuk mengambil karakter 'llo', yaitu indek dimulai dari 0, maka indek ke-2 ialah 'l', ke=3 ialah 'l', ke-4 'o'.
4. Menghilangkan spasi pada teks teresebut (HelloWord), saya menghilangkan spasi pada teks dengan menggunakan method replace (" ","") 
5. Mengubah teks menjadi huruf besar (HELLO WORD), saya memasukkan variabel lalu method upper, untuk membuat karakter menjadi huruf besar semua.
6. Mengubah teks menjadi huruf kecil (hello word), saya memasukkan variabel lalu method lower berlawanan dengan upper, lower membuat teks menjadi huruf kecil semua.
7. Mengganti karakter huruf H dengan huruf J (Jello Word, saya memakai method replace dengan cara memasukkan variabel lalu replace ("H", "J") maka huruf H akan berganti ke huruf J

## Penjelasan Latihan 2
1. Menampilkan umur menggunakan method format, saya membuat terlebih dahulu variabel umur yang akan dimasukkan ke dalam karakter, kemudian membuat variabel txt yang berisi string menampilkan teks "Hello, nama saya John, saya berumur {0} tahun", saya membuat dict 0
2. Kemudian saya membuat print menggunakan method format lalu variabel umur untuk menampilkan umur.

## Output Latihan 1 dan Latihan 2
![iji](https://user-images.githubusercontent.com/115929351/209910621-3cf7d663-486f-48a5-aefe-5aacf1205f18.png)
Berikut adalah hasil output dari latihan 1 dan latihan 2, ternyata string mempunyai banyak method yang dapat digunakan maupun diaplikasikan.

# Thanks for Read Everyone
