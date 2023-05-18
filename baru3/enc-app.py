import socket
from Crypto.Cipher import AES, DES, ARC4
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import random
import time

# Fungsi untuk mengenkripsi pesan menggunakan AES
def encrypt_aes(key, iv, plaintext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

# Fungsi untuk mengenkripsi pesan menggunakan DES
def encrypt_des(key, iv, plaintext):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size))
    return ciphertext

# Fungsi untuk mengenkripsi pesan menggunakan RC4
def encrypt_rc4(key, iv, plaintext):
    cipher = ARC4.new(key, iv)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# Inisialisasi key dan iv untuk setiap algoritma
aes_key = b'babingepbabingep'
des_key = b'babingep'
rc4_key = b'babingepbabingep'
aes_iv = b'burungjhburungjh'  # IV dengan panjang 16 byte untuk AES
des_iv = b'burungjh'  # IV dengan panjang 8 byte untuk DES
rc4_iv = 0  # IV untuk RC4 harus berupa integer

# Baca file yang akan dikirim
filename = 'sample_file.txt'  # Ganti dengan nama file yang ingin dikirim
with open(filename, 'rb') as file:
    plaintext = file.read()

# Pilih algoritma enkripsi yang ingin digunakan oleh user (AES, DES, atau RC4)
encryption_choice = input("Pilih jenis algoritma enkripsi (AES, DES, atau RC4): ")

# Enkripsi file sesuai dengan algoritma yang dipilih
if encryption_choice == 'AES':
    start_time = time.time()
    ciphertext = encrypt_aes(aes_key, aes_iv, plaintext)
    algorithm = 'AES'
elif encryption_choice == 'DES':
    start_time = time.time()
    ciphertext = encrypt_des(des_key, des_iv, plaintext)
    algorithm = 'DES'
elif encryption_choice == 'RC4':
    start_time = time.time()
    ciphertext = encrypt_rc4(rc4_key, rc4_iv, plaintext)
    algorithm = 'RC4'
else:
    print("Algoritma enkripsi yang dipilih tidak tersedia.")
    exit()

# Tulis ciphertext ke file teks baru
ciphertext_filename = 'ciphertext.txt'  # Nama file ciphertext baru
with open(ciphertext_filename, 'wb') as file:
    file.write(ciphertext)

# Hitung waktu eksekusi enkripsi
end_time = time.time()
running_time = end_time - start_time

# Simpan hasil running time ke dalam file teks
result_filename = 'result.txt'  # Nama file untuk menyimpan hasil running time
with open(result_filename, 'w') as file:
    file.write(f'Hasil running time enkripsi adalah: {running_time} detik\n')
    file.write(f'Algoritma enkripsi yang digunakan: {algorithm}\n')

# Kirim informasi tentang algoritma enkripsi yang digunakan ke penerima
# (Misalnya, melalui header pesan atau protokol komunikasi yang telah disepakati sebelumnya)

# Kirim ciphertext ke server penerima
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 7777))  # Ganti dengan IP address dan port number penerima
sock.sendall(ciphertext)
sock.close()