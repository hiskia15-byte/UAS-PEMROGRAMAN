import string
import os

while True:
    os.system('cls')

    print(10*"=","SISTEM ENKRIPSI PESAN","="*10,"\n")

    pesan_asli = input(f"masukan pesan yang akan dienkripsi: ")
    print("\n")
    kunci = [1,3,5,7,9] 
    a_z = string.ascii_lowercase
    enkripsi = []

    for i, pesan in enumerate(pesan_asli.lower()):
        if pesan in a_z:
            berubah = (a_z.index(pesan) + kunci[i % len(kunci)]) % 26
            enkripsi.append(a_z[berubah])
        else:
            enkripsi.append(pesan)
    enkripsi = ''.join(enkripsi)
    print(f"enkripsi bergerak\t: {enkripsi}")

    with open("kunci1.txt", "w") as file:
        file.write(" ".join(map(str,kunci)))
    try:
        with open("kunci1.txt", "r") as file:
            kunci_file = list(map(int, file.read().split()))
        print(f"kunci bergerak dari file: {kunci_file}")
    except:
        print("file kunci_bergera.txt tidak ditemukan")
        kunci_file = []

    if kunci_file:
        dekripsi = []
        for i, pesan in enumerate(enkripsi.lower()):
            if pesan in a_z:
                berubah = (a_z.index(pesan) - kunci_file[i % len(kunci_file)]) % 26
                dekripsi.append(a_z[berubah])
            else:
                dekripsi.append(pesan)
        dekripsi = ''.join(dekripsi)
        print(f"dekripsi bergerak\t: {dekripsi}\n")

    kunci_caesar_cipher = [2]
    enkripsi_cipher = []
    for i, pesan in enumerate(pesan_asli.lower()):
        enkripsi_cipher.append(chr(ord(pesan) ^ kunci_caesar_cipher[i % len(kunci_caesar_cipher)]))
    enkripsi_cipher = ''.join(enkripsi_cipher)
    print(f"enkrpsi cipher\t\t: {enkripsi_cipher}")

    with open("kunci2.txt", "w") as file:
        file.write(" ".join(map(str,kunci_caesar_cipher)))
    try:
        with open("kunci2.txt", "r") as file:
            kunci_file = list(map(int, file.read().split()))
        print(f"kunci cipher dari file\t: {kunci_file}")
    except:
        print("file kunc.txt tidak ditemukan")

    dekripsi_cipter = []
    for i, pesan in enumerate(enkripsi_cipher):
        dekripsi_cipter.append(chr(ord(pesan) ^ kunci_caesar_cipher[i % len(kunci_caesar_cipher)]))
    dekripsi_cipter = ''.join(dekripsi_cipter)
    print(f"dekripsi cipher\t\t: {dekripsi_cipter}\n")

    lanjutan = [1,3,5,7,9]
    enkripsi_pesan = []
    for i, pesan in enumerate(pesan_asli.lower()):
        enkripsi_pesan.append(chr(ord(pesan) - lanjutan[i % len(lanjutan)]))
    enkripsi_pesan = ''.join(enkripsi_pesan)
    print(f"enkrpsi lanjutan\t: {enkripsi_pesan}")

    with open("kunci3.txt", "w") as file:
        file.write(" ".join(map(str,lanjutan)))
    try:
        with open("kunci3.txt", "r") as file:
            kunci_rahasia = list(map(int, file.read().split()))
        print(f"kunci lanjutan dri file: {kunci_rahasia}")
    except:
        print("file kunci lanjutan.txt tidak ditenukan")

    dekripsi_pesan = []
    for i, pesan in enumerate(enkripsi_pesan):
        dekripsi_pesan.append(chr(ord(pesan) + lanjutan[i % len(lanjutan)]))
    dekripsi_pesan = ''.join(dekripsi_pesan)
    print(f"dekripsi lanjutan\t: {dekripsi_pesan}")

    opsi = input("\napakah ingin mengenkipsi ulang? [y/n]")
    if opsi == "y" or opsi == "Y":
        continue
    else:
        break
print(10*"=","SISTEM ENKRIPSI BERAKHIR","="*10)