import streamlit as st
import pickle
import pandas as pd
from sklearn.linear_model import LogisticRegression

# Page configuration
st.set_page_config(
    page_title="Mental Health Prediction",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #2E86AB;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 3rem;
        font-style: italic;
    }
    
    .prediction-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .warning-box {
        background: linear-gradient(135deg, #ffeaa7 0%, #fab1a0 100%);
        padding: 15px;
        border-radius: 10px;
        color: #2d3436;
        text-align: center;
        margin: 20px 0;
    }
    
    .info-box {
        background: linear-gradient(135deg, #74b9ff 0%, #0984e3 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin: 20px 0;
    }
    
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #ddd;
        font-size: 16px;
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #00b894 0%, #00cec9 100%);
        color: white;
        border-radius: 25px;
        border: none;
        padding: 10px 30px;
        font-size: 18px;
        font-weight: bold;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Define the paths to the model and vectorizer files
model_path = 'trained_model.pkl'
vectorizer_path = 'vectorizer.pkl'

# Load the pre-trained model and vectorizer
try:
    with open(model_path, 'rb') as file:
        loaded_model = pickle.load(file)

    with open(vectorizer_path, 'rb') as file:
        loaded_vectorizer = pickle.load(file)

    # Header section
    st.markdown('<h1 class="main-header">🧠 Mental Health Condition Prediction</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">AI-powered analysis to help understand mental health patterns</p>', unsafe_allow_html=True)
    
    # Create columns for better layout
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Information box
        st.markdown("""
        <div class="info-box">
            <h3>ℹ️ How it works</h3>
            <p>Enter text describing your thoughts, feelings, or experiences, and our AI model will analyze patterns to predict potential mental health conditions. This tool is for educational purposes and should not replace professional medical advice.</p>
        </div>
        """, unsafe_allow_html=True)

        
        # Input section
        st.markdown("### 📝 Enter Your Text")
        user_input = st.text_area(
            "",
            placeholder="Describe your thoughts, feelings, or any mental health concerns you'd like to analyze...",
            height=150,
            help="Be as detailed as possible for better analysis"
        )

        # Prediction button
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔍 Analyze Mental Health Pattern"):
            if user_input.strip():
                with st.spinner("Analyzing your input..."):
                    # Transform the user input using the loaded vectorizer
                    sample_input_tfidf = loaded_vectorizer.transform([user_input])

                    # Make a prediction
                    prediction = loaded_model.predict(sample_input_tfidf)

                    # Display the prediction result with enhanced styling
                    st.markdown(f"""
                    <div class="prediction-box">
                        <h2>🎯 Analysis Result</h2>
                        <h3>Predicted Mental Health Condition:</h3>
                        <h1 style="font-size: 2.5rem; margin: 10px 0;">{prediction[0]}</h1>
                        <p style="font-size: 1.1rem; opacity: 0.9;">Please consult with a mental health professional for proper diagnosis and treatment.</p>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Additional information
                    st.markdown("### 📋 Important Notes")
                    st.info("🔹 This prediction is based on AI analysis and should not be considered a medical diagnosis.\n\n🔹 If you're experiencing mental health concerns, please reach out to a qualified healthcare provider.\n\n🔹 Crisis resources are available 24/7 if you need immediate support.")
                    
            else:
                st.markdown("""
                <div class="warning-box">
                    <h3>⚠️ Input Required</h3>
                    <p>Please enter some text describing your thoughts or feelings for analysis.</p>
                </div>
                """, unsafe_allow_html=True)

except FileNotFoundError:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #e17055 0%, #d63031 100%); padding: 20px; border-radius: 15px; color: white; text-align: center; margin: 20px 0;">
        <h2>❌ Error: Files Not Found</h2>
        <p>Model or vectorizer file not found. Please make sure 'trained_model.pkl' and 'vectorizer.pkl' are in the correct directory.</p>
    </div>
    """, unsafe_allow_html=True)
except Exception as e:
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #e17055 0%, #d63031 100%); padding: 20px; border-radius: 15px; color: white; text-align: center; margin: 20px 0;">
        <h2>❌ An Error Occurred</h2>
        <p>{e}</p>
    </div>
    """, unsafe_allow_html=True)
    
# Sidebar with additional information
with st.sidebar:
    st.markdown("### 📚 About This Tool")
    st.markdown("""
    This AI-powered tool uses machine learning to analyze text patterns and predict potential mental health conditions.
    
    **Features:**
    - 🤖 Advanced text analysis
    - 📊 Pattern recognition
    - 🎯 Instant predictions
    
    **Disclaimer:** This tool is for educational purposes only and should not replace professional medical advice.
    """)
    
    st.markdown("### 🆘 Mental Health Resources")
    st.markdown("""
    **Crisis Helplines:**
    - National Suicide Prevention Lifeline: +880 1779-554391
    - Crisis Text Line: Text HOME to 09612-119911
    - International Association for Suicide Prevention: [iasp.info](https://www.iasp.info)
    """)
    
    st.markdown("### 🏥 When to Seek Help")
    st.markdown("""
    Please consider professional help if you experience:
    - Persistent sadness or anxiety
    - Thoughts of self-harm
    - Significant life disruptions
    - Substance abuse issues
    - Difficulty functioning daily
    """)

# Footer with enhanced styling
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #2d3436 0%, #636e72 100%); border-radius: 15px; color: white; margin-top: 50px;'>
        <h3 style='color: #74b9ff; margin-bottom: 15px;'>🎓 Green University Of Bangladesh</h3>
        <p style='font-size: 16px; margin-bottom: 10px;'>Mental Health Prediction System</p>
        <p style='font-size: 14px; opacity: 0.8;'>Developed by: Manik Biswas • Shovro Nandi • Sudipta Biswas Puja</p>
        <p style='font-size: 12px; opacity: 0.6; margin-top: 15px;'>🤝 Empowering mental health awareness through AI technology</p>
    </div>
    """,
    unsafe_allow_html=True)