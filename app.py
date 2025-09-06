import streamlit as st
from langchain_ollama import OllamaEmbeddings
from langchain_qdrant import QdrantVectorStore
from dotenv import load_dotenv
import os
from litellm import completion
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="LegalAI | Motor Vehicle Act Assistant",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional SaaS theme
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Manrope:wght@400;500;600;700;800&display=swap');
    
    /* Main app styling */
    .stApp {
        background: #0f0f1a;
        color: #e6e6f0;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Navigation bar */
    .nav-container {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 70px;
        background: rgba(16, 16, 28, 0.95);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(138, 43, 226, 0.2);
        display: flex;
        align-items: center;
        padding: 0 2rem;
        z-index: 1000;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
    }
    
    .nav-logo {
        font-family: 'Manrope', sans-serif;
        font-size: 1.5rem;
        font-weight: 800;
        color: #fff;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        text-decoration: none;
    }
    
    .nav-logo span {
        background: linear-gradient(135deg, #8a2be2, #ff00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Dashboard layout */
    .dashboard-container {
        margin-top: 90px;
        padding: 2rem;
        display: grid;
        gap: 2rem;
    }
    
    .stats-container {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 1.5rem;
        margin-bottom: 2rem;
    }
    
    .stat-card {
        background: rgba(25, 25, 40, 0.6);
        border: 1px solid rgba(138, 43, 226, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(138, 43, 226, 0.2);
    }
    
    .stat-title {
        font-size: 0.875rem;
        color: #8a8aaa;
        margin-bottom: 0.5rem;
    }
    
    .stat-value {
        font-family: 'Manrope', sans-serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #fff;
        margin-bottom: 0.25rem;
    }
    
    .stat-trend {
        font-size: 0.875rem;
        color: #4caf50;
    }
    
    /* Main content area */
    .content-container {
        background: rgba(25, 25, 40, 0.4);
        border: 1px solid rgba(138, 43, 226, 0.2);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 2rem;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: rgba(30, 30, 50, 0.6) !important;
        border: 1px solid rgba(138, 43, 226, 0.3) !important;
        border-radius: 8px !important;
        color: #fff !important;
        font-size: 1rem !important;
        padding: 1rem !important;
        font-family: 'Inter', sans-serif !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #8a2be2 !important;
        box-shadow: 0 0 0 2px rgba(138, 43, 226, 0.2) !important;
        background: rgba(35, 35, 60, 0.8) !important;
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(135deg, #8a2be2, #ff00ff) !important;
        border: none !important;
        border-radius: 8px !important;
        color: #fff !important;
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        transition: all 0.3s ease !important;
        text-transform: none !important;
        letter-spacing: 0 !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 30px rgba(138, 43, 226, 0.3) !important;
    }
    
    /* Response container styling */
    .response-container {
        background: rgba(30, 30, 50, 0.4);
        border: 1px solid rgba(138, 43, 226, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1.5rem;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(16, 16, 28, 0.95) !important;
        border-right: 1px solid rgba(138, 43, 226, 0.2) !important;
    }
    
    /* Chat history styling */
    .chat-history {
        margin-top: 2rem;
    }
    
    .chat-item {
        background: rgba(30, 30, 50, 0.4);
        border: 1px solid rgba(138, 43, 226, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .chat-timestamp {
        font-size: 0.875rem;
        color: #8a8aaa;
        margin-bottom: 0.5rem;
    }
    
    /* Professional headings */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Manrope', sans-serif;
        font-weight: 700;
        color: #fff;
        margin-bottom: 1rem;
    }
    
    /* Loader styling */
    .stSpinner > div {
        border-color: #8a2be2 transparent #ff00ff transparent !important;
    }
    
    /* Alert styling */
    .stAlert {
        background: rgba(30, 30, 50, 0.4) !important;
        border: 1px solid rgba(138, 43, 226, 0.2) !important;
        border-radius: 8px !important;
    }
    
    /* Expander styling */
    .streamlit-expanderHeader {
        background: rgba(30, 30, 50, 0.4) !important;
        border: 1px solid rgba(138, 43, 226, 0.2) !important;
        border-radius: 8px !important;
        color: #fff !important;
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        padding: 1rem 2rem;
        background: rgba(30, 30, 50, 0.4);
        border: 1px solid rgba(138, 43, 226, 0.2);
        border-radius: 8px;
        color: #fff;
    }
    
    .stTabs [aria-selected="true"] {
        background: rgba(138, 43, 226, 0.2);
        border-color: #8a2be2;
    }
</style>
""", unsafe_allow_html=True)

# Navigation bar
st.markdown("""
<div class="nav-container">
    <a href="#" class="nav-logo">
        ⚖️ <span>LegalAI</span> | Motor Vehicle Act Assistant
    </a>
</div>
""", unsafe_allow_html=True)

def completion_llm(prompt):
    """Generate completion using LLM with streaming"""
    try:
        response = completion(
            model="ollama/llama3.2:latest",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a specialized legal assistant focused on the Motor Vehicle Act of India. Your role is to provide accurate summaries and interpretations of the Motor Vehicle Act provisions, regulations, and related legal content. When given passages from the Act, provide clear, concise explanations while maintaining legal accuracy."
                },
                {"role": "user", "content": prompt}
            ],
            api_base="http://localhost:11434",
            stream=True
        )
        
        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
        
        return full_response
    except Exception as e:
        return f"Error generating response: {str(e)}"

@st.cache_resource
def initialize_qdrant():
    """Initialize Qdrant connection with caching"""
    try:
        embeddings = OllamaEmbeddings(model="llama3.2:latest")
        url = "https://9731d9ce-cbf4-4495-b840-9b220a8cd953.us-west-1-0.aws.cloud.qdrant.io:6333"
        api_key = os.getenv("QDRANT_API_KEY")
        
        if not api_key:
            st.error("⚠️ API Key not found in environment variables")
            return None
        
        qdrant = QdrantVectorStore.from_existing_collection(
            embedding=embeddings,
            url=url,
            api_key=api_key,
            collection_name="Motor_Act",
        )
        return qdrant
    except Exception as e:
        st.error(f"⚠️ Connection error: {str(e)}")
        return None

def main():
    # Initialize session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'total_queries' not in st.session_state:
        st.session_state.total_queries = 0
    if 'successful_queries' not in st.session_state:
        st.session_state.successful_queries = 0
    
    # Dashboard container
    st.markdown('<div class="dashboard-container">', unsafe_allow_html=True)
    
    # Stats section
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    
    # Stat cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-title">Total Queries</div>
            <div class="stat-value">{}</div>
            <div class="stat-trend">↑ Active</div>
        </div>
        """.format(st.session_state.total_queries), unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-title">Success Rate</div>
            <div class="stat-value">{}%</div>
            <div class="stat-trend">↑ Optimal</div>
        </div>
        """.format(round(st.session_state.successful_queries / max(st.session_state.total_queries, 1) * 100)), unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-title">Response Time</div>
            <div class="stat-value">2.3s</div>
            <div class="stat-trend">↓ Fast</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="stat-card">
            <div class="stat-title">System Status</div>
            <div class="stat-value">Active</div>
            <div class="stat-trend">↑ Online</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Main content area
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    
    # Initialize Qdrant
    qdrant = initialize_qdrant()
    
    if qdrant is None:
        st.error("⚠️ System initialization failed. Please check your configuration.")
        st.markdown('</div>', unsafe_allow_html=True)
        return
    
    # Tabs for different sections
    tab1, tab2 = st.tabs(["📝 Query Assistant", "📊 History & Analytics"])
    
    with tab1:
        st.markdown("### Ask about Motor Vehicle Act")
        st.markdown("Enter your query about the Motor Vehicle Act of India. Our AI will provide accurate interpretations and summaries.")
        
        # Input section with better layout
        col1, col2 = st.columns([4, 1])
        
        with col1:
            question = st.text_input(
                "",
                placeholder="Type your legal query here...",
                key="question_input"
            )
        
        with col2:
            ask_button = st.button("Submit Query", key="ask_button")
        
        # Process question
        if ask_button and question:
            st.session_state.total_queries += 1
            
            with st.spinner("🔍 Analyzing relevant legal documents..."):
                try:
                    # Perform similarity search
                    search_results = qdrant.similarity_search(
                        query=question,
                        k=5
                    )
                    
                    # Create prompt for LLM
                    prompt = f"""
                    Question: {question}
                    Context: {search_results}
                    Only return the summary based on the provided content.
                    """
                    
                    # Generate response
                    with st.spinner("⚖️ Generating legal interpretation..."):
                        response = completion_llm(prompt)
                    
                    # Display response
                    st.markdown('<div class="response-container">', unsafe_allow_html=True)
                    st.markdown("#### Legal Analysis")
                    st.markdown(response)
                    st.markdown('</div>', unsafe_allow_html=True)
                    
                    # Update stats
                    st.session_state.successful_queries += 1
                    
                    # Add to chat history
                    st.session_state.chat_history.append({
                        'question': question,
                        'response': response,
                        'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")
                    })
                    
                except Exception as e:
                    st.error(f"⚠️ Processing error: {str(e)}")
    
    with tab2:
        st.markdown("### Query History & Analytics")
        
        # Display chat history with professional styling
        if st.session_state.chat_history:
            for chat in reversed(st.session_state.chat_history):
                with st.expander(f"Query: {chat['question'][:50]}..."):
                    st.markdown(f"**Timestamp:** {chat['timestamp']}")
                    st.markdown(f"**Question:** {chat['question']}")
                    st.markdown("**Analysis:**")
                    st.markdown(chat['response'])
        else:
            st.info("No queries yet. Start by asking a question about the Motor Vehicle Act.")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Professional footer
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; color: #8a8aaa; font-size: 0.875rem;">
        <p>LegalAI Motor Vehicle Act Assistant | Powered by Advanced AI Technology</p>
        <p style="font-size: 0.75rem;">© 2024 LegalAI. All rights reserved.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()