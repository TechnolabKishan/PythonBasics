import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars : {chars}")
#print(f"key : {key}")

#encrypt

# plain_Text = input('enter a message to encrypt: ')
# cipher_text = ''

# for text in plain_Text:
#     index = chars.index(text)
#     cipher_text += key[index]

# print(f'origanl messafe: {plain_Text}')
# print(f'encrypt messafe: {cipher_text}')

#dencrypt

cipher_text = input('enter a message to encrypt: ')
plaintext = ''

for text in cipher_text:
    index = key.index(text)
    plaintext += chars[index]

print(f'origanl messafe: {cipher_text}')
print(f'encrypt messafe: {plaintext}')



