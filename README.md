# Python Secret Hashing

This is a small script that I use to hash and save secrets for use in Python scripts.

If you don't have access to a secret store like Vault and you don't want to use environment variables because your script might be copied and run from different locations then this is a good alternative.

## Usage

When you run hashing_setup.py it asks you to enter your secret, it takes that secret and hashes it and saves it to a .toml file.

The script will then create a Python function to read that line from the toml file and decrypt it and save the secret as a string type variable.




## License
This project is licensed under the terms of the MIT License.
