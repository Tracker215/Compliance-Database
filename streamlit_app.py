import streamlit as st

st.title("Compliance Database")
st.write(
    "Database for viewing compliance information"
    "
)
st.write("hello")

# Custom CSS to set specific dark purple background
st.markdown("""
    <style>
    .stApp {
        background-color: #100030;
        color: white;
    }
    .stTextInput > div > div > input {
        color: black;
        background-color: #f0f0f0;
    }
    .stButton > button {
        background-color: #4a148c;
        color: white;
    }
    h1, h2, h3, .stMarkdown {
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("Dark Purple Background App")
    
    # A simple input and button
    name = st.text_input("Enter your name:")
    
    if st.button("Greet Me"):
        if name:
            st.write(f"Hello, {name}!")
        else:
            st.write("Please enter a name")

if __name__ == "__main__":
    main()
