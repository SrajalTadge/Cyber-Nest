from flask import Blueprint, request, jsonify, render_template
from utils.encryption import encrypt_data, decrypt_data

cryptography_bp = Blueprint('cryptography', __name__, url_prefix='/cryptography')

@cryptography_bp.route('/', methods=['GET', 'POST'])
def cryptography():
    # This route simply serves the page with both encryption and decryption forms.
    return render_template('cryptography.html')

@cryptography_bp.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    plain_text = data.get('data', '')
    key = data.get('key', '')
    try:
        encrypted_data = encrypt_data(plain_text, key)
        return jsonify({"encrypted_data": encrypted_data})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@cryptography_bp.route('/decrypt', methods=['POST'])
def decrypt():
    data = request.get_json()
    encrypted_data = data.get('encrypted_data')
    key = data.get('key', '')
    if not encrypted_data:
        return jsonify({"error": "Missing encrypted_data"}), 400
    try:
        plain_text = decrypt_data(encrypted_data, key)
        return jsonify({"plain_text": plain_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
