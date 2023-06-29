from Modul import input_email, password, input_yn, fonts, input_kredit, nominal, pulsa, kuitansi_prepaid, kuitansi_postpaid, transaksi_postpaid, transaksi_prepaid
import matplotlib.pyplot as plt
import time
import os
import sys
import msvcrt
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
    print('''Tracity atau Track Your Electricity ini telah dirancang khusus untuk membantu
Anda melacak penggunaan listrik Anda. Dengan program ini, Anda dapat dengan
mudah memantau konsumsi listrik Anda dan mengidentifikasi area di mana Anda
dapat melakukan penghematan energi''')
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
        print(f"{fonts('[1]', color='pink')} Masuk  (login)")
        print(f"{fonts('[2]', color='pink')} Daftar (sign up)")
        print(fonts('Tekan Esc untuk keluar dari program', color='yellow', style='italic'))
        print('Silakan pilih    : ')
        try:
            while True:
                key = ord(msvcrt.getch())
                if key == 27: 
                    print('Terimakasih telah menggunakan Tracity!')
                    exit()
                elif key == 49:  
                    masuk()
                    break
                elif key == 50:  
                    daftar()
        except ValueError:
            print("Maaf, input tidak valid. Silakan coba lagi.\n")
            
def daftar():
    print('\n===============  Daftar Akun ===============')
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
    print('\n==================  Masuk ==================')
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

def logout():
    print('Anda berhasil logout.\n')
    time.sleep(2)
    print('\n\n========== Track Your Electricity ==========')
    home()

def home2():
    while True:
        print('\n================  Transaksi  ===============')
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
        print('\n==============   Pembayaran   ==============')
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
        print('\n=================  Riwayat  ================')
        print(f"{fonts('[1]', color='pink')} Riwayat Prepaid")
        print(f"{fonts('[2]', color='pink')} Riwayat Postpaid")
        print(fonts('Tekan Enter untuk kembali ke halaman utama\nTekan Esc untuk logout', color='yellow', style='italic'))
        print('Silakan pilih    : ')
        try:
            while True:
                key = ord(msvcrt.getch())
                if key == 49:
                    riwayat_prepaid()                                            
                elif key == 50:
                    riwayat_postpaid()
                elif key == 13:  
                    print(fonts("Kembali ke halaman utama...", color='yellow', style='italic'))
                    time.sleep(2)
                    os.system('cls')
                    home2()
                elif key == 27:  
                    logout()
        except ValueError:
            print("Maaf, input tidak valid")
            print('Silakan coba lagi\n')   

def prepaid():
    email = email_login
    tanggal = datetime.date.today()
    pulsa_awal = pulsa("Masukkan pulsa awal     : ")
    token_awal = pulsa_awal / 2000
    print("Token awal Anda         : ", token_awal)
    pemakaian_listrik = nominal("Masukkan jumlah pemakaian listrik dalam kWh     : ")
    bayar = 0
    sisa_token = 0
    while pemakaian_listrik > token_awal:
        print(f"Pulsa anda tidak mencukupi. Pembelian maksimal untuk {token_awal} kWh\n")
        time.sleep(1)
        pemakaian_listrik = nominal("Masukkan jumlah pemakaian listrik dalam kWh     : ")
    sisa_token = token_awal - pemakaian_listrik
    print("Sisa token Anda     :", sisa_token)
    token_options = {
        20_000: 15,
        50_000: 30,
        100_000: 60,
        250_000: 120,
        500_000: 240,
        1_000_000: 480,
        5_000_000: 960,
        10_000_000: 1920,
    }
    pembayaran = input_yn("Apakah Anda ingin melakukan pembelian token? (Y/N): ")
    if pembayaran == "y":
        nomor_kartu_kredit = input_kredit("Masukkan nomor kartu kredit: ")
        print("Pilihan Token:")
        for denomination, kwh_value in token_options.items():
            print(f"{denomination}: {kwh_value} kWh")
        selected_denomination = int(input("Masukkan nominal token yang ingin Anda beli: "))
        while selected_denomination not in token_options:
            print("Pilihan token tidak valid. Silakan coba lagi.")
            selected_denomination = int(input("Masukkan nominal token yang ingin Anda beli: "))
        kwh_bonus = token_options[selected_denomination]
        bayar = selected_denomination + 2500
        token_sekarang = sisa_token + kwh_bonus
        print(fonts("\nPembayaran Anda sedang diproses...", color='yellow', style='italic'))
        time.sleep(2)
        print(f"Pembayaran kartu kredit {fonts('berhasil', color='blue')}")
        kuitansi_prepaid(email, tanggal, bayar, token_sekarang)
        transaksi_prepaid(email, tanggal, bayar, token_sekarang)
        print(fonts('Tekan Enter untuk kembali ke halaman utama\nTekan Esc untuk logout', color='yellow', style='italic'))
        while True:
            key = ord(msvcrt.getch())
            if key == 13:  
                print(fonts("Kembali ke halaman utama...", color='yellow', style='italic'))
                time.sleep(2)
                os.system('cls')
                home2()
            elif key == 27:  
                logout()
            else:
                print('Input tidak valid!')
                print(fonts('Tekan Enter untuk kembali ke halaman utama\nTekan Esc untuk logout', color='yellow', style='italic'))
    else:
        token_sekarang = sisa_token
        kuitansi_prepaid(email, tanggal, bayar, token_sekarang)
        transaksi_prepaid(email, tanggal, bayar, token_sekarang)
        print(fonts('Tekan Enter untuk kembali ke halaman utama\nTekan Esc untuk logout', color='yellow', style='italic'))
        while True:
            key = ord(msvcrt.getch())
            if key == 13:  
                print(fonts("Kembali ke halaman utama...", color='yellow', style='italic'))
                time.sleep(2)
                os.system('cls')
                home2()
            elif key == 27:  
                logout()
            else:
                print('Input tidak valid!')
                print(fonts('Tekan Enter untuk kembali ke halaman utama\nTekan Esc untuk logout', color='yellow', style='italic'))

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
        if bayar == 0:
            sisa_tagihan = total
        else:
            sisa_tagihan = total - bayar
        print(fonts("\nPembayaran Anda sedang diproses...", color='yellow', style='italic'))
        time.sleep(2)
        print(f"Pembayaran kartu kredit {fonts('berhasil', color='blue')}")
        if sisa_tagihan <= 0 :
            print("Tagihan Anda sudah terbayar penuh")
            kuitansi_postpaid(email, tanggal, total, bayar, sisa_tagihan, kwh)
            transaksi_postpaid(email, tanggal, total, kwh)
            print(fonts('Tekan Enter untuk kembali ke halaman utama\nTekan Esc untuk logout', color='yellow', style='italic'))
            while True:
                key = ord(msvcrt.getch())
                if key == 13:  
                    print(fonts("Kembali ke halaman utama...", color='yellow', style='italic'))
                    time.sleep(2)
                    os.system('cls')
                    home2()
                elif key == 27:  
                    logout()
                else:
                    print('Input tidak valid!')
                    print(fonts('Tekan Enter untuk kembali ke halaman utama\nTekan Esc untuk logout', color='yellow', style='italic'))
        else:
            print("Sisa tagihan Anda sebesar Rp", sisa_tagihan)
            kuitansi_postpaid(email, tanggal, total, bayar, sisa_tagihan, kwh)
            transaksi_postpaid(email, tanggal, total, kwh)
            print(fonts('Tekan Enter untuk kembali ke halaman utama\nTekan Esc untuk logout', color='yellow', style='italic'))
            while True:
                key = ord(msvcrt.getch())
                if key == 13:  
                    print(fonts("Kembali ke halaman utama...", color='yellow', style='italic'))
                    time.sleep(2)
                    os.system('cls')
                    home2()
                elif key == 27:  
                    logout()
                else:
                    print('Input tidak valid!')
                    print(fonts('Tekan Enter untuk kembali ke halaman utama\nTekan Esc untuk logout', color='yellow', style='italic'))
    else:
        if bayar == 0:
            sisa_tagihan = total
        else:
            sisa_tagihan = total - bayar
        print("Sisa tagihan Anda sebesar Rp", total)
        kuitansi_postpaid(email, tanggal, total, bayar, sisa_tagihan, kwh)
        transaksi_postpaid(email, tanggal, total, kwh)
        print(fonts('Tekan Enter untuk kembali ke halaman utama\nTekan Esc untuk logout', color='yellow', style='italic'))
        while True:
            key = ord(msvcrt.getch())
            if key == 13:  
                print(fonts("Kembali ke halaman utama...", color='yellow', style='italic'))
                time.sleep(2)
                os.system('cls')
                home2()
            elif key == 27:  
                logout()
            else:
                print('Input tidak valid!')
                print(fonts('Tekan Enter untuk kembali ke halaman utama\nTekan Esc untuk logout', color='yellow', style='italic'))
   
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
    #Grafik pertama
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(tanggal, pembayaran)
    ax1.set_title('Riwayat Pembayaran (prepaid)')
    ax1.set_xlabel('Tanggal')
    ax1.set_xticklabels(tanggal, rotation='vertical')
    ax1.set_ylabel('Pembayaran (dalam rupiah)')

    # Grafik kedua
    ax2.plot(tanggal2, pemakaian)
    ax2.set_title('Riwayat Pemakaian (prepaid)')
    ax2.set_xlabel('Tanggal')
    ax2.set_xticklabels(tanggal, rotation='vertical')
    ax2.set_ylabel('Pemakaian (dalam kwh)')
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
    #Grafik pertama
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(tanggal, pembayaran)
    ax1.set_title('Riwayat Pembayaran (postpaid)')
    ax1.set_xlabel('Tanggal')
    ax1.set_xticklabels(tanggal, rotation='vertical')
    ax1.set_ylabel('Pembayaran (dalam rupiah)')

    # Grafik kedua
    ax2.plot(tanggal2, pemakaian)
    ax2.set_title('Riwayat Pemakaian (postpaid)')
    ax2.set_xlabel('Tanggal')
    ax2.set_xticklabels(tanggal, rotation='vertical')
    ax2.set_ylabel('Pemakaian (dalam kwh)')
    plt.show()


run()
