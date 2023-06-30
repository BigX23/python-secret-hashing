#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
----------------------------------------------
Created By: Matt White <https://github.com/BigX23>
Created Date: 01/2023
Version: 1.0
----------------------------------------------

hashing_setup.py

This module is used to encrypt a secret and write the ciphered text to a toml file, and then create
a function that will read the toml file, decrypt the secret, and return it.
"""

import random
import string
from cryptography.fernet import Fernet

# TOML file name to write hashed secrets to
TOML_FILE = "flokenes.toml"

# Module to write the crypto functions to
CRYPTO_MODULE = "crypto_functions.py"


def random_string_write():
    """
    Generate a random string of length 7 to 10 characters and append it to a TOML file.

    This function generates a random string of length 7 to 10 characters using the ASCII letters
    and writes it to the end of a TOML file. The function returns the generated random string.

    Returns:
    str: The generated random string.
    """
    rand_string = "".join(
        random.choice(string.ascii_letters) for i in range(random.randint(7, 10))
    )
    with open(TOML_FILE, "a", encoding="utf-8") as f:
        f.write("\n\n[" + rand_string + "]")
    return rand_string


def generate_key_and_encrypt_password(secret, call_name):
    """
    This function generates a Fernet key and uses it to encrypt a password. The encrypted password
    is then written to a TOML file, and a new function that can decrypt the password is generated
    and written to a Python module. The name of the generated function is specified by the
    `call_name` parameter.

    Args:
    secret (str): The password to encrypt.
    call_name (str): The name to give to the generated function.

    Returns:
    None.
    """
    reference_name = random_string_write()
    byte_secret = bytes(secret, "utf-8")
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    ciphered_text = cipher_suite.encrypt(byte_secret)
    string_ciphertext = ciphered_text.decode("utf-8")
    with open("flokenes.toml", "a", encoding="utf-8") as f:
        f.write("\nsecret = " + string_ciphertext)

    print_str = (
        """def """
        + call_name
        + '''():
    config = configparser.ConfigParser()
    config.read("flokenes.toml")
    secret = config["'''
        + reference_name
        + """"]["secret"]
    key = """
        + str(key)
        + """
    cipher_suite = Fernet(key)
    encryptedpwd = bytes(secret, "utf-8")
    uncipher_text = cipher_suite.decrypt(encryptedpwd)
    plain_text_encryptedpassword = bytes(uncipher_text).decode("utf-8")
    return plain_text_encryptedpassword"""
    )

    with open(CRYPTO_MODULE, "a", encoding="utf-8") as f:
        f.write("\n\n" + print_str + "\n")

    # crypto_module_stripped = CRYPTO_MODULE.split(".")[0]
    crypto_module_stripped = CRYPTO_MODULE.split(".", maxsplit=1)[0]

    print(f"\nfrom {crypto_module_stripped} import " + call_name)
    function_name_stripped = call_name[4:]
    print(f"{function_name_stripped} = {call_name}()")


if __name__ == "__main__":
    secret_text = input("Enter secret: ")
    function_name = input("Enter function name: ")
    generate_key_and_encrypt_password(secret_text, function_name)
