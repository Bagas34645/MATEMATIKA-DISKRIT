def tambah(a, b):
    """Fungsi untuk menambahkan dua bilangan."""
    return a + b

def kurang(a, b):
    """Fungsi untuk mengurangi dua bilangan."""
    return a - b

def kali(a, b):
    """Fungsi untuk mengalikan dua bilangan."""
    return a * b

def bagi(a, b):
    """Fungsi untuk membagi dua bilangan."""
    return a / b

a=0
b=0

while(True):
    # pilihan = pilih_menu()
    print("1. Tambah (+)")
    print("2. Kurang (-)")
    print("3. Kali (X)")
    print("4. Bagi (÷)")

    pilihan = input("Masukan Pilihan: ")

    if pilihan == '1':
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        hasil = tambah(a, b)
        print("Hasil penambahan:", hasil)
    elif pilihan == '2':
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        hasil = kurang(a, b)
        print("Hasil pengurangan:", hasil)
    elif pilihan == '3':
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        hasil = kali(a, b)
        print("Hasil perkalian:", hasil)
    elif pilihan == '4':
        a = int(input("Masukkan nilai a: "))
        b = int(input("Masukkan nilai b: "))
        hasil = bagi(a, b)
        print("Hasil perkalian:", hasil)
    else:
        print("Pilihan tidak valid")
    
    apakah_selesai = input("Apakah Selesai (y/n)? ")
    if apakah_selesai == "y" or apakah_selesai == "Y":
        break
    
print("Program Berakhir, Terima Kasiih")