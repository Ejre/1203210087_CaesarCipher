def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():  # Hanya mengenkripsi huruf
            is_upper = char.isupper()
            char = char.lower()
            shifted_char = chr(((ord(char) - ord('a') + shift * mode) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char  # Tidak mengubah karakter selain huruf
    return result

def caesar_cipher_operation(text, shift, operation):
    if operation == "encrypt":
        return caesar_cipher(text, shift, 1)
    elif operation == "decrypt":
        return caesar_cipher(text, shift, -1)
    else:
        return "Operasi tidak valid."

# Input pesan, jumlah pergeseran, dan operasi dari pengguna
pesan = input("Masukkan pesan: ")
shift = int (input("Masukkan jumlah untuk bergeser: "))
operation = input("Operasi (encrypt/decrypt): ").lower()

# Enkripsi atau dekripsi
if operation in ["encrypt", "decrypt"]:
    hasil = caesar_cipher_operation(pesan, shift, operation)
    print(f"Pesan {operation}ed: {hasil}")
else:
    print("Operasi tidak valid.")
