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
def decrypt_rc4(key, ciphertext):
    cipher = ARC4.new(key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Inisialisasi key dan iv untuk setiap algoritma
aes_key = b'babingepbabingep'
des_key = b'babingep'
rc4_key = b'babingepbabingep'
iv = b'burungjhburungjh'

# Baca algoritma enkripsi yang digunakan dari file result.txt
result_filename = 'result.txt' # Nama file yang berisi hasil running time
with open(result_filename, 'r') as file:
    lines = file.readlines()
algorithm = lines[1].strip().split(': ')[1]

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

# Dapatkan informasi tentang algoritma enkripsi yang digunakan dari pengirim
# (Misalnya, melalui header pesan atau protokol komunikasi yang telah disepakati sebelumnya)
algorithm = 'AES'  # Ganti dengan algoritma yang sesuai

# Dekripsi ciphertext sesuai dengan algoritma yang digunakan oleh pengirim
if algorithm == 'AES':
    start_time = time.time()
    plaintext = decrypt_aes(aes_key, iv, ciphertext)
elif algorithm == 'DES':
    start_time = time.time()
    plaintext = decrypt_des(des_key, iv, ciphertext)
elif algorithm == 'RC4':
    start_time = time.time()
    plaintext = decrypt_rc4(rc4_key, ciphertext)

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