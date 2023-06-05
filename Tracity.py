def run():
    print('========== Track Your Electricity ==========')
    print()
    home()

def home():
    while True:
        print()
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
            if data[0] ==email_daftar:
                print("Pendaftaran gagal. Email sudaf terdaftar.")
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
    print("Maaf, Password salah")
    return False

def keluar():
    print('Terima kasih telah menggunakan Tracity')
    exit()

run()

# import datetime

# def prepaid(riwayat):
#     tanggal = datetime.datetime.now()
#     nominal = float(input("harga"))
#     riwayat.append((tanggal,nominal))

# def tampilkan_riwayat(riwayat):
#     for pembayaran in riwayat:
#         tanggal = pembayaran[0].strftime("%d-%m-%Y %H:%M:%S")
#         nominal = pembayaran[1]
#         print(f"{tanggal} - Rp{nominal}")
    
# riwayat_pembayaran[]

# prepaid(riwayat_pembayaran)



        

