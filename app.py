import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load the trained model
model = load_model("models/tomato_disease_model.keras")

# Class labels (make sure these match the training order)
class_names = [
    'Bacterial Spot',
    'Early Blight',
    'Healthy',
    'Late Blight',
    'Septoria Leaf Spot',
    'Yellow Leaf Curl Virus'
]

# Streamlit UI
st.title("🍅 Tomato Leaf Disease Detection")
st.write("Upload an image of a tomato leaf to detect the disease.")
st.info("For best results, upload a close-up of a single tomato leaf against a plain background (256x256 recommended size).")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image_pil = Image.open(uploaded_file).convert("RGB")
    st.image(image_pil, caption="Uploaded Leaf Image", use_column_width=True)

    # Preprocess image 
    img = image.load_img(uploaded_file, target_size=(256, 256))
    img_array = image.img_to_array(img)  
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

    # Predict
    prediction = model.predict(img_array)[0]
    predicted_class = class_names[np.argmax(prediction)]
    confidence = np.max(prediction) * 100

    # Display result
    st.markdown(f"### ✅ Prediction: **{predicted_class}**")
    st.markdown(f"**Confidence:** {confidence:.2f}%")
