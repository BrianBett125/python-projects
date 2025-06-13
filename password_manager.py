import os
import json
import base64
import hashlib

DATA_FILE = "vault.json"

def derive_key(master_password):
    """Derive a consistent key from the master password using SHA-256."""
    return hashlib.sha256(master_password.encode()).digest()

def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    """Encrypt or decrypt data using XOR with a repeating key."""
    return bytes([b ^ key[i % len(key)] for i, b in enumerate(data)])

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def encrypt_password(password, key):
    encrypted = xor_encrypt_decrypt(password.encode(), key)
    return base64.b64encode(encrypted).decode()

def decrypt_password(encrypted, key):
    try:
        encrypted_bytes = base64.b64decode(encrypted.encode())
        decrypted = xor_encrypt_decrypt(encrypted_bytes, key)
        return decrypted.decode()
    except Exception:
        return "[Decryption Failed]"

def add_entry(site, username, password, key):
    data = load_data()
    encrypted = encrypt_password(password, key)
    data[site] = {"username": username, "password": encrypted}
    save_data(data)
    print(f"✅ Entry for '{site}' added.")

def view_entries(key):
    data = load_data()
    if not data:
        print("🗃️ No entries found.")
        return
    for site, creds in data.items():
        print(f"\n🔐 Site: {site}")
        print(f"👤 Username: {creds['username']}")
        print(f"🔑 Password: {decrypt_password(creds['password'], key)}")

def main():
    print("🔒 Welcome to Your Terminal Password Manager")
    master = input("Enter master password: ")
    key = derive_key(master)

    while True:
        print("\nOptions: [add] [view] [exit]")
        cmd =

