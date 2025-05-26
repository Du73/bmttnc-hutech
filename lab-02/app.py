from flask import Flask, render_template, request, json
from ex01.cipher.caesar import CaesarCipher
from ex01.cipher.vigenere import VigenereCipher
from ex01.cipher.railfence import RailFenceCipher
from ex01.cipher.playfair import PlayFairCipher

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text} </br> key: {key} </br> encrypted text: {encrypted_text}"

@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypted_text(text, key)
    return f"text: {text} </br> key: {key} </br> decrypted text: {decrypted_text}"

@app.route('/vigenere')
def vigenere():
    return render_template('vigenere.html')

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    
    return f"text: {text} </br> key: {key} </br> encrypted text: {encrypted_text}"

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return f"text: {text} </br> key: {key} </br> decrypted text: {decrypted_text}"

@app.route('/railfence')
def railfence():
    return render_template('railfence.html')

@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKey'])
    RailFence = RailFenceCipher()
    encrypted_text = RailFence.rail_fence_encrypt(text, key)
    return f"text: {text} </br> key: {key} </br> encrypted text: {encrypted_text}"

@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKey'])
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.rail_fence_decrypt(text, key)
    return f"text: {text} </br> key: {key} </br> decrypted text: {decrypted_text}"

@app.route('/playfair')
def playfair():
    return render_template('playfair.html')

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    Playfair = PlayFairCipher()
    playfair_matrix = Playfair.create_playfair_matrix(key)
    encrypted_text = Playfair.playfair_encrypt(text, playfair_matrix)
    return f"text: {text} </br> key: {key} </br> encrypted text: {encrypted_text}"

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKey']
    Playfair = PlayFairCipher()
    playfair_matrix = Playfair.create_playfair_matrix(key)
    decrypted_text = Playfair.playfair_decrypt(text, playfair_matrix)
    return f"text: {text} </br> key: {key} </br> decrypted text: {decrypted_text}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)