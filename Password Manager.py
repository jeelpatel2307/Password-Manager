import os
import json
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, master_password):
        # Derive a key from the master password using PBKDF2
        self.key = self.derive_key(master_password.encode())

        # Initialize an empty dictionary to store passwords
        self.passwords = {}

    def derive_key(self, password):
        # Use PBKDF2 to derive a key from the password
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            iterations=100000,
            salt=os.urandom(16),
            length=32,
            backend=default_backend()
        )
        return Fernet(base64.urlsafe_b64encode(kdf.derive(password)))

    def encrypt(self, data):
        # Encrypt data using the derived key
        return self.key.encrypt(data.encode())

    def decrypt(self, encrypted_data):
        # Decrypt data using the derived key
        return self.key.decrypt(encrypted_data).decode()

    def save_password(self, website, username, password):
        # Encrypt and store the password for a website
        encrypted_password = self.encrypt(password)
        self.passwords[website] = {'username': username, 'password': encrypted_password}

    def get_password(self, website):
        # Retrieve and decrypt the password for a website
        if website in self.passwords:
            encrypted_password = self.passwords[website]['password']
            return self.decrypt(encrypted_password)
        else:
            return None

    def save_to_file(self, file_path):
        # Save the encrypted passwords to a JSON file
        with open(file_path, 'w') as file:
            json.dump(self.passwords, file)

    def load_from_file(self, file_path):
        # Load and decrypt passwords from a JSON file
        with open(file_path, 'r') as file:
            self.passwords = json.load(file)
            for website, data in self.passwords.items():
                data['password'] = self.decrypt(data['password'])

if __name__ == '__main__':
    # Example usage
    master_password = input("Enter your master password: ")
    password_manager = PasswordManager(master_password)

    # Save passwords
    password_manager.save_password('example.com', 'user123', 'securePassword123')
    password_manager.save_password('another-site.com', 'admin', 'strongPass456')

    # Get passwords
    print("Password for example.com:", password_manager.get_password('example.com'))
    print("Password for non-existent-site.com:", password_manager.get_password('non-existent-site.com'))

    # Save and load passwords to/from a file
    file_path = 'passwords.json'
    password_manager.save_to_file(file_path)

    # Create a new PasswordManager instance and load passwords from the file
    new_password_manager = PasswordManager(master_password)
    new_password_manager.load_from_file(file_path)

    # Display the loaded passwords
    print("\nPasswords loaded from file:")
    for website, data in new_password_manager.passwords.items():
        print(f"{website}: {data['username']}, {data['password']}")
