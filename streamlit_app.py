import streamlit as st

# Enhanced CSS to improve text visibility
st.markdown("""
    <style>
    /* Ensure all text is visible */
    body, .stMarkdown, .stText, .stTextInput > div > div > input, 
    .stButton > button, h1, h2, h3, h4, h5, h6 {
        color: white !important;
    }
    
    .stApp {
        background-color: #100030;
    }
    
    .stTextInput > div > div > input {
        background-color: #2a2a2a !important;
        color: white !important;
    }
    
    .stButton > button {
        background-color: #4a148c !important;
        color: white !important;
    }
    
    .stTable {
        color: white !important;
    }
    
    .stTable th {
        background-color: #4a148c !important;
        color: white !important;
    }
    
    .stTable td {
        background-color: #1a0047 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main_page():
    # Large, bold title to ensure visibility
    st.markdown("<h1 style='color: white; text-align: center;'>Compliance Database</h1>", unsafe_allow_html=True)
    
    # Ensure multiple ways of adding text
    st.markdown("<p style='color: white; font-size: 18px;'>Database for viewing compliance information</p>", unsafe_allow_html=True)
    
    # Use st.write with explicit color
    st.write("<p style='color: white; font-size: 16px;'>Hello, this is the main compliance page.</p>", unsafe_allow_html=True)
    
    # Another method to ensure text visibility
    st.markdown("""
    <div style='color: white; background-color: #1a0047; padding: 10px; border-radius: 5px;'>
    <h2 style='color: white;'>Main Page Details</h2>
    <p style='color: white;'>Welcome to the main section of our application.</p>
    <p style='color: white;'>This is the home page with general information.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Table with explicit styling
    st.markdown("<h3 style='color: white;'>Compliance Overview</h3>", unsafe_allow_html=True)
    compliance_data = {
        'Category': ['Safety', 'Environmental', 'Regulatory'],
        'Status': ['Compliant', 'Pending Review', 'Compliant']
    }
    st.dataframe(compliance_data, use_container_width=True)

def electrical_page():
    st.markdown("<h1 style='color: white;'>Electrical Compliance</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: white;'>Explore electrical engineering compliance topics and resources.</p>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='color: white;'>Electrical Systems Compliance</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: white;'>Detailed information about electrical systems compliance and regulations.</p>", unsafe_allow_html=True)
    
    electrical_compliance = {
        'Standard': ['IEEE 1584', 'NFPA 70E', 'IEC 60364'],
        'Compliance Level': ['Full', 'Partial', 'Full']
    }
    st.dataframe(electrical_compliance, use_container_width=True)

def mechanical_page():
    st.markdown("<h1 style='color: white;'>Mechanical Compliance</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color: white;'>Dive into mechanical engineering compliance insights.</p>", unsafe_allow_html=True)
    
    st.markdown("<h2 style='color: white;'>Mechanical Systems Compliance</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: white;'>Details about mechanical design compliance, standards, and regulations.</p>", unsafe_allow_html=True)
    
    mechanical_compliance = {
        'Standard': ['ISO 9001', 'ASME Y14.5', 'ISO 13485'],
        'Compliance Status': ['Compliant', 'Under Review', 'Compliant']
    }
    st.dataframe(mechanical_compliance, use_container_width=True)

def main():
    # Sidebar with contrasting colors
    st.sidebar.markdown("<h2 style='color: white;'>Compliance Navigation</h2>", unsafe_allow_html=True)
    
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
