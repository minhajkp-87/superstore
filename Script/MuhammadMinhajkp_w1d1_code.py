import streamlit as st
st.title("👨‍💻 Muhammad Minhaj kp")
st.header("About Me", divider="blue")
st.write("""
Hi, I'm Minhaj.

I am a BCA student who is learning Python,
Data Analysis, and Web Development.

Currently I am learning Streamlit to build
interactive web applications using Python.
""")
st.header("Skills", divider="green")

st.markdown(
    "- Python\n"
    "- HTML\n"
    "- CSS\n"
    "- Web Development\n"
    "- Data Cleaning\n"
)
st.subheader(
    "Favourite Python Snippet",
    help="Simple Hello World Program"
)

st.code("""
name = "Minhaj"
print("Hello", name)
""", language="python")
st.header("Contact", divider="orange")

st.write("📧 Email: minhajkp.bca25.dbi@gmail.com")

st.write("📱 Phone: +91 0123456789")

st.write("🌐 Portfolio: coming soon")
st.markdown("---")

st.caption("Week 1 Day 1 Project")