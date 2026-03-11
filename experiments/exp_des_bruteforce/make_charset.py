with open("custom.chr", "wb") as f:
    for i in range(256):
        if i != 0x00:
            f.write(bytes([i]))
print("Đã tạo xong file custom.chr gồm 255 bytes!")
