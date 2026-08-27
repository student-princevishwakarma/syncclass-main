import streamlit as st

def footer_home():

    st.markdown(f"""
        <div style='margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center;'>
            <p style='font-weight:bold; color:white'/>Created with ❤️ by </p>
            <img style="width:100%; max-width:100px; height:auto; margin-bottom:10px;" src="https://i.ibb.co/HTTd1q29/logo-bitofprince.png" alt="BITOFPRINCE">
        </div>

                """
                , unsafe_allow_html=True)

    
def footer_dashboard():

    st.markdown(f"""
        <div style='margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center;'>
            <p style='font-weight:bold; color:black'/>Created with ❤️ by </p>
            <img style="width:100%; max-width:100px; height:auto; margin-bottom:10px;" src="https://i.ibb.co/HTTd1q29/logo-bitofprince.png" alt="BITOFPRINCE">
        </div>

                """
                , unsafe_allow_html=True)