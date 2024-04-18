import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['hello']).generate()
print(hashed_passwords)

from streamlit_authenticator.utilities.hasher import Hasher
hashed_passwords = Hasher(['brijesh']).generate()
print(hashed_passwords)