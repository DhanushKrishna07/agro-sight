# 🌾Agro-Sight – AI-Driven Agricultural Intelligence System🌿

**Agro-Sight** is an AI-powered web application built using *Flask* that helps farmers detect fruit diseases (like Guava and Dragon Fruit) and get multilingual agricultural assistance through a smart chatbot. It leverages *deep learning (CNN)* for disease prediction and *Gemini API* for a multilingual AI assistant that provides farming advice, pest control suggestions, and government scheme information.

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

- *Backend*: Flask
- *Frontend*: HTML, CSS, JavaScript
- *AI Model*: TensorFlow / Keras (.h5)
- *Chatbot*: Gemini API (Google Generative AI)
- *Languages Supported*: English, Tamil, Hindi, Telugu, Kannada, more...

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

### 🇮🇳 Chatbot – Tamil  
![Chatbot Tamil](assets/screenshots/Chatbot%20Tamil.png)

### 🇮🇳 Chatbot – Hindi  
![Chatbot Hindi](assets/screenshots/Chatbot%20Hindi.png)

### 🇮🇳 Chatbot – Telugu                                                 ### 🇮🇳 Chatbot – Kannada  
![Chatbot Telugu](assets/screenshots/Chatbot%20Telugu.png)              ![Chatbot Kannada](assets/screenshots/Chatbot%20Kannada.png)



### 📈 Model Accuracy & Loss  
![Training and Validation Graph](assets/screenshots/Training%20and%20Validation%20Graph.png)

---

## 🎬 Demo Video

📺 Click below to **watch/download the full project demo**:

➡️ [View Full Demo](assets/demo/Full_Demo_Project.mp4)

---

## 🚀 Getting Started

```bash
git clone https://github.com/DhanushKrishna07/agro-sight.git
cd agro-sight
python "Agri AI App.py"
```
---

## 📦 Model File Access
⚠️ Note: The `.h5` model file is not included in this repository due to GitHub's file size limitations.  
If you would like to test the prediction feature locally, please feel free to request the model file by contacting me at: [dhanushkrishnab@gmail.com](mailto:dhanushkrishnab@gmail.com).
