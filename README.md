# Password Manager

Welcome to the Password Manager! This Python project provides a simple password manager that securely stores and manages passwords using encryption.

## How to Use

1. Run the script (`password_manager.py`).
2. Enter your master password when prompted.
3. Save, retrieve, and manage passwords securely.

## Features

### `PasswordManager` Class

- Manages encryption, decryption, and storage of passwords.
- Uses PBKDF2 for key derivation and Fernet symmetric encryption.

### Methods

### `save_password(website, username, password)`

- Encrypts and stores a password for a given website.

### `get_password(website)`

- Retrieves and decrypts the password for a given website.

### `save_to_file(file_path)`

- Saves encrypted passwords to a JSON file.

### `load_from_file(file_path)`

- Loads and decrypts passwords from a JSON file.

## Example Usage

```python
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
print("\\nPasswords loaded from file:")
for website, data in new_password_manager.passwords.items():
    print(f"{website}: {data['username']}, {data['password']}")

```

## Security Considerations

- **Master Password:**
    - Handle master passwords securely, ensuring they are not displayed on the screen during input.
- **Encryption:**
    - The project uses Fernet symmetric encryption. In a production environment, consider industry-standard encryption practices.
- **File Storage:**
    - Passwords are stored in a JSON file. Ensure the security of this file and consider additional security measures.

## Author

Jeel patel
