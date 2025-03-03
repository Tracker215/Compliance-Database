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
    st.title("Compliance Database")
    st.write("Database for viewing compliance information")
    st.write("Hello")
    
    st.header("Main Page Details")
    st.write("Welcome to the main section of our application.")
    
    # Additional main page content
    st.write("This is the home page with general information.")
    
    # Add a table or some sample data
    st.subheader("Compliance Overview")
    compliance_data = {
        'Category': ['Safety', 'Environmental', 'Regulatory'],
        'Status': ['Compliant', 'Pending Review', 'Compliant']
    }
    st.table(compliance_data)

def electrical_page():
    st.header("Electrical Compliance")
    st.write("Explore electrical engineering compliance topics and resources.")
    
    # Electrical-specific compliance content
    st.subheader("Electrical Systems Compliance")
    st.write("Detailed information about electrical systems compliance and regulations.")
    
    # Sample electrical compliance data
    electrical_compliance = {
        'Standard': ['IEEE 1584', 'NFPA 70E', 'IEC 60364'],
        'Compliance Level': ['Full', 'Partial', 'Full']
    }
    st.table(electrical_compliance)

def mechanical_page():
    st.header("Mechanical Compliance")
    st.write("Dive into mechanical engineering compliance insights.")
    
    # Mechanical-specific compliance content
    st.subheader("Mechanical Systems Compliance")
    st.write("Details about mechanical design compliance, standards, and regulations.")
    
    # Sample mechanical compliance data
    mechanical_compliance = {
        'Standard': ['ISO 9001', 'ASME Y14.5', 'ISO 13485'],
        'Compliance Status': ['Compliant', 'Under Review', 'Compliant']
    }
    st.table(mechanical_compliance)

def main():
    # Sidebar menu
    st.sidebar.title("Compliance Navigation")
    
    # Create radio button for menu selection
    menu_selection = st.sidebar.radio(
        "Select Compliance Section", 
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
