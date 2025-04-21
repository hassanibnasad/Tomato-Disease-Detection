import argparse
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
import os

# Define class labels 
CLASS_NAMES = [
    'Bacterial Spot',
    'Early Blight',
    'Healthy',
    'Late Blight',
    'Septoria Leaf Spot',
    'Yellow Leaf Curl Virus'
]

# Load the trained model
model = load_model("models/tomato_disease_model2.keras")

def predict_image(image_path):
    # Load and preprocess image
    image = cv2.imread(image_path)
    image = cv2.resize(image, (256, 256))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = preprocess_input(image)
    image = np.expand_dims(image, axis=0)

    # Predict
    preds = model.predict(image)[0]
    class_idx = np.argmax(preds)
    class_label = CLASS_NAMES[class_idx]
    confidence = preds[class_idx]

    return class_label, confidence

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True, help="Path to input image")
    args = parser.parse_args()

    if not os.path.exists(args.image):
        print("❌ Error: Image path does not exist.")
    else:
        label, conf = predict_image(args.image)
        print(f"✅ Prediction: {label} ({conf * 100:.2f}% confidence)")
