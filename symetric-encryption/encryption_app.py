import os
from Crypto.Cipher import AES, ARC4, DES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# Function to encrypt a file using AES
def encrypt_aes(filename, key, iv):
    aes_cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(filename, 'rb') as file:
        plaintext = file.read()
    ciphertext = aes_cipher.encrypt(pad(plaintext, AES.block_size))
    return ciphertext

# Function to decrypt a file using AES
def decrypt_aes(filename, key, iv):
    aes_cipher = AES.new(key, AES.MODE_CBC, iv)
    with open(filename, 'rb') as file:
        ciphertext = file.read()
    plaintext = unpad(aes_cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# Function to encrypt a file using RC4
def encrypt_rc4(filename, key):
    rc4_cipher = ARC4.new(key)
    with open(filename, 'rb') as file:
        plaintext = file.read()
    ciphertext = rc4_cipher.encrypt(plaintext)
    return ciphertext

# Function to decrypt a file using RC4
def decrypt_rc4(filename, key):
    rc4_cipher = ARC4.new(key)
    with open(filename, 'rb') as file:
        ciphertext = file.read()
    plaintext = rc4_cipher.decrypt(ciphertext)
    return plaintext

# Function to encrypt a file using DES
def encrypt_des(filename, key, iv):
    des_cipher = DES.new(key, DES.MODE_CBC, iv)
    with open(filename, 'rb') as file:
        plaintext = file.read()
    ciphertext = des_cipher.encrypt(pad(plaintext, DES.block_size))
    return ciphertext

# Function to decrypt a file using DES
def decrypt_des(filename, key, iv):
    des_cipher = DES.new(key, DES.MODE_CBC, iv)
    with open(filename, 'rb') as file:
        ciphertext = file.read()
    plaintext = unpad(des_cipher.decrypt(ciphertext), DES.block_size)
    return plaintext

# Main function
def main():
    # Generate a random key and IV for AES and DES
    aes_key = get_random_bytes(16)
    aes_iv = get_random_bytes(AES.block_size)
    des_key = get_random_bytes(8)
    des_iv = get_random_bytes(DES.block_size)

    # Encrypt a sample file using AES
    aes_ciphertext = encrypt_aes('sample_file.txt', aes_key, aes_iv)
    with open('sample_file_aes.bin', 'wb') as file:
        file.write(aes_ciphertext)

    # Decrypt the AES ciphertext
    aes_plaintext = decrypt_aes('sample_file_aes.bin', aes_key, aes_iv)
    with open('sample_file_aes_decrypted.txt', 'wb') as file:
        file.write(aes_plaintext)

    # Encrypt the same sample file using RC4
    rc4_ciphertext = encrypt_rc4('sample_file.txt', rc4_key)
    with open('sample_file_rc4.bin', 'wb') as file:
        file.write(rc4_ciphertext)

    # Decrypt the RC4 ciphertext
    rc4_plaintext = decrypt_rc4('sample_file_rc4.bin', rc4_key)
    with open('sample_file_rc4_decrypted.txt', 'wb') as file:
        file.write(rc4_plaintext)

    # Encrypt the same sample file using DES
    des_ciphertext = encrypt_des('sample_file.txt', des_key, des_iv)
    with open('sample_file_des.bin', 'wb') as file:
        file.write(des_ciphertext)

    # Decrypt the DES ciphertext
    des_plaintext = decrypt_des('sample_file_des.bin', des_key, des_iv)
    with open('sample_file_des_decrypted.txt', 'wb') as file:
        file.write(des_plaintext)