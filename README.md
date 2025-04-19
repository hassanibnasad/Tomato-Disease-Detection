# 🍅 Tomato Leaf Disease Classification

A deep learning project using Convolutional Neural Networks and Transfer Learning to classify tomato leaf diseases from images. Built using TensorFlow/Keras.

---

## 📁 Dataset 

Trained on kaggle's [Plant Village Dataset (Updated)] 

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
- Model saved as: `models/tomato_disease_model.keras`

---

## 🧪 Accuracy

- Training Accuracy: 0.9322
- Validation Accuracy: 0.8641 


---

## 📈 Sample Prediction

```bash
python predict.py --image "..\tomato_disease\Tomato\Test\Early Blight\803ac166-670f-4cad-9f37-e36eea3118d9___RS_Erly.B 9457.JPG""
✅ Prediction: Yellow Leaf Curl Virus (100.00% confidence)

