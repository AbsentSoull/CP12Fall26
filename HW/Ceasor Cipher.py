def encrypt(s, shift):
    ans = ""
    for i in range(len(s)):
        letter = ord(s[i]) + shift
        if letter > ord('Z'):
            letter -= 26
        ans += chr(letter)
    return ans
def decrypt(s, shift):
    ans = ""
    for i in range(len(s)):
        letter = ord(s[i]) - shift
        if letter < ord('A'):
            letter += 26
        ans += chr(letter)
    return ans
s = "DECAFZ"
shift = 2
encrypted = encrypt(s, shift)
s = input("Enter a message: ")
shift = int(input("Enter shift number: "))
encrypted = encrypt(s, shift)
print("Encrypted:", encrypted)
decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)
