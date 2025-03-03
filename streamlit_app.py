import streamlit as st

st.title("🎈 My new app app ")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.write("hello")


# Custom CSS to set purple background
st.markdown("""
    <style>
    .stApp {
        background-color: purple;
        color: white;
    }
    .stTextInput > div > div > input {
        color: black;
    }
    .stButton > button {
        background-color: lavender;
        color: purple;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("Purple Background Streamlit App")
    
    # A simple input and button
    name = st.text_input("Enter your name:")
    
    if st.button("Greet Me"):
        if name:
            st.write(f"Hello, {name}!")
        else:
            st.write("Please enter a name")

if __name__ == "__main__":
    main()
