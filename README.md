# Python Secret Hashing

This is a small script that I use to hash and save secrets for use in Python scripts.

If you don't have access to a secret store like Vault and you don't want to use environment variables because your script might be copied and run from different locations then this is a good alternative.

## Requirements
The only requirement is the cryptoography package.
- https://pypi.org/project/cryptography/

You can get it by running:
```
pip install cryptography
```

## Usage

Edit the hashing_setup.py file on line 21 and enter the name you would like for your toml file and the name for your Python module that will hold the cryptographic functions. In the example below I used flokenes.toml and crypto_functions.py for my filenames, but you can use any name you'd like.

```
# TOML file name to write hashed secrets to
TOML_FILE = "flokenes.toml"

# Module to write the crypto functions to
CRYPTO_MODULE = "crypto_functions.py"
```

When you run hashing_setup.py it asks you to enter your secret, it takes that secret, hashes it, and saves it to the toml file using a random name as the descriptor. If the toml file does not exist it will create it with the name you specified.

The script will then create a Python function to read that line from the toml file, decrypt the hashed secret, and then return the secret as a string type variable. It will save this function in the filename you specified as the CRYPTO_MODULE. Again, if that file doesn't exist it will create it.

Lastly the script will give you the import statement you need to add to read that secret and the call you need to make to run the function and retrieve the secret as a variable.

```
Enter secret: user1234
Enter function name: get_widget_username

from crypto_functions import get_widget_username
widget_username = get_widget_username()


Enter secret: Password1234!
Enter function name: get_widget_password

from crypto_functions import get_widget_password
widget_password = get_widget_password()
```

This is what the contents of your toml file will look like:
```
[cXbnzAfR]
secret = gAAAAABknN1o_ZBwtyDCv5zK2VV_9Ofi01ALKDhj8oo83wrtcSVxS3UDhtxd7DcGDoaqy3lVF08HqQgFWi0RtmUp-RN7aG6cOw==

[VPkNRUNhzF]
secret = gAAAAABknNkipPJ8eNrZt5Ip1tnYvkp3cjPxR7WAG2XsB69o3he11ckE_yXqGAyHW9nT3qZ4QEmu_xOq9cpVa0f5FZQCLiCa5A==
```

This is what the contents of the CRYPTO_MODULE will look like:
```
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
```

And to tie it all together this is what the contents of your Python script will look like in order to access the secret:
```
from crypto_functions import get_widget_username, get_widget_password

def _connect_to_widget(widget_ip):
    widget_username = get_widget_username()
    widget_password = get_widget_password()
    .....
```

You can add as many secrets as you need for your script, hashing_setup.py will keep appending new ones to the end of the toml file and CRYPTO_MODULE.

Note!!! If you are syncing to GitHub you will want to add the toml file to your .gitignore. Even though they are encrypted you don't want the secrets out there for anyone to copy.

## License
This project is licensed under the terms of the MIT License.
