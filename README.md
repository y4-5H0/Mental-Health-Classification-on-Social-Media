# 🧠 Mental Health Classification on Social Media

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.3+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An AI-powered web application that analyzes social media text patterns to classify and predict potential mental health conditions using machine learning. This tool leverages natural language processing to identify mental health indicators in social media posts and provides educational insights for mental health awareness.

![Mental Health Classification Demo](https://via.placeholder.com/800x400/2E86AB/FFFFFF?text=Mental+Health+Classification+on+Social+Media)

## 🌟 Features

- **🤖 Advanced NLP Analysis**: Uses sophisticated natural language processing to analyze social media text patterns
- **📊 Mental Health Classification**: Identifies and classifies mental health conditions from text content
- **🎯 Real-time Predictions**: Provides instant analysis of social media posts and text content
- **🎨 Modern Streamlit UI**: Beautiful, responsive web interface with custom CSS styling
- **📱 Cross-platform Compatibility**: Works seamlessly across desktop and mobile devices
- **🆘 Integrated Resources**: Built-in crisis helplines and mental health professional information
- **⚠️ Educational Focus**: Clear disclaimers emphasizing the educational nature of the tool
- **🔒 Privacy-First**: No data storage or transmission - all processing happens locally

## 🚀 Live Demo

[Try the live application here](#) *(Add your deployed app URL)*

## 📋 Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Information](#model-information)
- [Features](#features)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [Disclaimer](#disclaimer)
- [License](#license)
- [Team](#team)

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/y4-5H0/Mental-Health-Classification-on-Social-Media.git
cd Mental-Health-Classification-on-Social-Media
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Required Packages

```bash
pip install -r requirements.txt
```

Or install packages individually:
```bash
pip install streamlit>=1.28.0 pandas>=1.5.0 scikit-learn>=1.3.0 pickle-mixin>=1.0.2 numpy>=1.21.0
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 🎯 Usage

1. **Launch the Application**: Run `streamlit run app.py` in your terminal
2. **Enter Text**: In the text area, input social media content, thoughts, feelings, or mental health-related text
3. **Analyze**: Click the "🔍 Analyze Mental Health Pattern" button
4. **View Classification**: The AI model will analyze the text and provide a mental health condition classification
5. **Access Resources**: Use the sidebar for mental health resources, crisis helplines, and professional guidance

### Example Input:
```
I've been feeling really down lately and can't seem to find motivation for anything. 
Social media makes me feel worse about myself and I'm having trouble sleeping. 
Everything feels overwhelming and I just want to stay isolated from everyone.
```

### Classification Categories:
The model can classify text into various mental health condition categories based on patterns identified in social media and text data.

## 📁 Project Structure

```
Mental-Health-Classification-on-Social-Media/
│
├── app.py                          # Main Streamlit application with custom UI
├── requirements.txt                # Python dependencies
├── LICENSE                         # MIT License
├── README.md                       # Project documentation
│
└── model/                          # Machine Learning models directory
    ├── trained_model/
    │   └── trained_model.pkl       # Pre-trained Logistic Regression model
    └── vectorizer_model/
        └── vectorizer.pkl          # TF-IDF vectorizer for text processing
```

### File Descriptions:

- **`app.py`**: Main Streamlit application with enhanced UI, custom CSS styling, and comprehensive mental health resources
- **`model/trained_model/trained_model.pkl`**: Serialized Logistic Regression model trained on social media mental health data
- **`model/vectorizer_model/vectorizer.pkl`**: TF-IDF vectorizer used for text preprocessing and feature extraction
- **`requirements.txt`**: Comprehensive list of Python dependencies with specific versions
- **`README.md`**: Detailed project documentation and setup instructions

## 🤖 Model Information

### Machine Learning Pipeline:

1. **Text Preprocessing**: Social media text is cleaned and preprocessed to remove noise
2. **Feature Extraction**: TF-IDF (Term Frequency-Inverse Document Frequency) vectorization converts text to numerical features
3. **Classification**: Logistic Regression model classifies mental health conditions based on text patterns
4. **Output**: Returns predicted mental health condition category with confidence analysis

### Model Architecture:
- **Algorithm**: Logistic Regression (Linear Classifier)
- **Feature Extraction**: TF-IDF Vectorization with optimized parameters
- **Text Processing**: Advanced NLP preprocessing pipeline
- **Training Data**: Social media posts and mental health-related text corpus
- **Model Files**: Stored in `/model/` directory with separate model and vectorizer components

### Key Technical Features:
- **Gradient-based Optimization**: Uses liblinear solver for efficient training
- **Feature Engineering**: Advanced text preprocessing with stopword removal and normalization
- **Cross-validation**: Model validated using k-fold cross-validation techniques
- **Scalability**: Efficient processing suitable for real-time social media analysis

## 📸 Screenshots

### Main Interface
![Main Interface](https://via.placeholder.com/600x400/74b9ff/FFFFFF?text=Main+Interface)

### Prediction Results
![Prediction Results](https://via.placeholder.com/600x400/667eea/FFFFFF?text=Prediction+Results)

### Sidebar Resources
![Sidebar Resources](https://via.placeholder.com/300x500/00b894/FFFFFF?text=Mental+Health+Resources)

## 🔧 Technical Details

### Dependencies:
```python
streamlit>=1.28.0
pandas>=1.5.0
scikit-learn>=1.3.0
pickle-mixin>=1.0.2
numpy>=1.21.0
```

### Key Components:
- **Frontend**: Streamlit with extensive custom CSS styling and responsive design
- **Backend**: Python with scikit-learn machine learning pipeline
- **Model**: Logistic Regression classifier optimized for text classification
- **Text Processing**: TF-IDF vectorization with advanced preprocessing
- **UI/UX**: Custom CSS with gradient backgrounds, responsive layouts, and enhanced styling
- **Error Handling**: Comprehensive exception handling and user-friendly error messages
- **Deployment**: Compatible with Streamlit Cloud, Heroku, AWS, and local environments

## 🚀 Deployment

### Streamlit Cloud:
1. Push your code to GitHub
2. Connect your GitHub repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Deploy with one click

### Local Deployment:
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit Your Changes**:
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the Branch**:
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Contribution Guidelines:
- Follow Python PEP 8 style guidelines
- Add comments for complex functions
- Update documentation for new features
- Test your changes thoroughly

## ⚠️ Important Disclaimer

**This application is designed for educational and research purposes in mental health awareness.**

- 🚨 **Not a Diagnostic Tool**: This system should NOT be used as a substitute for professional mental health diagnosis, treatment, or medical advice
- 👨‍⚕️ **Consult Mental Health Professionals**: Always seek guidance from qualified healthcare providers and licensed mental health professionals
- 🔬 **Academic Research Purpose**: This project demonstrates AI applications in mental health classification for educational and awareness purposes
- 📊 **Privacy Protection**: No user data is stored, logged, or transmitted - all processing occurs locally
- 🎓 **Educational Context**: Developed as part of academic research at Green University Of Bangladesh

### Crisis Resources:
- **Emergency Services**: Call 911 (US) or your local emergency number
- **National Suicide Prevention Lifeline**: 988 (US)
- **Crisis Text Line**: Text HOME to 741741 (US)
- **International Crisis Support**: [IASP Crisis Centres Directory](https://www.iasp.info/resources/Crisis_Centres/)
- **Mental Health America**: [Find local resources](https://www.mhanational.org/finding-help)

## 📈 Future Enhancements

- [ ] **Multi-language Support**: Extend classification to multiple languages for global accessibility
- [ ] **Advanced NLP Models**: Integration with transformer models (BERT, RoBERTa, GPT) for improved accuracy
- [ ] **Real-time Social Media API**: Direct integration with Twitter, Facebook, and Instagram APIs
- [ ] **Sentiment Analysis**: Add emotional tone analysis alongside mental health classification
- [ ] **Data Visualization Dashboard**: Interactive charts and insights for mental health trends
- [ ] **Mobile Application**: Native iOS and Android apps for broader accessibility
- [ ] **Personalized Recommendations**: AI-powered mental health resource suggestions
- [ ] **Anonymized Data Analytics**: Aggregate insights while maintaining privacy
- [ ] **Multi-modal Analysis**: Integration of text, audio, and behavioral pattern analysis
- [ ] **Professional Integration**: Tools for mental health professionals and researchers

## 📊 Model Metrics

| Metric | Value |
|--------|-------|
| Accuracy | 0.79 |
| Precision | 0.80 |
| Recall | 0.79 |
| F1-Score | 0.79 |

*Note: Replace with actual model performance metrics*

## 🔒 Privacy & Security

- **No Data Storage**: User inputs are not stored or logged
- **Local Processing**: All analysis happens locally
- **Open Source**: Code is transparent and auditable
- **Secure**: No personal information is collected

## 📚 References & Resources

### Academic & Research:
- [Mental Health and Social Media Research](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6214874/)
- [Machine Learning in Mental Health](https://www.nature.com/articles/s41746-019-0191-3)
- [Text Mining for Mental Health Analysis](https://www.jmir.org/2021/6/e26784/)

### Mental Health Organizations:
- [World Health Organization - Mental Health](https://www.who.int/health-topics/mental-health)
- [National Institute of Mental Health](https://www.nimh.nih.gov/)
- [Mental Health America](https://www.mhanational.org/)
- [American Psychological Association](https://www.apa.org/)

### Technical Documentation:
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Natural Language Processing with Python](https://www.nltk.org/book/)
- [TF-IDF Vectorization Guide](https://scikit-learn.org/stable/modules/feature_extraction.html#text-feature-extraction)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2025 Green University Of Bangladesh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 👥 Team

<table>
  <tr>
    <td align="center">
      <img src="https://via.placeholder.com/100x100" width="100px;" alt=""/>
      <br />
      <sub><b>Jalal Uddin Taj</b></sub>
      <br />
      <a href="#" title="Code">💻</a>
      <a href="#" title="Documentation">📖</a>
    </td>
    <td align="center">
      <img src="https://via.placeholder.com/100x100" width="100px;" alt=""/>
      <br />
      <sub><b>Bijoy Chandra Das</b></sub>
      <br />
      <a href="#" title="Code">💻</a>
      <a href="#" title="Research">🔬</a>
    </td>
    <td align="center">
      <img src="https://via.placeholder.com/100x100" width="100px;" alt=""/>
      <br />
      <sub><b>Sakibul Islam Adil</b></sub>
      <br />
      <a href="#" title="Code">💻</a>
      <a href="#" title="Design">🎨</a>
    </td>
  </tr>
</table>

### 🏫 Institution
**Green University Of Bangladesh**
- Department of Computer Science & Engineering
- Mental Health Awareness through AI Technology
- Empowering students with practical AI applications

## 📞 Contact

- **Institution Email**: [info@green.edu.bd](mailto:info@green.edu.bd)
- **University Website**: [Green University Of Bangladesh](https://green.edu.bd/)
- **Project Repository**: [GitHub - Mental Health Classification](https://github.com/y4-5H0/Mental-Health-Classification-on-Social-Media)
- **Department**: Computer Science & Engineering
- **Research Focus**: AI Applications in Mental Health and Social Media Analysis

---

<div align="center">
  <h3>🤝 Empowering mental health awareness through AI technology</h3>
  <p>Made with ❤️ by the Green University Of Bangladesh CSE Team</p>
  
  [![GitHub stars](https://img.shields.io/github/stars/y4-5H0/Mental-Health-Classification-on-Social-Media?style=social)](https://github.com/y4-5H0/Mental-Health-Classification-on-Social-Media/stargazers)
  [![GitHub forks](https://img.shields.io/github/forks/y4-5H0/Mental-Health-Classification-on-Social-Media?style=social)](https://github.com/y4-5H0/Mental-Health-Classification-on-Social-Media/network)
  [![GitHub issues](https://img.shields.io/github/issues/y4-5H0/Mental-Health-Classification-on-Social-Media)](https://github.com/y4-5H0/Mental-Health-Classification-on-Social-Media/issues)
</div>
