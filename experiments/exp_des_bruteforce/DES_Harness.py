import os
import binascii
from Cryptodome.Cipher import DES

def main():
    print("--- TRÌNH TẠO DỮ LIỆU BRUTE-FORCE DES ---")
    
    pt_input = input("Nhập plaintext: ")
    
    # Đệm thêm khoảng trắng nếu chưa đủ 8 ký tự
    pt_bytes = pt_input.ljust(8, ' ').encode('utf-8')[:8]
    pt_hex = binascii.hexlify(pt_bytes).decode('utf-8')
    
    # Tạo khóa DES 
    key = os.urandom(8)
    key_hex = binascii.hexlify(key).decode('utf-8')
    
    # 3. Mã hóa DES mode ECB
    cipher = DES.new(key, DES.MODE_ECB)
    ct_bytes = cipher.encrypt(pt_bytes)
    ct_hex = binascii.hexlify(ct_bytes).decode('utf-8')
    
    # Ghi file plaintext.txt
    with open("plaintext.txt", "w") as f:
        f.write(f"Plaintext (String): {pt_bytes.decode('utf-8')}\n")
        f.write(f"Plaintext (Hex)   : {pt_hex}\n")
        
    # Ghi file ciphertext.txt
    with open("ciphertext.txt", "w") as f:
        f.write(f"Ciphertext (Hex)  : {ct_hex}\n")
        
    # Ghi file target để brutefoce
    with open("hashcat_target.txt", "w") as f:
        f.write(f"{ct_hex}:{pt_hex}\n")
        
    print("\nThành công!!!!")
    
    print(f"\nKhóa (Secret Key) để đối chiếu là: {key_hex}")

if __name__ == "__main__":
    main()
