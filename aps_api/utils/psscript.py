from Crypto.Cipher import AES
import base64

def decrypt_password(encrypted_password, secret_key, iv_hex):
    # Asegúrate de que la clave tenga la longitud correcta para AES
    if len(secret_key) not in [16, 24, 32]:
        raise ValueError("AES key must be either 16, 24, or 32 bytes long")

    # Convierte el IV de hexadecimal a bytes
    iv = bytes.fromhex(iv_hex)
    if len(iv) != 16:
        raise ValueError("Incorrect IV length (it must be 16 bytes long)")

    # Decodifica y desencripta el password
    cipher = AES.new(secret_key.encode('utf-8'), AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(base64.b64decode(encrypted_password))
    return decrypted.strip().decode('utf-8')
