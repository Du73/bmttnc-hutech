import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow
import requests


class PlayfairApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_gen.clicked.connect(self.call_api_generate_matrix)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)

    def call_api_generate_matrix(self):
        url = "http://127.0.0.1:5000/api/playfair/creatematrix"
        payload = {
            "key": self.ui.txt_key.text(),
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                # Chuyển đổi danh sách thành chuỗi
                matrix = data["playfair_matrix"]
                formatted_matrix = "\n".join([" ".join(row) for row in matrix])
                self.ui.txt_matrix.setText(formatted_matrix)

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Matrix Generated Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain.toPlainText(),
            "key": self.ui.txt_key.text(),
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher.setText(data["encrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher.toPlainText(),
            "key": self.ui.txt_key.text(),
        }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain.setText(data["decrypted_message"])

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayfairApp()
    window.show()
    sys.exit(app.exec_())