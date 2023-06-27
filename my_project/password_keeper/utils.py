from cryptography.fernet import Fernet
from django.conf import settings


def get_token():
    key = settings.PASSWORD_KEY
    key_obj = Fernet(key.encode())
    return key_obj


def encrypt(app_password):
    token = get_token()
    encrypted_text = token.encrypt(app_password.encode())
    return encrypted_text.decode()


def decrypt(encrypted_text):
    token = get_token()
    decrypt_text = token.decrypt(encrypted_text.encode())
    return decrypt_text.decode()




