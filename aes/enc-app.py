import socket
from Crypto.Cipher import AES, DES, ARC4
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import random

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
aes_key = b'\x12\x34\x56\x78\x90\xAB\xCD\xEF\x12\x34\x56\x78\x90\xAB\xCD\xEF'
des_key = get_random_bytes(8)
rc4_key = get_random_bytes(16)
iv = b'\xAB\xCD\xEF\x12\x34\x56\x78\x90\x12\x34\x56\x78\x90\xAB\xCD\xEF'

# Baca file yang akan dikirim
filename = 'sample_file.txt'  # Ganti dengan nama file yang ingin dikirim
with open(filename, 'rb') as file:
    plaintext = file.read()

# Pilih algoritma enkripsi secara acak (AES, DES, atau RC4)
encryption_choice = 'AES'

# Enkripsi file sesuai dengan algoritma yang dipilih
if encryption_choice == 'AES':
    ciphertext = encrypt_aes(aes_key, iv, plaintext)
    algorithm = 'AES'
elif encryption_choice == 'DES':
    ciphertext = encrypt_des(des_key, iv, plaintext)
    algorithm = 'DES'
elif encryption_choice == 'RC4':
    ciphertext = encrypt_rc4(rc4_key, plaintext)
    algorithm = 'RC4'

# Tulis ciphertext ke file teks baru
ciphertext_filename = 'ciphertext.txt'  # Nama file ciphertext baru
with open(ciphertext_filename, 'wb') as file:
    file.write(ciphertext)

# Kirim informasi tentang algoritma enkripsi yang digunakan ke penerima
# (Misalnya, melalui header pesan atau protokol komunikasi yang telah disepakati sebelumnya)

# Kirim ciphertext ke server penerima
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 7777))  # Ganti dengan IP address dan port number penerima
sock.sendall(ciphertext)
sock.close()