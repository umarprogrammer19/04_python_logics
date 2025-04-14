
import streamlit as st
import time

# Set page configuration
st.set_page_config(page_title="My Awesome Website", page_icon="🌟", layout="wide")

# Custom CSS Styling
st.markdown("""
    <style>
    body {
        background-color: black;
        color:white,
    }
    .main {
        color:white,
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
        margin: 1rem;
    }
    .big-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 3rem;

        text-align: center;
        margin-bottom: 1rem;
    }
    .subtitle {
        font-size: 1.5rem;

        text-align: center;
        margin-bottom: 1rem;
    }
    .footer {
        text-align: center;
        font-size: 0.9rem;

        padding: 1rem;
        border-top: 1px solid #ddd;
        margin-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About",  "Contact"])

# Home Page
if page == "Home":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>Welcome to My Awesome Website!</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Where creativity meets technology.</p>", unsafe_allow_html=True)
    st.image("https://picsum.photos/1200/400", use_column_width=True, caption="A Glimpse of Creativity")
    st.write("""
        Hello and welcome! This website is built using **Streamlit** and showcases a blend of design and functionality.
        Navigate through the pages using the sidebar to explore more about me, my work, and get in touch.
    """)
    st.markdown("</div>", unsafe_allow_html=True)

# About Page
elif page == "About":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>About Me</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>My Journey & Passion</p>", unsafe_allow_html=True)
    st.image("https://picsum.photos/800/300", use_column_width=True, caption="A snippet of my journey")
    st.write("""
        Hi, I'm a passionate developer and creative thinker. My journey started with a simple 'Hello World' and has evolved into building interactive and dynamic web applications.
        I love exploring new technologies and translating creative ideas into digital experiences.
    """)
    st.markdown("</div>", unsafe_allow_html=True)



# Contact Page
elif page == "Contact":
    st.markdown("<div class='main'>", unsafe_allow_html=True)
    st.markdown("<h1 class='big-title'>Get in Touch</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>We'd love to hear from you!</p>", unsafe_allow_html=True)

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Send Message")
        if submitted:
            st.success("Thank you for your message! I'll get back to you soon.")
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Made by ❤️ Ayesha Aziz</div>", unsafe_allow_html=True)
