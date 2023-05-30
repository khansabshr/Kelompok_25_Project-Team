def run():
    print('========== Track Your Electricity ==========')
    print()
    home()

def home():
    print()
    print('[1] Masuk')
    print('[2] Daftar')
    print('[3] Keluar')
    pilih = int(input('Silakan pilih    :'))
    if pilih == 1:
        masuk()
    elif pilih == 2:
        daftar()
    elif pilih == 3:
        keluar()
    else :
        print(f'Maaf, pilihan {pilih} tidak tersedia')
        print('Silakan coba lagi')

def daftar():
    print('\n========== Daftar Akun ==========')
    print('\nIsi data-data berikut dengan benar')
    email_daftar = input('Masukkan email yang sudah ada             :')
    password = int(input('Masukkan password 5 karakter berupa angka :'))
    tipe_pw = type(password)
    if tipe_pw == str:
        print('Password harus merupakan angka')
        password = input('Masukkan password 5 karakter berupa angka')
    if tipe_pw == int:
        teks = "Email   : {}\nPassword: {}".format(email_daftar, password)
        file_biodata = open('D:\python\TUBES\Daftar akun.txt', 'w')
        file_biodata.write(teks)
        file_biodata.close()
        print('Anda berhasil registrasi')
        home()

def masuk():
    print('\n========== Masuk ==========')
    print('\nSilakan Masukkan Akun Anda yang Sudah Terdaftar')
    email_login = input('Masukkan email yang sudah ada    :')
    pw_login = int(input('Masukkan password                :'))
    with open('D:\python\TUBES\Daftar akun.txt', 'r') as file:
        for line in file:
            if email_login and str(pw_login) in line:
                print('Login berhasil')
            else:
                print('Maaf, akun anda tidak tersedia')
                email_login
                pw_login

def keluar():
    print('Terima kasih telah menggunakan Tracity')

run()



        

