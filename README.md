# 🌾Agro-Sight – AI-Driven Agricultural Intelligence System🌿

**Agro-Sight** is an AI-powered web application built using *Flask* that helps farmers detect fruit diseases (like Guava and Dragon Fruit) and get multilingual agricultural assistance through a smart chatbot. It leverages *deep learning (CNN)* for disease prediction and *Gemini API* for a multilingual AI assistant that provides farming advice, pest control suggestions, and government scheme information.

<p align="center">

  <img src="https://img.shields.io/badge/Python-Backend-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-Framework-000000?style=for-the-badge&logo=flask&logoColor=white"/>

  <img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google%20Gemini-Chatbot-4285F4?style=for-the-badge&logo=google&logoColor=white"/>
  
  <img src="https://img.shields.io/badge/HTML5-Clean%20Layout-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-Vanilla%20JS-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>

  <img src="https://img.shields.io/badge/HuggingFace-Deployed-FFD21E?style=for-the-badge&logo=huggingface&logoColor=yellow"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>

</p>

---

## 🌐 Live Demo

You can experience the interactive website live here: [**🌾Agro-Sight**](https://huggingface.co/spaces/DhanushKrishna07/Agro-Sight)

---

## 📚 Table of Contents

- [🌾 Overview](#agro-sight--ai-driven-agricultural-intelligence-system)
- [🌐 Live Demo](#-live-application)
- [🚀 Features](#-features)
- [🛠 Tech Stack](#-tech-stack)
- [📸 Screenshots](#-screenshots)
- [🎥 Demo Video](#-demo-video)
- [⚙️ How It Works](#️-how-it-works)
- [🔮 Future Enhancements](#-future-enhancements)
- [🚀 Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [📦 Model Access](#-model-file-access)
- [📄 License](#-license)
- [📬 Contact](#-contact)

---

## 🚀 Features

### 🍏 AI-Based Fruit Disease Prediction
- Upload fruit images and receive instant predictions.
- Detects diseases like **Anthracnose**, **Fruit Fly**, **Defect Dragon Fruit**, and more.
- Trained on 4299 images using a custom CNN model.

### 💬 Multilingual Smart Chatbot (Powered by Gemini API)
- Ask questions in *English, Tamil, Hindi, Telugu or Kannada and more*.
- Get recommendations on:
  - Crop yield improvement.
  - Pest control and fertilizer suggestions.
  - Government schemes for Indian farmers.

### 📊 Training Metrics
- Model accuracy and loss visualized through graphs.
- Evaluated using training/validation split for high performance.

### 🎨 Intuitive Frontend
- Built using HTML, CSS, and JS.
- User-friendly interface with voice input (Speech-to-Text), voice output (Text-to-Speech), and real-time responses.

---

## 🛠 Tech Stack

### 1. Backend:

  - **Python (Flask):** Acts as the main server framework, handling image uploads, routing, and API endpoints for prediction and chatbot functionality.
  
  - **TensorFlow / Keras:** Used to load and run the trained fruit disease prediction deep learning model.
  
  - **NumPy:** Supports image tensor manipulation and preprocessing before prediction.

  - **Pillow (PIL):** Handles uploaded image reading and resizing.
  
  - **Flask-CORS:** Ensures secure communication between frontend and backend while allowing cross-origin API calls.
  
  - **Google Gemini API:** Used to generate intelligent farming responses through the chatbot.
  
### 2. Frontend:

  - **HTML5:** Provides the structure for the web interface including file upload, chatbot UI, and prediction display.
    
  - **CSS (Custom Styling):** Adds UI polish, animations, glowing effects, chat sidebar UI, and background transitions.
    
  - **JavaScript:** Handles dynamic UI updates, file preview, prediction requests, chatbot messaging, speech recognition, and text-to-speech.
  
---

## 📸 Demo Screenshots

### 🍂 Diseased Fruits
These images represent fruits affected by various diseases, as detected by the AgroSight model.

**Anthracnose on Guava**
![Anthracnose on Guava](assets/screenshots/Guava%20-%20Anthracnose%20Disease.png)

**Fruit Fly Infection in Guava**
![Fruit Fly Infection in Guava](assets/screenshots/Guava%20-%20Fruit%20Fly%20Disease.png)

**Defect in Dragon Fruit**
![Defect in Dragon Fruit](assets/screenshots/Defect%20Dragon%20Fruit.png)

### 🌱 Healthy Fruits
These are predictions of fruits with no disease symptoms.

**Healthy Guava**
![Healthy Guava](assets/screenshots/Guava%20-%20Healthy.png)

**Fresh Dragon Fruit**
![Fresh Dragon Fruit](assets/screenshots/Fresh%20Dragon%20Fruit.png)

### 🗣 Chatbot – English  
![Chatbot English](assets/screenshots/Chatbot%20English.png)

### 🗣 Chatbot – Tamil  
![Chatbot Tamil](assets/screenshots/Chatbot%20Tamil.png)

### 🗣 Chatbot – Hindi  
![Chatbot Hindi](assets/screenshots/Chatbot%20Hindi.png)

### 🗣 Chatbot – Telugu
![Chatbot Telugu](assets/screenshots/Chatbot%20Telugu.png) 

### 🗣 Chatbot – Kannada
![Chatbot Kannada](assets/screenshots/Chatbot%20Kannada.png)

### 📈 Model Accuracy & Loss  
![Training and Validation Graph](assets/screenshots/Training%20and%20Validation%20Graph.png)

---

## 🎥 Demo Video

📺 Click below to **watch/download the full project demo**:

➡️ [View Full Demo](assets/demo/Full_Demo_Project.mp4)

---

## ⚙️ How It Works

### The application follows a hybrid AI workflow combining machine learning and language-based reasoning:

  **1. Image Upload:** The user uploads a fruit image through the interface on Frontend.html.

  **2. Image Preview:** The frontend instantly displays a preview using JavaScript before sending it to the backend.

  **3. Backend Prediction:** Flask receives the uploaded file at the /predict endpoint, preprocesses the image (resizing, normalizing), and sends it to the TensorFlow model for prediction.

  **4. Result Display:** The predicted class (e.g., Fruit Fly, Anthracnose, Fresh Dragon Fruit) is returned as JSON and shown in the UI.

  **5. AI Chatbot Interaction:** Users can send farming-related queries to the chatbot. The /chat endpoint forwards the message to the Gemini model, which returns a tailored farming response.

  **6. Speech Input & Output:** The chatbot supports voice-based conversation using browser speech recognition and speech synthesis.
  
---

## 🔮 Future Enhancements

- Multi-crop and leaf disease support

- Offline prediction using TensorFlow Lite

- Farmer profile system with personalized recommendations

- Integration with government DBs for localized subsidies & alerts

- Multi-language dashboard with OCR image-to-text

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites
   - Python 3.9+

   - pip package manager
   
   - Gemini API Key

### Installation

**1. Clone the repository:**

```bash
git clone https://github.com/DhanushKrishna07/agro-sight.git
cd agro-sight
pip install -r requirements.txt
```

**2. Set up environment variables:**

Create a .env file in the root directory of your project and add your API key:

```bash
GEMINI_API_KEY=your_gemini_api_key_here
```

### Running the Application

```bash
python agri_ai_app.py
```

Once running, open the web app in your browser at:

```bash
http://localhost:5000
```

Upload a fruit image, click Predict, or interact with the AI chatbot for farming guidance.

---

## 📦 Model File Access
⚠️ Note: The `.h5` model file is not included in this repository due to GitHub's file size limitations.  
If you would like to test the prediction feature locally, please feel free to request the model file by contacting me at: [dhanushkrishnab@gmail.com](mailto:dhanushkrishnab@gmail.com).

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with proper attribution.

---

## 📧 Contact

📨 **Email:** dhanushkrishnab@gmail.com  
🔗 **LinkedIn:** https://www.linkedin.com/in/dhanushkrishna15  

