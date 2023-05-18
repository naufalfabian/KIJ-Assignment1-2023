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
def encrypt_rc4(key, plaintext):
    cipher = ARC4.new(key)
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext

# Inisialisasi key dan iv untuk setiap algoritma
aes_key = b'babingepbabingep'
des_key = b'babingep'
rc4_key = b'babingepbabingep'
iv = b'burungjhburungjh'

# Baca file yang akan dikirim
filename = 'sample_file.txt'  # Ganti dengan nama file yang ingin dikirim
with open(filename, 'rb') as file:
    plaintext = file.read()

# Pilihan algoritma enkripsi yang tersedia
encryption_choices = ['AES', 'DES', 'RC4']
print("Pilihan algoritma enkripsi: ")
for i, choice in enumerate(encryption_choices):
    print(f"{i + 1}. {choice}")
encryption_choice = input("Masukkan pilihan algoritma enkripsi (1/2/3): ")

# Validasi input pilihan algoritma enkripsi
while encryption_choice not in ['1', '2', '3']:
    print("Pilihan tidak valid. Silakan masukkan pilihan yang benar.")
    encryption_choice = input("Masukkan pilihan algoritma enkripsi (1/2/3): ")

encryption_choice = int(encryption_choice)



# Enkripsi file sesuai dengan algoritma yang dipilih
ciphertext = None # Menambahkan definisi awal ciphertext
algorithm = None # Menambahkan definisi awal algorithm
start_time = None # Menambahkan definisi awal start_time
if encryption_choice == 1: # Mengubah menjadi integer tanpa tanda kutip
    start_time = time.time()
    ciphertext = encrypt_aes(aes_key, iv, plaintext)
    algorithm = 'AES'
elif encryption_choice == 2: # Mengubah menjadi integer tanpa tanda kutip
    start_time = time.time()
    ciphertext = encrypt_des(des_key, iv, plaintext)
    algorithm = 'DES'
elif encryption_choice == 3: # Mengubah menjadi integer tanpa tanda kutip
    start_time = time.time()
    ciphertext = encrypt_rc4(rc4_key, plaintext)
    algorithm = 'RC4'

# Tulis ciphertext ke file teks baru
ciphertext_filename = 'ciphertext.txt'
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

# Membuat koneksi socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 7777))  
# Ganti dengan IP address dan port number penerima

# Mengirim informasi tentang algoritma enkripsi yang digunakan sebagai header pesan
header = algorithm.encode('utf-8')
sock.sendall(header)

# Kirim ciphertext ke server penerima
sock.sendall(ciphertext)

# Tutup koneksi socket
sock.close()