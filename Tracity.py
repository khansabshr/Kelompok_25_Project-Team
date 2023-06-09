def welcome_message():
    print('    ================================================================================')
    print("\t\t\tSELAMAT DATANG DI PROGRAM TRACITY!")
    print("\tKami adalah Platform untuk membantu payment listrik Anda secara online!")
    print('''
    ================================================================================
    Tracity atau Track Your Electricity Program ini dirancang untuk membantu
    Anda melacak penggunaan listrik Anda. Dengan program ini, Anda dapat dengan
    mudah memantau konsumsi listrik Anda dan mengidentifikasi area di mana Anda
    dapat menghemat energi
    ================================================================================
    Kami menyediakan berbagai opsi pembayaran untuk kenyamanan Anda:")
    1. Prepaid
    2. Postpaid
    ================================================================================
    ''')
    print("\t\tSelamat menggunakan program Track Your Electricity!")
    print('    ================================================================================')

welcome_message()

def run():
    print('\n\n========== Track Your Electricity ==========')
    home()

def home():
    while True:
        print('[1] Masuk')
        print('[2] Daftar')
        print('[3] Keluar')
        pilih = input('Silakan pilih    :')
        if pilih == "1":
            if masuk():
                break
        elif pilih == "2":
            daftar()
        elif pilih == "3":
            keluar()
        else :
            print(f'Maaf, pilihan {pilih} tidak tersedia')
            print('Silakan coba lagi')

def daftar():
    print('\n========== Daftar Akun ==========')
    print('\nIsi data-data berikut dengan benar')
    email_daftar = input('Masukkan email yang sudah ada             :')

    with open("Daftar akun.txt","r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == email_daftar:
                print("Pendaftaran gagal. Email sudah terdaftar.")
                return

    password = input('Masukkan password 5 karakter berupa angka :')
    
    while len(password) !=5 or not password.isdigit():
        print("Password tidak memenuhi")
        password = input('Masukkan password 5 karakter berupa angka :')

    with open("Daftar akun.txt","a") as file:
        file.write(f"{email_daftar},{password}\n")


def masuk():
    print('\n========== Masuk ==========')
    print('\nSilakan Masukkan Akun Anda yang Sudah Terdaftar')
    email_login = input('Masukkan email yang sudah ada    :')
    pw_login = input('Masukkan password                :')
    with open('Daftar akun.txt', 'r') as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == email_login:
                if data[1] == pw_login:
                    print('Login berhasil')
                    return True
            else:
                print('Maaf, Email tidak terdaftar')
                masuk()
                return False
    print('Maaf, Password salah')
    return False

def keluar():
    print('Terima kasih telah menggunakan Tracity')
    exit()

run()

def home2():
    while True:
        print()
        print('[1] Pembayaran')
        print('[2] Riwayat')
        pilih = input('Silakan pilih    :')
        if pilih == '1':
            pembayaran()
        elif pilih == '2':
            tampilkan_riwayat()
        else :
            print(f'Maaf, pilihan {pilih} tidak tersedia')
            print('Silakan coba lagi')

def pembayaran():
    while True:
        print()
        print('[1] Prepaid')
        print('[2] Postpaid')
        pilih = input('Silakan pilih    :')
        if pilih == '1':
            prepaid()
        elif pilih == '2':
            postpaid()
        else :
            print(f'Maaf, pilihan {pilih} tidak tersedia')
            print('Silakan coba lagi')   
            
def tampilkan_riwayat():
    while True:
        print()
        print('[1] Riwayat Pembayaran')
        print('[2] Riwayat Pemakaian')
        pilih = input('Silakan pilih    :')
        if pilih == '1':
            riwayat_pembayaran()
        elif pilih == '2':
            riwayat_pemakaian()
        else :
            print(f'Maaf, pilihan {pilih} tidak tersedia')
            print('Silakan coba lagi')  

import datetime

def prepaid(riwayat):
     tanggal = datetime.datetime.now()
     bayar = float(input("harga"))
     riwayat.append((tanggal,nominal))
     
def riwayat_pembayaran(riwayat):
     for pembayaran in riwayat:
             with open("Daftar akun.txt","r") as file:
                  tanggal = pembayaran[0].strftime("%d-%m-%Y %H:%M:%S")
                  nominal = pembayaran[1]
                  print(f"{tanggal} - Rp{bayar}")
        
def hitung(kwh):
    return kwh*2000
        
def postpaid(riwayat):
    tanggal = datetime.datetime.now()
    kwh = float(input("Masukkan jumlah pemakaian listrik dalam kwh: "))
    riwayat.append((tanggal, kwh))
    total = hitung(kwh)
    email = input("Masukkan email login:   ")
    print("Email: ", email)
    print("Total tagihan Anda sebesar Rp", total)
    bayar = float(input("Masukan jumlah pembayaran Anda: "))
    sisa_tagihan = total - bayar
    print("Sisa tagihan Anda sebesar Rp", sisa_tagihan)
    with open('Daftar akun.txt', 'a') as file:
        file.write(f"{kwh},{total}\n")
        file.write(f"{tanggal}, {bayar}, {sisa_tagihan}\n")

def riwayat_pemakaian(riwayat):
     for pemakaian in riwayat:
            with open("Daftar akun.txt","r") as file:
                tanggal = pembayaran[0].strftime("%d-%m-%Y %H:%M:%S")
                kwh = float(input("Masukkan jumlah pemakaian listrik dalam kwh: "))
                print(f"{tanggal} - {kwh}kwh")
        

def home3():
    while True:
        print('Apakah Anda ingin melakukan pembayaran?')
        print('[1] Ya')
        print('[2] Tidak')
        pilih = input('Silakan pilih    :')
        if pilih == "1":
            if ya():
                print(int(input("Masukkan nomor kartu kredit Anda: ")))
                print("Pembayaran Anda sedang diproses...")
                print("Pembayaran dengan kartu kredit berhasil!")
        elif pilih == "2":
            keluar()
        else :
            print(f'Maaf, pilihan {pilih} tidak tersedia')
            print('Silakan coba lagi')
