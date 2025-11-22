from flask import Flask, render_template, request, jsonify
import numpy as np
import tensorflow as tf
from PIL import Image
import os
from chatbot import get_chat_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Railway model path
railway_model_path = "/app/models/enhanced_fruit_disease_model.h5"

# Local model path
local_model_path = "enhanced_fruit_disease_model.h5"

# Auto select correct model path
if os.path.exists(railway_model_path):
    print("🚀 Running on Railway — Loading model from Railway storage...")
    model = tf.keras.models.load_model(railway_model_path)
elif os.path.exists(local_model_path):
    print("🖥 Running locally — Loading model from local file...")
    model = tf.keras.models.load_model(local_model_path)
else:
    raise FileNotFoundError("❌ Model file not found in either local or Railway location.")

# Define the class labels (update these with your actual model classes)
class_names = ['Anthracnose', 'Defect Dragon Fruit', 'Fresh Dragon Fruit', 'fruit_fly', 'healthy_guava']

@app.route("/")
def home():
    return render_template("Frontend.html")

@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files["file"]
    if not file:
        return jsonify({"error": "Empty file"}), 400

    try:
        img = Image.open(file).convert("RGB")
        img = img.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction)]

        return jsonify({"prediction": predicted_class})
    except Exception as e:
        return jsonify({"error": f"Error processing image: {str(e)}"}), 500

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "Invalid input"}), 400
    try:
        user_message = data["message"]
        response = get_chat_response(user_message)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

