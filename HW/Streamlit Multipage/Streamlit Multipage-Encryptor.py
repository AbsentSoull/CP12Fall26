
import streamlit as st

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

s = st.text_input("Enter a message:")
shift = st.number_input("Enter shift number:", step=1)

if st.button("Encrypt"):
    encrypted = encrypt(s, shift)
    st.write("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, shift)
    st.write("Decrypted:", decrypted)
