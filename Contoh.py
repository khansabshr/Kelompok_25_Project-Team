import datetime

def postpaid(riwayat):
    tanggal = datetime.datetime.now()
    nominal = float(input("Masukkan nominal pembayaran: "))
    riwayat.append((tanggal, nominal))

def tampilkan_riwayat(riwayat):
    print("Riwayat Pembayaran:")
    for pembayaran in riwayat:
        tanggal = pembayaran[0].strftime("%d-%m-%Y %H:%M:%S")
        nominal = pembayaran[1]
        print(f"{tanggal} - Rp{nominal}")

riwayat_pembayaran = []

while True:
    pilihan = input("Masukkan pilihan (1/2/3): ")

    if pilihan == "1":
        postpaid(riwayat_pembayaran)
    elif pilihan == "2":
        tampilkan_riwayat(riwayat_pembayaran)
    elif pilihan == "3":
        print("Terima kasih! Telah menggunakan Tracity")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")