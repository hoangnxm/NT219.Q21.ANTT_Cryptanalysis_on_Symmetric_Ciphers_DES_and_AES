from Cryptodome.Cipher import DES
import binascii
import os

def generate_des():
    plaintext = b'TANCONGA'

    # Tạo 8 bytes key ngẫu nhiên
    key = os.urandom(8)

    # ===== MÃ HÓA DES =====
    cipher = DES.new(key, DES.MODE_ECB)
    ciphertext = cipher.encrypt(plaintext)

    # ===== CHUYỂN SANG HEX =====
    hex_pt = binascii.hexlify(plaintext).decode()
    hex_ct = binascii.hexlify(ciphertext).decode()
    hex_key = binascii.hexlify(key).decode()

    print(f"Plaintext : {plaintext.decode()} -> {hex_pt}")
    print(f"Ciphertext: {hex_ct}")

    print("\nKEY")
    print(hex_key)

    hashcat_format = f"{hex_ct}:{hex_pt}"
    
    with open("des_target.txt", "w") as f:
        f.write(hashcat_format)

    print("\nFile des_target.txt đã được tạo.")

if __name__ == "__main__":
    generate_des()
