class VigenereCipher:
    def __init__(self):
        pass

    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""
        key_index = 0
        for char in plain_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) %26 + ord('a'))
                key_index += 1
            else:
                encrypted_text += char
        return encrypted_text
    
    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""
        key_index = 0
        for char in encrypted_text:
            if char.isalpha():
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')
                if char.isupper():
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))
                key_index += 1
            else:
                decrypted_text += char
        return decrypted_text
        

    def decrypt(self, ciphertext):
        plaintext = []
        keyword_repeated = (self.keyword * (len(ciphertext) // len(self.keyword) + 1))[:len(ciphertext)]
        for c, k in zip(ciphertext, keyword_repeated):
            if c.isalpha():
                c_index = self.alphabet.index(c.upper())
                k_index = self.alphabet.index(k.upper())
                p_index = (c_index - k_index) % len(self.alphabet)
                plaintext.append(self.alphabet[p_index])
            else:
                plaintext.append(c)
        return ''.join(plaintext)