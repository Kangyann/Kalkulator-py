import os,time
def calculator(num1: int,num2: int,opsi: int):
    r = None
    if opsi == 1:
         r = num1 + num2
    elif opsi == 2:
         r = num1 - num2
    elif opsi == 3:
         r = num1 * num2
    elif opsi == 4:
         r = num1 / num2
    else:
         r = 'Operasi Tidak Ditemukan.'
    return print('Hasilnya adalah', r)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print("Pilih operasi:")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")

    o = int(input('Masukan Pilihan 1/2/3/4 : '))
    os.system('cls' if os.name == 'nt' else 'clear')
    r = None
    if o == 1:
         r = 'Penjumlahan'
    elif o == 2:
         r = 'Pengurangan'
    elif o == 3:
         r = 'Perkalian'
    elif o == 4:
         r = 'Pembagian'
    else:
        print('Pilihan Tidak Ditemukan\nSilahkan Ulangi Kembali')
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    print('Pilihan Anda Adalah', r)
    time.sleep(1)
    n1 = input('\nMasukan Bilangan Pertama : ')
    n2 = input('Masukan Bilangan Kedua : ')
    try:
         n1 = int(n1)
         n2 = int(n2)
    except ValueError:
         print('Bilangan Tidak Valid.')
         break
    time.sleep(1)
    calculator(n1,n2,o)
    n = input('\nGunakan Kalkulator Kembali ? \nY/N : ')
    if n.lower() == 'n':
         print('\nThanks For Using')
         time.sleep(1)
         print('Created by Kangyann')
         time.sleep(1)
         print('Keluar Program')
         time.sleep(1)
         os.system('cls' if os.name == 'nt' else 'clear')
         break
    elif n.lower() == 'y':
        True
    else:
        break
        