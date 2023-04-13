from Crypto.Cipher import AES, ARC4, DES
from Crypto.Util.Padding import unpad
from Crypto.Util.Counter import Counter
from Crypto.Random import get_random_bytes
import os

# Fungsi untuk dekripsi file dengan algoritma AES
def decrypt_aes(key, iv, ciphertext):
    cipher = AES.new(key, AES.MODE_CTR, counter=Counter.new(128, initial_value=int.from_bytes(iv, byteorder='big')))
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Fungsi untuk dekripsi file dengan algoritma RC4
def decrypt_rc4(key, ciphertext):
    cipher = ARC4.new(key)
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Fungsi untuk dekripsi file dengan algoritma DES
def decrypt_des(key, iv, ciphertext):
    cipher = DES.new(key, DES.MODE_CTR, counter=Counter.new(64, initial_value=int.from_bytes(iv, byteorder='big')))
    plaintext = cipher.decrypt(ciphertext)
    return plaintext

# Fungsi untuk dekripsi file
def decrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
        iv = encrypted_data[:16]  # IV 128 bit
        rc4_iv = encrypted_data[16:32]  # IV 64 bit untuk RC4
        des_iv = encrypted_data[32:40]  # IV 64 bit untuk DES
        decrypted_data = decrypt_aes(key, iv, encrypted_data[40:80]) + decrypt_rc4(key, rc4_iv, encrypted_data[80:120]) + decrypt_des(key, des_iv, encrypted_data[120:])
    with open(file_path, 'wb') as file:
        file.write(decrypted_data)

# Main program
if __name__ == '__main__':
    # Key yang digunakan untuk dekripsi (contoh, gunakan kunci yang sesuai untuk implementasi yang sebenarnya)
    key = get_random_bytes(16)  # Key 128 bit

    file_path = 'encrypted_file.bin'  # Path file yang ingin didekripsi

    # Dekripsi file
    decrypt_file(file_path, key)

    print('File has been decrypted successfully.')