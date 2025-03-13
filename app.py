import streamlit as st
from models.pseudo_to_code import PseudoToCode
from models.code_to_pseudo import CodeToPseudo

# Set page config with a bright/light theme look
st.set_page_config(
    page_title="Pseudocode to C++ Code and C++ Code to Pseudocode Generator",
    page_icon=":sparkles:",
    layout="wide",
)

# Inject custom CSS to enforce a bright theme
st.markdown(
    """
    <style>
    body {
        background-color:rgb(0, 0, 0);
        color: #000000;
    }
    .stApp {
        background-color:rgb(0, 0, 0);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    /* Footer styling */
    .footer {
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #e0e0e0;
        text-align: center;
        color: #666;
    }
    
    /* Creator profiles */
    .creator-profiles {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-top: 10px;
    }
    .creator-profile {
        text-align: center;
    }
    .linkedin-button {
        display: inline-block;
        background-color: #0077B5;
        color: white !important;
        text-decoration: none;
        padding: 5px 10px;
        border-radius: 5px;
        font-size: 0.8rem;
        margin-top: 5px;
        transition: background-color 0.3s;
    }
    .linkedin-button:hover {
        background-color: #005582;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Use Streamlit's cache_resource for model initialization
@st.cache_resource
def load_pseudo_to_code_model():
    return PseudoToCode()

@st.cache_resource
def load_code_to_pseudo_model():
    return CodeToPseudo()

# Initialize models with caching
pseudo_to_code_model = load_pseudo_to_code_model()
code_to_pseudo_model = load_code_to_pseudo_model()

# Add session state to keep track of user inputs
if 'pseudocode_input' not in st.session_state:
    st.session_state.pseudocode_input = ""
if 'cpp_code_input' not in st.session_state:
    st.session_state.cpp_code_input = ""

# Streamlit application title
st.title("Pseudocode to C++ Code and C++ Code to Pseudocode Generator")

# Sidebar for user input
st.sidebar.header("User Input")

# Option to choose the conversion type
conversion_type = st.sidebar.selectbox("Select Conversion Type", 
                                       ("Pseudocode to C++ Code", "C++ Code to Pseudocode"))

# Input text area for pseudocode or C++ code
if conversion_type == "Pseudocode to C++ Code":
    pseudocode_input = st.text_area("Enter Pseudocode:", value=st.session_state.pseudocode_input)
    st.session_state.pseudocode_input = pseudocode_input
    
    if st.button("Generate C++ Code"):
        if pseudocode_input:
            with st.spinner("Generating C++ code..."):
                cpp_code = pseudo_to_code_model.generate_code(pseudocode_input)
            st.subheader("Generated C++ Code:")
            st.code(cpp_code, language="cpp")
        else:
            st.error("Please enter pseudocode to generate C++ code.")
else:
    cpp_code_input = st.text_area("Enter C++ Code:", value=st.session_state.cpp_code_input)
    st.session_state.cpp_code_input = cpp_code_input
    
    if st.button("Generate Pseudocode"):
        if cpp_code_input:
            with st.spinner("Generating pseudocode..."):
                pseudocode = code_to_pseudo_model.generate_pseudocode(cpp_code_input)
            st.subheader("Generated Pseudocode:")
            st.code(pseudocode)
        else:
            st.error("Please enter C++ code to generate pseudocode.")

# Add some information about the app and the creators
with st.expander("About this app"):
    st.write("""
    This application uses deep learning models to convert between pseudocode and C++ code.
    - The pseudocode to code model translates algorithmic descriptions into executable C++ code.
    - The code to pseudocode model extracts the algorithmic logic from C++ code into human-readable pseudocode.
    """)

# Footer with developer credits
st.markdown("""
<div class="footer">
    <p>Developed by:</p>
    <div class="creator-profiles">
        <div class="creator-profile">
            <p><strong>Ali Mustafa</strong></p>
            <a href="https://www.linkedin.com/in/alii-mustafa-" class="linkedin-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg> LinkedIn
            </a>
        </div>
        <div class="creator-profile">
            <p><strong>Fasih Zaidi</strong></p>
            <a href="https://www.linkedin.com/in/syed-fasih-zaidi-60643a255/" class="linkedin-button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg> LinkedIn
            </a>
        </div>
    </div>
    <p style="margin-top: 20px; font-size: 0.8rem;">© 2025 PseudoCode <-> C++ Code</p>
</div>
""", unsafe_allow_html=True)