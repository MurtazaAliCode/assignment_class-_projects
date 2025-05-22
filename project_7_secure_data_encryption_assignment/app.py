import streamlit as st
import base64
import hashlib
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

# --- Session Initialization ---
if "data_store" not in st.session_state:
    st.session_state.data_store = {}
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "authenticated" not in st.session_state:
    st.session_state.authenticated = True
if "user_password" not in st.session_state:
    st.session_state.user_password = None
if "remaining_chances" not in st.session_state:
    st.session_state.remaining_chances = 3

# --- Dummy login credentials ---
VALID_USERNAME = "admin"
VALID_PASSWORD = "pass123"

# --- Key derivation using passkey ---
def create_fernet_key(passkey: str) -> Fernet:
    password = passkey.encode()
    salt = b'streamlit-secure-salt'  # Fixed salt for demo
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return Fernet(key)

# --- Encryption/Decryption ---
def encrypt_data(data: str, key: Fernet):
    return key.encrypt(data.encode())

def decrypt_data(encrypted_data: bytes, key: Fernet):
    return key.decrypt(encrypted_data).decode()

# --- Login Page ---
def login():
    st.title("🔐 Reauthorization Required")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == VALID_USERNAME and password == VALID_PASSWORD:
            st.session_state.authenticated = True
            st.session_state.failed_attempts = 0
            st.session_state.remaining_chances = 3
            st.success("Logged in successfully!")
        else:
            st.error("Invalid credentials")

# --- Main App Logic ---
def main_app():
    st.title("🗄️ Secure In-Memory Data Storage")
    menu = st.sidebar.selectbox("Choose Action", ["Store Data", "Retrieve Data"])

    if menu == "Store Data":
        key = st.text_input("Enter a unique passkey", type="password")
        data = st.text_area("Enter data to store")

        if st.button("Encrypt and Store"):
            if key and data:
                fernet = create_fernet_key(key)
                encrypted = encrypt_data(data, fernet)
                st.session_state.data_store[key] = encrypted
                st.success("Data encrypted and stored successfully!")
            else:
                st.warning("Both passkey and data are required.")

    elif menu == "Retrieve Data":
        key = st.text_input("Enter your passkey to retrieve data", type="password")

        if st.button("Retrieve"):
            if key in st.session_state.data_store:
                try:
                    fernet = create_fernet_key(key)
                    decrypted = decrypt_data(st.session_state.data_store[key], fernet)
                    st.success("Decrypted Data:")
                    st.code(decrypted)
                    st.session_state.failed_attempts = 0
                    st.session_state.remaining_chances = 3
                except InvalidToken:
                    st.session_state.failed_attempts += 1
                    st.session_state.remaining_chances -= 1
                    st.error(f"❌ Incorrect passkey! Chances left: {st.session_state.remaining_chances}")
            else:
                st.session_state.failed_attempts += 1
                st.session_state.remaining_chances -= 1
                st.error(f"❌ No data found for this passkey! Chances left: {st.session_state.remaining_chances}")

            if st.session_state.failed_attempts >= 3:
                st.session_state.authenticated = False

# --- Routing ---
if not st.session_state.authenticated:
    login()
else:
    main_app()
