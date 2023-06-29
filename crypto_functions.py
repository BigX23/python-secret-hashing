import configparser
from cryptography.fernet import Fernet

def get_widget_username():
    config = configparser.ConfigParser()
    config.read("flokenes.toml")
    secret = config["cXbnzAfR"]["secret"]
    key = b'ufaXDGwHLvclunQaW70rVAJRUNNhfXSS035Swa2T3pc='
    cipher_suite = Fernet(key)
    encryptedpwd = bytes(secret, "utf-8")
    uncipher_text = cipher_suite.decrypt(encryptedpwd)
    plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8")
    return plain_text_encryptedpassword


def get_widget_password():
    config = configparser.ConfigParser()
    config.read("flokenes.toml")
    secret = config["VPkNRUNhzF"]["secret"]
    key = b'2bkIg4DQeznUNN4LnhoDPSbv498zyUgvMjq54HFTePw='
    cipher_suite = Fernet(key)
    encryptedpwd = bytes(secret, "utf-8")
    uncipher_text = cipher_suite.decrypt(encryptedpwd)
    plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8")
    return plain_text_encryptedpassword


