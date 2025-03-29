import base64
from Crypto.Cipher import AES

def adjust_key(key):
    key_bytes = key.encode('utf-8')
    # Ensure key length is exactly 16 bytes (pad with null bytes or trim)
    if len(key_bytes) < 16:
        key_bytes = key_bytes.ljust(16, b'\0')
    elif len(key_bytes) > 16:
        key_bytes = key_bytes[:16]
    return key_bytes

def encrypt_data(plain_text, key):
    key_bytes = adjust_key(key)
    cipher = AES.new(key_bytes, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(plain_text.encode('utf-8'))
    encrypted = {
        'nonce': base64.b64encode(cipher.nonce).decode('utf-8'),
        'tag': base64.b64encode(tag).decode('utf-8'),
        'ciphertext': base64.b64encode(ciphertext).decode('utf-8')
    }
    return encrypted

def decrypt_data(encrypted_data, key):
    key_bytes = adjust_key(key)
    nonce = base64.b64decode(encrypted_data['nonce'])
    tag = base64.b64decode(encrypted_data['tag'])
    ciphertext = base64.b64decode(encrypted_data['ciphertext'])
    cipher = AES.new(key_bytes, AES.MODE_EAX, nonce=nonce)
    plain_text = cipher.decrypt_and_verify(ciphertext, tag)
    return plain_text.decode('utf-8')
