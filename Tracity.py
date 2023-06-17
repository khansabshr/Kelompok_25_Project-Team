import Modul
from Modul import input_email, password, input_yn, fonts, input_kredit, nominal, pulsa
import matplotlib.pyplot as plt
import time
import os
import datetime

def welcome_message():
    print()
    garis = fonts('='*80, color='blue',style='bold')
    text1 = fonts("SELAMAT DATANG DI PROGRAM TRACITY!", color='yellow', style='bold')
    text2 = ('Kami adalah Platform untuk membantu payment listrik Anda secara online!')
    text3 = fonts('Selamat menggunakan program Track Your Electricity!', color='yellow')
    print(fonts(garis.center(80)))
    print(fonts(text1.center(90)))                                                      
    print(fonts(text2.center(80)))
    print(fonts(garis.center(80)))
    print('''Tracity atau Track Your Electricity ini telah dirancang khusus untuk 
membantu Anda melacak penggunaan listrik Anda. Dengan program ini, Anda dapat dengan
mudah memantau konsumsi listrik Anda dan mengidentifikasi area di mana Anda dapat
melakukan penghematan energi''')
    print(fonts(garis.center(80)))
    print('''Kami menyediakan berbagai opsi pembayaran untuk kenyamanan Anda dan riwayat
yang bisa diakses kapan saja!
1. Prepaid
2. Postpaid''')
    print(fonts(garis.center(80)))
    print(fonts(text3.center(90)))
    print(fonts(garis.center(80)))

def run():
    welcome_message()
    print('\n\n========== Track Your Electricity ==========')
    home()

def home():
    while True:
        print(f"{fonts('[1]', color='pink')} Masuk")
        print(f"{fonts('[2]', color='pink')} Daftar")
        print(f"{fonts('[3]', color='pink')} Keluar")  
        try:
            pilih = input('Silakan pilih    : ')
            option = int(pilih)
            if option == 1:
                masuk()
                break
            elif option == 2:
                daftar()
            elif option == 3:
                print("Terima kasih telah menggunakan Tracity!")
                exit()
            else:
                raise ValueError
        except ValueError:
            print(f"Maaf, pilihan {pilih} tidak tersedia.")
            print('Silakan coba lagi\n')
            
def daftar():
    print('\n========== Daftar Akun ==========')
    print('Isi data-data berikut dengan benar')
    email_daftar = input_email('Masukkan email                        : ')
    with open("Daftar akun.txt","r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data)==2 and data[0] == email_daftar:
                print("Pendaftaran gagal. Email sudah terdaftar.")
                return
    pw_daftar = password('Masukkan password (5 digit)           : ')
    with open("Daftar akun.txt","a") as file:
        file.write(f"\n{email_daftar},{pw_daftar}")
    print('Akun berhasil didaftarkan\n') 
    home()

def masuk():
    print('\n========== Masuk  ==========')
    print('Silakan Masukkan Akun Anda yang Sudah Terdaftar')
    global email_login
    email_login = input_email('Masukkan email yang terdaftar    : ')
    with open("Daftar akun.txt", "r") as file:
        email_terdaftar = False
        for line in file:
            data = line.strip().split(",")
            if len(data) == 2 and data[0] == email_login:
                email_terdaftar = True
                break
    if email_terdaftar:
        coba = 0
        while coba < 3:
            password = input("Masukkan password (5 digit)      : ")
            with open("Daftar akun.txt", "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 2 and data[0] == email_login and data[1] == password:
                        print("Login berhasil!")
                        time.sleep(2)
                        home2()
            coba += 1
            print("Password salah. Silakan coba lagi.")
        print("\nGagal login. Terlalu banyak percobaan.")
    else:
        print("Email belum terdaftar.\n")
    home()
    
def home2():
    while True:
        print('\n========== Transaksi  ==========')
        print(f"{fonts('[1]', color='pink')} Pembayaran")
        print(f"{fonts('[2]', color='pink')} Riwayat")
        print(fonts('Tekan enter untuk kembali ke halaman utama', color='yellow', style='italic'))
        try:
            pilih = input('Silakan pilih    : ')
            if pilih == '1':
                pembayaran()                                            
            elif pilih == '2':
                riwayat()
            elif pilih == '':
                os.system('cls')
                time.sleep(2)
                home()
            else :
                raise ValueError
        except ValueError:
            print(f"Maaf, pilihan {pilih} tidak tersedia.")
            print('Silakan coba lagi\n')

def pembayaran():
    while True:
        print('\n==========   Pembayaran   ==========')
        print(f"{fonts('[1]', color='pink')} Prepaid")
        print(f"{fonts('[2]', color='pink')} Postpaid")
        print(fonts('Tekan enter untuk kembali ke page sebelumnya', color='yellow', style='italic'))
        try:
            pilih = input('Silakan pilih    : ')
            if pilih == '1':
                prepaid()                                            
            elif pilih == '2':
                postpaid()
            elif pilih == '':
                os.system('cls')
                time.sleep(2)
                home2()
            else :
                raise ValueError
        except ValueError:
            print(f"Maaf, pilihan {pilih} tidak tersedia.")
            print('Silakan coba lagi\n')  
            
def riwayat():
    while True:
        print('\n========== Riwayat ==========')
        print(f"{fonts('[1]', color='pink')} Riwayat Prepaid")
        print(f"{fonts('[2]', color='pink')} Riwayat Postpaid")
        print(fonts('Tekan enter untuk kembali ke halaman sebelumnya', color='yellow', style='italic'))
        try:
            pilih = input('Silakan pilih    : ')
            if pilih == '1':
                riwayat_prepaid()                                            
            elif pilih == '2':
                riwayat_postpaid()
            elif pilih == '':
                os.system('cls')
                time.sleep(2)
                home2()
            else :
                raise ValueError
        except ValueError:
            print(f"Maaf, pilihan {pilih} tidak tersedia.")
            print('Silakan coba lagi\n')   

def prepaid():
    email = email_login
    tanggal = datetime.date.today()
    pulsa_awal = pulsa("Masukkan pulsa awal     : ")
    token_awal = pulsa_awal/2000
    print("Token awal Anda         : ", token_awal)
    pemakaian_listrik = nominal("Masukkan jumlah pemakaian listrik dalam kWh     : ")
    bayar = 0
    sisa_token = 0 
    while pemakaian_listrik > token_awal:
        print(f"Pulsa anda tidak mencukupi. Pembelian maksimal untuk {token_awal} kwh\n")
        time.sleep(1)
        pemakaian_listrik = nominal("Masukkan jumlah pemakaian listrik dalam kWh     : ")
    sisa_token = token_awal - pemakaian_listrik
    print("Sisa token Anda     :", sisa_token)
    pembayaran = input_yn("Apakah Anda ingin melakukan pembelian token? (Y/N): ")
    if pembayaran == "y":
        nomor_kartu_kredit = input_kredit("Masukkan nomor kartu kredit: ")
        bayar = pulsa('Masukkan nominal pembayaran: ')
        token_sekarang = (bayar/2000) + sisa_token
        print(fonts("\nPembayaran Anda sedang diproses...", color='yellow', style='italic'))
        time.sleep(2)
        print(f"Pembayaran kartu kredit {fonts('berhasil', color='blue')}")
        print("Token anda sekarang :", token_sekarang)
        ask = input(fonts('Tekan enter untuk kembali ke halaman utama', color='yellow', style='italic'))
        if ask == '':
            print(fonts("Kembali ke halaman utama...", color='yellow', style='italic'))
            time.sleep(2)
            os.system('cls')
            home2()
    else:
        token_sekarang = sisa_token
        print('Token anda sekarang :', token_sekarang)
        ask = input(fonts('Tekan enter untuk kembali ke halaman utama', color='yellow', style='italic'))
        if ask == '':
            print(fonts("Kembali ke halaman utama...", color='yellow', style='italic'))
            time.sleep(2)
            os.system('cls')
            home2()
    with open('Prepaid.txt', 'a') as file:
        file.write(f"\n{email},{tanggal},{bayar},{token_sekarang}")
    exit()

sisa_tagihan = 0

def postpaid():
    email = email_login
    global sisa_tagihan
    tanggal = datetime.date.today()
    tagihan = sisa_tagihan
    if tagihan > 0:
        print('=' * 30)
        print('Tagihan Anda Rp', tagihan)
        print('=' * 30)
    kwh = nominal("\nMasukkan jumlah pemakaian listrik dalam kwh     : ")
    total = kwh * 2000
    if tagihan > 0:
        total += tagihan
    bayar = 0
    print('Sisa tagihan sebelumnya    Rp', sisa_tagihan)
    print(fonts(f"Total tagihan Anda         Rp {total}", style='underline'))
    pembayaran = input_yn("Apakah Anda ingin melakukan pembayaran? (Y/N)   : ")    
    if pembayaran == "y":                                                          
        nomor_kartu_kredit = input_kredit("Masukkan nomor kartu kredit : ")        
        minimal = total*(15/100)
        bayar = nominal('Masukkan nominal pembayaran : ')
        while bayar < minimal or bayar > total:
            print(f"Input tidak valid! Nominal minimal Rp{minimal} maksimal Rp{total}\n")
            time.sleep(1)
            bayar = nominal('Masukkan nominal pembayaran : ')
        sisa_tagihan = total - bayar
        print(fonts("\nPembayaran Anda sedang diproses...", color='yellow', style='italic'))
        time.sleep(2)
        print(f"Pembayaran kartu kredit {fonts('berhasil', color='blue')}")
        if sisa_tagihan <= 0 :
            print("Tagihan Anda sudah terbayar penuh")
            ask = input(fonts('Tekan enter untuk kembali ke halaman utama', color='yellow', style='italic'))
            if ask == '':
                print(fonts("Kembali ke halaman utama...", color='yellow', style='italic'))
                time.sleep(2)
                os.system('cls')
                home2()
        else:
            print("Sisa tagihan Anda sebesar Rp", sisa_tagihan)
            ask = input(fonts('Tekan enter untuk kembali ke halaman utama', color='yellow', style='italic'))
            if ask == '':
                print(fonts("Kembali ke halaman utama...", color='yellow', style='italic'))
                time.sleep(2)
                os.system('cls')
                home2()
    else:
        print("Sisa tagihan Anda sebesar Rp", total)
        ask = input(fonts('Tekan enter untuk kembali ke halaman utama', color='yellow', style='italic'))
        if ask == '':
            print(fonts("Kembali ke halaman utama...", color='yellow', style='italic'))
            time.sleep(2)
            os.system('cls')
            home2()
    with open('Postpaid.txt', 'a') as file:
        file.write(f"\n{email},{tanggal},{total},{kwh}")

def riwayat_prepaid():
    email = email_login
    data1 = []
    with open('Prepaid.txt', 'r') as file:
        for line in file:
            line_data = line.strip().split(',')
            data1.append(line_data)
    tanggal = []
    pembayaran = []
    for item in data1:
        if item[0] == email:
            tanggal.append(item[1][5:10])
            pembayaran.append(float(item[2]))
    plt.subplot(1, 2, 1)
    plt.plot(tanggal, pembayaran)
    plt.title("Riwayat Pembayaran (prepaid)")
    plt.xlabel("Tanggal")
    plt.ylabel("Pembayaran (dalam rupiah)")
    plt.show()
  
    data2 = []
    with open('Prepaid.txt', 'r') as file:
        for line in file:
            line_data = line.strip().split(',')
            data2.append(line_data)
    tanggal2 = []
    pemakaian = []
    for item in data2:
        if item[0] == email:
            tanggal2.append(item[1][5:10])
            pemakaian.append(float(item[3]))
    plt.subplot(1, 2, 2)
    plt.plot(tanggal2, pemakaian)
    plt.title("Riwayat Pemakaian (prepaid)")
    plt.xlabel("Tanggal")
    plt.ylabel("Pemakaian (dalam kwh)")
    plt.tight_layout()
    plt.show()
    
def riwayat_postpaid():
    email = email_login
    data1 = []
    with open('Postpaid.txt', 'r') as file:
        for line in file:
            line_data = line.strip().split(',')
            data1.append(line_data)
    tanggal = []
    pembayaran = []
    for item in data1:
        if item[0] == email:
            tanggal.append(item[1][5:10])
            pembayaran.append(float(item[2]))
    plt.subplot(1, 2, 1)
    plt.plot(tanggal, pembayaran)
    plt.title("Riwayat Pembayaran (postpaid)")
    plt.xlabel("Tanggal")
    plt.ylabel("Pembayaran (dalam rupiah)")
    plt.show()
  
    data2 = []
    with open('Postpaid.txt', 'r') as file:
        for line in file:
            line_data = line.strip().split(',')
            data2.append(line_data)
    tanggal2 = []
    pemakaian = []
    for item in data2:
        if item[0] == email:
            tanggal2.append(item[1][5:10])
            pemakaian.append(float(item[3]))
    plt.subplot(1, 2, 2)
    plt.plot(tanggal2, pemakaian)
    plt.title("Riwayat Pemakaian (postpaid)")
    plt.xlabel("Tanggal")
    plt.ylabel("Pemakaian (dalam kwh)")
    plt.tight_layout()
    plt.show()


run()
