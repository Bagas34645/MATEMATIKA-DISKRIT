def bin_to_dec(bin_str):
    return int(bin_str, 2)

def dec_to_bin(dec_num):
    return bin(dec_num)[2:]

def dec_to_hex(dec_num):
    return hex(dec_num)[2:]

def hex_to_dec(hex_str):
    return int(hex_str, 16)

def bin_to_hex(bin_str):
    dec_num = bin_to_dec(bin_str)
    return dec_to_hex(dec_num)

def hex_to_bin(hex_str):
    dec_num = hex_to_dec(hex_str)
    return dec_to_bin(dec_num)

def main():
    while True:
        print("\n1. Biner ke Desimal")
        print("2. Desimal ke Biner")
        print("3. Desimal ke Heksadesimal")
        print("4. Heksadesimal ke Desimal")
        print("5. Biner ke Heksadesimal")
        print("6. Heksadesimal ke Biner")
        print("0. Keluar")
        
        choice = input("\nMasukkan pilihan Anda: ")
        
        if choice == '0':
            print("Terima kasih, sampai jumpa!")
            break
        
        elif choice == '1':
            bin_str = input("Masukkan bilangan biner: ")
            print("Hasil konversi:", bin_to_dec(bin_str))
        
        elif choice == '2':
            dec_num = int(input("Masukkan bilangan desimal: "))
            print("Hasil konversi:", dec_to_bin(dec_num))
        
        elif choice == '3':
            dec_num = int(input("Masukkan bilangan desimal: "))
            print("Hasil konversi:", dec_to_hex(dec_num))
        
        elif choice == '4':
            hex_str = input("Masukkan bilangan heksadesimal: ")
            print("Hasil konversi:", hex_to_dec(hex_str))
        
        elif choice == '5':
            bin_str = input("Masukkan bilangan biner: ")
            print("Hasil konversi:", bin_to_hex(bin_str))
        
        elif choice == '6':
            hex_str = input("Masukkan bilangan heksadesimal: ")
            print("Hasil konversi:", hex_to_bin(hex_str))
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()