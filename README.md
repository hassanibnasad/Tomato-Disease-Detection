# 🍅 Tomato Leaf Disease Classification

A deep learning project using Convolutional Neural Networks and Transfer Learning to classify tomato leaf diseases from images. A web app for classifying tomato leaf diseases using images. Built with TensorFlow and Streamlit, this tool can help farmers and researchers quickly identify six common tomato plant diseases.

---

## 📁 Dataset 

Trained on: [PlantVillage Dataset](https://www.kaggle.com/datasets/emmarex/plantdisease)

- Structured into `Train`, `Val`, and `Test` directories
- Categories include:
  - Septoria Leaf Spot 
  - Bacterial Spot
  - Early Blight
  - Late Blight
  - Yellow Leaf Curl Virus
  - Healthy

---

## 🧠 Model Details

- Framework: **TensorFlow/Keras**
- Image size: **256x256**
- Techniques:
  - Data Augmentation
  - Transfer Learning with **MobileNetV2** 
  - Dropout Regularization
- Output: Softmax over 6 disease classes
- Model saved as: `models/tomato_disease_model.keras`
- 🌐 Interactive web interface via Streamlit
- 📊 Displays prediction confidence

---

## 🌍 Live Demo

> ✅ Deployed on Streamlit Cloud  
> [Link:](https://tomato-disease-detection-2gdpyuxyzzeil4buqxmvfd.streamlit.app/)
  
---

## 🧪 Accuracy

- Training Accuracy: 0.9322
- Validation Accuracy: 0.8641 

---

## 🖼️ Image Upload Guidelines

To get accurate results, follow these tips when uploading images:

### ✅ Recommended:
- Clear, in-focus photo of **a single tomato leaf**
- Leaf should be centered and clearly visible
- Image taken against a **plain background** (paper, board, etc.)
- Similar to the training dataset (256x256 or square image)

### ❌ Avoid:
- Blurry or dark images
- Photos with multiple leaves or full plant
- Background clutter (soil, hand, other plants)
- Shadows, poor lighting, or partial leaves

> ℹ️ The model was trained on standardized leaf images. Real-world images with noise or complex backgrounds may reduce accuracy.

---

## 🧑‍💻 Author

**Mohd Hassan**  
📚 Aspiring Data Scientist  
📧 [for queries: mohassan390@gmail.com]

---

## ⭐ Show Some Love

If you found this project helpful, consider giving it a ⭐ on GitHub!

