# 🧠 Mental Health Condition Prediction System

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Latest-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An AI-powered web application that analyzes text patterns to predict potential mental health conditions using machine learning. This tool is designed for educational purposes and mental health awareness.

![Mental Health Prediction Demo](https://via.placeholder.com/800x400/2E86AB/FFFFFF?text=Mental+Health+Prediction+System)

## 🌟 Features

- **🤖 Advanced Text Analysis**: Uses natural language processing to analyze input text
- **📊 Pattern Recognition**: Identifies patterns in text that may indicate mental health conditions
- **🎯 Instant Predictions**: Provides real-time analysis and predictions
- **🎨 Modern UI**: Beautiful, responsive web interface built with Streamlit
- **📱 Mobile Friendly**: Works seamlessly across desktop and mobile devices
- **🆘 Mental Health Resources**: Includes crisis helplines and professional help information
- **⚠️ Educational Focus**: Clear disclaimers about professional medical advice

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
git clone https://github.com/your-username/mental_health_project.git
cd mental_health_project
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
pip install streamlit pandas scikit-learn pickle-mixin
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## 🎯 Usage

1. **Launch the Application**: Run `streamlit run app.py` in your terminal
2. **Enter Text**: In the text area, describe your thoughts, feelings, or mental health concerns
3. **Analyze**: Click the "🔍 Analyze Mental Health Pattern" button
4. **View Results**: The AI will analyze your text and provide a prediction
5. **Get Resources**: Use the sidebar for mental health resources and crisis helplines

### Example Input:
```
I've been feeling really down lately. I can't seem to find motivation to do anything, 
and I'm having trouble sleeping. Everything feels overwhelming and I just want to 
stay in bed all day.
```

## 📁 Project Structure

```
mental_health_project/
│
├── app.py                 # Main Streamlit application
├── trained_model.pkl      # Pre-trained machine learning model
├── vectorizer.pkl         # TF-IDF vectorizer for text processing
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── LICENSE              # MIT License
```

### File Descriptions:

- **`app.py`**: Main application file containing the Streamlit web interface
- **`trained_model.pkl`**: Serialized machine learning model (Logistic Regression)
- **`vectorizer.pkl`**: TF-IDF vectorizer used for text preprocessing
- **`README.md`**: Comprehensive project documentation
- **`requirements.txt`**: List of Python dependencies

## 🤖 Model Information

### Machine Learning Pipeline:

1. **Text Preprocessing**: Input text is cleaned and preprocessed
2. **Feature Extraction**: TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
3. **Classification**: Logistic Regression model predicts mental health conditions
4. **Output**: Returns predicted mental health condition category

### Model Performance:
- **Algorithm**: Logistic Regression
- **Feature Extraction**: TF-IDF Vectorization
- **Text Processing**: Natural Language Processing techniques
- **Training Data**: [Specify your dataset source]

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
streamlit>=1.0.0
pandas>=1.3.0
scikit-learn>=1.0.0
pickle-mixin>=1.0.0
```

### Key Components:
- **Frontend**: Streamlit with custom CSS styling
- **Backend**: Python with scikit-learn
- **Model**: Logistic Regression classifier
- **Text Processing**: TF-IDF vectorization
- **Deployment**: Can be deployed on Streamlit Cloud, Heroku, or AWS

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

**This application is for educational and research purposes only.**

- 🚨 **Not a Medical Tool**: This tool should NOT be used as a substitute for professional medical advice, diagnosis, or treatment
- 👨‍⚕️ **Consult Professionals**: Always seek the advice of qualified healthcare providers
- 🔬 **Research Purpose**: This project is designed for learning and awareness about AI in healthcare
- 📊 **Data Privacy**: No user data is stored or transmitted

### Crisis Resources:
- **Emergency**: Call 911 (US) or your local emergency number
- **National Suicide Prevention Lifeline**: 988
- **Crisis Text Line**: Text HOME to 741741
- **International**: [Find help worldwide](https://www.iasp.info/resources/Crisis_Centres/)

## 📈 Future Enhancements

- [ ] Multi-language support
- [ ] Integration with more advanced NLP models (BERT, GPT)
- [ ] Real-time chat interface
- [ ] Data visualization dashboards
- [ ] Mobile app development
- [ ] Integration with wearable devices
- [ ] Personalized recommendations

## 📊 Model Metrics

| Metric | Value |
|--------|-------|
| Accuracy | XX.X% |
| Precision | XX.X% |
| Recall | XX.X% |
| F1-Score | XX.X% |

*Note: Replace with actual model performance metrics*

## 🔒 Privacy & Security

- **No Data Storage**: User inputs are not stored or logged
- **Local Processing**: All analysis happens locally
- **Open Source**: Code is transparent and auditable
- **Secure**: No personal information is collected

## 📚 References & Resources

- [Mental Health Resources](https://www.mentalhealth.gov/)
- [World Health Organization - Mental Health](https://www.who.int/health-topics/mental-health)
- [National Institute of Mental Health](https://www.nimh.nih.gov/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Streamlit Documentation](https://docs.streamlit.io/)

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

- **Email**: [your-email@example.com](mailto:your-email@example.com)
- **University**: [Green University Of Bangladesh](https://green.edu.bd/)
- **Project Repository**: [GitHub](https://github.com/your-username/mental_health_project)

---

<div align="center">
  <h3>🤝 Empowering mental health awareness through AI technology</h3>
  <p>Made with ❤️ by the Green University Of Bangladesh Team</p>
  
  [![GitHub stars](https://img.shields.io/github/stars/your-username/mental_health_project?style=social)](https://github.com/your-username/mental_health_project/stargazers)
  [![GitHub forks](https://img.shields.io/github/forks/your-username/mental_health_project?style=social)](https://github.com/your-username/mental_health_project/network)
  [![GitHub issues](https://img.shields.io/github/issues/your-username/mental_health_project)](https://github.com/your-username/mental_health_project/issues)
</div>
