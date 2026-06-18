import streamlit as st
st.title("👨‍💻 Muhammad Minhaj kp")
st.header("About Me", divider="blue")
st.write("""
Hi, I'm Muhammad Minhaj.

I am a BCA student who is learning Python,
Data Analysis, and Web Development.

Currently I am learning Streamlit to build
interactive web applications using Python.
""")
st.header("Skills", divider="green")

st.markdown(
    "- **Python**\n"
    "- Streamlit\n"
    "- Pandas\n"
    "- NumPy\n"
    "- HTML & CSS\n"
    "- SQL"
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

st.write("📧 Email: minhajjjjjj@example.com")

st.write("📱 Phone: +91 XXXXX XXXXX")

st.write("🌐 Portfolio: coming soon")