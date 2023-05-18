import socket
from Crypto.Cipher import AES, DES, ARC4
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import random
import time

# Fungsi untuk mendekripsi pesan menggunakan AES
def decrypt_aes(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# Fungsi untuk mendekripsi pesan menggunakan DES
def decrypt_des(key, iv, ciphertext):
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return plaintext

# Fungsi untuk mendekripsi pesan menggunakan RC4
def decrypt_rc4(key, iv, ciphertext):
    cipher = ARC4.new(key, iv)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Inisialisasi key dan iv untuk setiap algoritma
aes_key = b'babingepbabingep'
des_key = b'babingep'
rc4_key = b'babingepbabingep'
aes_iv = b'burungjhburungjh'  # IV dengan panjang 16 byte untuk AES
des_iv = b'burungjh'  # IV dengan panjang 8 byte untuk DES
rc4_iv = 0  # # IV untuk RC4 harus berupa integer

# Buka socket untuk menerima ciphertext dari pengirim
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 7777))  # Ganti dengan IP address dan port number yang sama dengan pengirim
sock.listen(1)
print("Menunggu koneksi dari pengirim...")
conn, addr = sock.accept()
print("Menerima koneksi dari:", addr)

# Terima ciphertext dari pengirim
ciphertext = b''
while True:
    data = conn.recv(1024)
    if not data:
        break
    ciphertext += data
conn.close()
sock.close()

# Pilih algoritma enkripsi yang digunakan oleh pengirim (AES, DES, atau RC4)
algorithm = input("Pilih jenis algoritma enkripsi yang digunakan oleh pengirim (AES, DES, atau RC4): ")

# Dekripsi ciphertext sesuai dengan algoritma yang digunakan oleh pengirim
if algorithm == 'AES':
    start_time = time.time()
    plaintext = decrypt_aes(aes_key, aes_iv, ciphertext)
elif algorithm == 'DES':
    start_time = time.time()
    plaintext = decrypt_des(des_key, des_iv, ciphertext)
elif algorithm == 'RC4':
    start_time = time.time()
    plaintext = decrypt_rc4(rc4_key, rc4_iv, ciphertext)
else:
    print("Algoritma enkripsi yang digunakan oleh pengirim tidak tersedia.")
    exit()

# Hitung waktu eksekusi dekripsi
end_time = time.time()
running_time = end_time - start_time

# Simpan file yang sudah didekripsi
filename = 'decrypted_file.txt'  # Ganti dengan nama file yang diinginkan
with open(filename, 'wb') as file:
    file.write(plaintext)
print("File telah didekripsi dan disimpan sebagai:", filename)

# Simpan hasil running time ke dalam file teks
result_filename = 'result.txt' # Nama file untuk menyimpan hasil running time
with open(result_filename, 'a') as file: # Menggunakan mode 'a' agar menambahkan hasil running time ke file yang sudah ada
    file.write(f'Hasil running time deskripsi adalah: {running_time} detik\n')