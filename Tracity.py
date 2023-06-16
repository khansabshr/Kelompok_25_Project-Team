import Modul
from Modul import input_email, password, input_yn, fonts, input_kredit, nominal
import matplotlib.pyplot as plt

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
    print('''Tracity atau Track Your Electricity Program ini dirancang untuk membantu
Anda melacak penggunaan listrik Anda. Dengan program ini, Anda dapat dengan
mudah memantau konsumsi listrik Anda dan mengidentifikasi area di mana Anda
dapat menghemat energi''')
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
            pilih = input('Silakan pilih    :')
            option = int(pilih)
            if option == 1:
                masuk()
                break
            elif option == 2:
                daftar()
            elif option == 3:
                keluar()
            else:
                raise ValueError
        except ValueError:
            print(f"Maaf, pilihan {pilih} tidak tersedia.")
            
def daftar():
    print('\n========== Daftar Akun ==========')
    print('\nIsi data-data berikut dengan benar')
    email_daftar = input_email('Masukkan email                        :')
    with open("Daftar akun.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 2 and data[0] == email_daftar:
                print("Pendaftaran gagal. Email sudah terdaftar.")
                return
    pw_daftar = password('Masukkan password (5 digit)           :')
    with open("Daftar akun.txt", "a") as file:
        file.write(f"{email_daftar},{pw_daftar}\n")
    print('Akun berhasil didaftarkan\n')
    home()
    
def keluar():
    print('Terima kasih telah menggunakan Tracity')
    exit()

def masuk():
    print('\n========== Masuk  ==========')
    print('Silakan Masukkan Akun Anda yang Sudah Terdaftar')
    global email_login
    email_login = input_email('Masukkan email yang terdaftar    : ')
    coba = 0
    while True:
        with open("Daftar akun.txt", "r") as file:
            for line in file:
                data = line.strip().split(",")
                if len(data) == 2 and data[0] == email_login:
                    while coba < 3:
                        pw_login = password("Masukkan password (5 digit)      : ")
                        if data[1] == pw_login:
                            print("Login berhasil")
                            home2()                                                             #TAMBAHANNNNSSS
                            return True
                        else:
                            coba += 1
                            print("Password salah.")
                    print("Gagal login. Terlalu banyak percobaan.\n")
                    home()
                    return False
            print('Email tidak terdaftar. Silakan coba lagi.\n')
            email_login = input_email('Masukkan email yang terdaftar    : ')
            
def home2():
    while True:
        print()
        print(f"{fonts('[1]', color='pink')} Pembayaran")
        print(f"{fonts('[2]', color='pink')} Riwayat")
        try:
            pilih = input('Silakan pilih    : ')
            option = int(pilih)
            if option == 1:
                pembayaran()                                            
            elif option == 2:
                riwayat()
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
        try:
            pilih = input('Silakan pilih    : ')
            option = int(pilih)
            if option == 1:
                prepaid()
            elif option == 2:                                       
                postpaid()
            else :
                raise ValueError
        except ValueError:
                print(f'Maaf, pilihan {pilih} tidak tersedia')
                print('Silakan coba lagi\n')  
            
def riwayat():
    while True:
        print('\n========== Riwayat ==========')
        print(f"{fonts('[1]', color='pink')} Riwayat Pembayaran")
        print(f"{fonts('[2]', color='pink')} Riwayat Pemakaian")
        pilih = input('Silakan pilih    :')
        if pilih == "1":
            riwayat_pembayaran()
        elif pilih == "2":
            riwayat_pemakaian()
        else :
            print(f'Maaf, pilihan {pilih} tidak tersedia')
            print('Silakan coba lagi')  

import datetime

def prepaid():
    tanggal = datetime.date.today()
    email = email_login
    pulsa_awal = nominal("Masukkan pulsa awal     : ")
    token_awal = pulsa_awal/2000
    print("Token awal Anda: ", token_awal)
    pemakaian_listrik = nominal("Masukkan jumlah pemakaian listrik dalam kWh     : ")
    kwh = 0
    bayar = 0
    if pemakaian_listrik <= token_awal:
        kwh = token_awal - pemakaian_listrik
        print("Sisa token Anda: ", kwh)
        pembayaran = input_yn("Apakah Anda ingin melakukan pembayaran? (Y/N)   : ") 
        if pembayaran == "y":                                                       
            nomor_kartu_kredit = input_kredit("Masukkan nomor kartu kredit : ")    
            bayar = nominal('Masukkan nominal pembayaran : ')
            token_sekarang = (bayar/2000) + kwh
            print(fonts("Pembayaran Anda sedang diproses...", color='yellow', style='italic'))
            print("Pembayaran kartu kredit berhasil.")
            print("Token anda sekarang: ",token_sekarang)                           
            print("Terima kasih telah menggunakan Tracity.")
        else:
            token_sekarang = kwh
            print("Terima kasih telah menggunakan Tracity.")
    else:
        print("Pulsa anda tidak mencukupi.")
        pembayaran = input_yn("Apakah Anda ingin melakukan pembayaran? (Y/N)   : ") 
        if pembayaran == "y":                                                       
            nomor_kartu_kredit = input_kredit("Masukkan nomor kartu kredit : ")     
            bayar = nominal('Masukkan nominal pembayaran : ')
            token_sekarang = (bayar/2000) + kwh
            print(fonts("Pembayaran Anda sedang diproses...", color='yellow', style='italic'))
            print("Pembayaran kartu kredit berhasil.")
            print("Token anda sekarang: ",token_sekarang)                           
            print("Terima kasih telah menggunakan Tracity.")
        else:
            print("Terima kasih telah menggunakan Tracity.")
    with open('Prepaid.txt', 'a') as file:
        file.write(f"\n{email},{tanggal},{bayar},{token_sekarang}")
    exit()
        
def postpaid():
    tanggal = datetime.date.today()
    email = email_login
    kwh = nominal("Masukkan jumlah pemakaian listrik dalam kwh     : ")
    total = kwh * 2000
    print("Total tagihan Anda sebesar Rp", total)
    pembayaran = input_yn("Apakah Anda ingin melakukan pembayaran? (Y/N)   : ")    
    if pembayaran == "y":                                                          
        nomor_kartu_kredit = input_kredit("Masukkan nomor kartu kredit : ")        
        bayar = nominal('Masukkan nominal pembayaran : ')
        sisa_tagihan = total - bayar
        print(fonts("Pembayaran Anda sedang diproses...", color='yellow', style='italic')) 
        print("Pembayaran kartu kredit berhasil.")
    else:
        print("Total tagihan Anda sebesar Rp", total)
        print("Terima kasih telah menggunakan Tracity.")
    if sisa_tagihan <= 0 :
        print("Tagihan Anda sudah terbayar penuh")
        print("Terima kasih telah menggunakan Tracity.")
    else:
        print("Sisa tagihan Anda sebesar Rp", sisa_tagihan)
        pembayaran = input_yn("Apakah Anda ingin melakukan pembayaran? (Y/N)   : ") 
        if pembayaran == "y":                                                       
            nomor_kartu_kredit = input_kredit("Masukkan nomor kartu kredit : ")     
            bayar = nominal('Masukkan nominal pembayaran : ')
            sisa_tagihan = total - bayar
            print(fonts("Pembayaran Anda sedang diproses...", color='yellow', style='italic'))  
            print("Pembayaran kartu kredit berhasil.")
            print("Terima kasih telah menggunakan Tracity.")
        else:
            print("Terima kasih telah menggunakan Tracity.")
    with open('Postpaid.txt', 'a') as file:
        file.write(f"\n{email},{tanggal},{total},{kwh}")

def riwayat_pemakaian():
    a = []
    b = []
    with open("Prepaid.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            a.append(data[1])
            b.append(int(data[3]))
    plt.plot(a, b)
    plt.xlabel("Tanggal")
    plt.ylabel("Kwh")
    plt.title("Grafik Pemakaian Listrik Prepaid")
    plt.show()
    c = []
    d = []
    with open("Postpaid.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")
            c.append(data[1])
            d.append(int(data[3]))
    plt.plot(c, d)
    plt.xlabel("Tanggal")
    plt.ylabel("Kwh")
    plt.title("Grafik Pemakaian Listrik Postpaid")
    plt.show()

def riwayat_pembayaran():
    data = []
    with open('Prepaid.txt', 'r') as file:
        for line in file:
            line_data = line.strip().split(',')
            data.append(line_data)
    tanggal = []
    pembayaran = []
    for item in data:
        tanggal.append(item[1][5:10])
        pembayaran.append(float(item[2]))
    plt.plot(tanggal, pembayaran)
    plt.title("Riwayat Pembayaran")
    plt.xlabel("Tanggal")
    plt.ylabel("Pembayaran")
    plt.show()


run()
