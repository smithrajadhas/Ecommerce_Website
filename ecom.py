import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth


cred = credentials.Certificate('ecom-tutorial-9e9b1-1c58945823d4.json')
firebase_admin.initialize_app(cred)



def app():
    st.title("Welcome to Ecom Store")
    choice = st.selectbox('Login / Signup', ["Login","Sign Up"])
    
    if choice == 'Login':
        user_name = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        
        st.button('Login')
    
    else:
        email = st.text_input("Email")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        user_name = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        
        if st.button('Create Account'):
            user = auth.create_user(uid = username, password = password)
            
            st.success("Account Created Sucessfully")
            st.markdown("Please Login using Username and Password")
            st.balloons()
    
        