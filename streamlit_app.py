import streamlit as st

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
    h1, h2, h3, .stMarkdown, .stLabel {
        color: white !important;
    }
    .stSidebar {
        background-color: #1a0047;
    }
    .stSidebar .stButton {
        background-color: #4a148c;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

def main_page():

    st.header("Main Page")
    st.write("Welcome to the main section of our application.")
    
    # Additional main page content
    st.write("This is the home page with general information.")

def electrical_page():
    st.header("Electrical Section")
    st.write("Explore electrical engineering topics and resources.")
    
    # Electrical-specific content
    st.subheader("Electrical Systems")
    st.write("Information about electrical systems, circuits, and components.")

def mechanical_page():
    st.header("Mechanical Section")
    st.write("Dive into mechanical engineering insights.")
    
    # Mechanical-specific content
    st.subheader("Mechanical Systems")
    st.write("Details about mechanical design, machinery, and engineering principles.")

def main():
    # Sidebar menu
    st.sidebar.title("Navigation Menu")
    
    # Create radio button for menu selection
    menu_selection = st.sidebar.radio(
        "Go to", 
        ["Main", "Electrical", "Mechanical"]
    )
    
    # Page routing based on menu selection
    if menu_selection == "Main":
        main_page()
    elif menu_selection == "Electrical":
        electrical_page()
    elif menu_selection == "Mechanical":
        mechanical_page()

if __name__ == "__main__":
    main()
