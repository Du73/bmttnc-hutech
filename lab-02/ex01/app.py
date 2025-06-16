import subprocess
import sys
import os
from flask import Flask, jsonify, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher

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

@app.route("/launch/caesar", methods=["POST"])
def launch_caesar():
    try:
        current_dir = os.path.dirname(__file__)  # C:\bmttnc-hutech\lab-02\ex01
        lab02_dir = os.path.dirname(current_dir)  # C:\bmttnc-hutech\lab-02
        root_dir = os.path.dirname(lab02_dir)     # C:\bmttnc-hutech
        caesar_file = os.path.join(root_dir, 'lab-03', 'caesar_cipher.py')
        
        if not os.path.exists(caesar_file):
            return jsonify({"status": "error", "message": f"File not found: {caesar_file}"}), 404
        
        subprocess.Popen([sys.executable, caesar_file])
        
        return jsonify({"status": "success", "message": "Caesar Cipher launched successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/launch/vigenere", methods=["POST"])
def launch_vigenere():
    try:
        current_dir = os.path.dirname(__file__)
        lab02_dir = os.path.dirname(current_dir)
        root_dir = os.path.dirname(lab02_dir)
        vigenere_file = os.path.join(root_dir, 'lab-03', 'vigenere_cipher.py')
        
        if not os.path.exists(vigenere_file):
            return jsonify({"status": "error", "message": f"File not found: {vigenere_file}"}), 404
        
        subprocess.Popen([sys.executable, vigenere_file])
        
        return jsonify({"status": "success", "message": "Vigenere Cipher launched successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/launch/railfence", methods=["POST"])
def launch_railfence():
    try:
        current_dir = os.path.dirname(__file__)
        lab02_dir = os.path.dirname(current_dir)
        root_dir = os.path.dirname(lab02_dir)
        railfence_file = os.path.join(root_dir, 'lab-03', 'railfence_cipher.py')
        
        if not os.path.exists(railfence_file):
            return jsonify({"status": "error", "message": f"File not found: {railfence_file}"}), 404
        
        subprocess.Popen([sys.executable, railfence_file])
        
        return jsonify({"status": "success", "message": "Rail Fence Cipher launched successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route("/launch/playfair", methods=["POST"])
def launch_playfair():
    try:
        current_dir = os.path.dirname(__file__)
        lab02_dir = os.path.dirname(current_dir)
        root_dir = os.path.dirname(lab02_dir)
        playfair_file = os.path.join(root_dir, 'lab-03', 'playfair_cipher.py')
        
        if not os.path.exists(playfair_file):
            return jsonify({"status": "error", "message": f"File not found: {playfair_file}"}), 404
        
        subprocess.Popen([sys.executable, playfair_file])
        
        return jsonify({"status": "success", "message": "Playfair Cipher launched successfully."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5050, debug=True)