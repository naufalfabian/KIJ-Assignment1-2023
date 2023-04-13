from Crypto.Cipher import AES, DES, ARC4
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

filename = input("Enter the name of the file to encrypt: ")
algorithm = input("Enter the algorithm to use (AES, RC4, or DES): ")
password = input("Enter the password for encryption: ")

# read the file to encrypt
with open(filename, 'rb') as f:
    plaintext = f.read()

# create key object based on password
if algorithm == 'AES':
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)
elif algorithm == 'RC4':
    key = get_random_bytes(16)
    cipher = ARC4.new(key)
elif algorithm == 'DES':
    key = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_CBC)

    # pad the plaintext
if algorithm == 'RC4':
    padded_plaintext = plaintext
else:
    padded_plaintext = pad(plaintext, cipher.block_size)

    # encrypt the plaintext
ciphertext = cipher.iv + cipher.encrypt(padded_plaintext)

# write the encrypted file
with open(filename + '.enc', 'wb') as f:
    f.write(ciphertext)

print(f"{algorithm} encryption of {filename} successful!")