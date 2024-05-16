from flask import Flask, request, jsonify, render_template
from encryption_decryption import RSAEncryption

app = Flask(__name__)
rsa = RSAEncryption()

@app.route('/', methods=['GET', 'POST'])
def homepage():
        return render_template("index.html")

@app.route('/api/encrypt', methods=['POST'])
def encrypt():
    message = request.json['message']
    cipher = rsa.encrypt(message)
    return jsonify(cipher)

@app.route('/api/decrypt', methods=['POST'])
def decrypt():
    message = request.json['message']
    decrypted_message = rsa.decrypt(message)
    return jsonify(decrypted_message)


if __name__ == '__main__':
    app.run(debug=True)