# 🥔 Potato-Disease-Detection

This project leverages a **Convolutional Neural Network (CNN) model** trained on a dataset containing images of potato leaves affected by **Early Blight, Late Blight, and Healthy leaves**. The model achieves high accuracy in detecting and classifying these diseases. The trained model is integrated into a **Streamlit web application**, providing an interactive interface for real-time disease prediction.

To ensure scalability and ease of deployment, the application is containerized using **Docker**, enabling it to run efficiently across different environments.

---

## 🚀 Features

✅ **Deep Learning Model** – A CNN trained on a potato disease dataset for accurate classification.  
✅ **Interactive Web App** – A user-friendly, responsive interface built with Streamlit for seamless interaction.  
✅ **Dockerized Deployment** – The application is containerized for easy deployment across different environments.  

---

## 🛠️ How It Works

1️⃣ **Upload an Image** – Users can upload an image of a potato leaf.  
2️⃣ **Preprocessing** – The image is resized, converted to grayscale, and normalized.  
3️⃣ **Prediction** – The trained CNN model classifies the image into one of three categories: **Early Blight, Late Blight, or Healthy**.  
4️⃣ **Output** – The predicted class is displayed along with the confidence score.  

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```sh
git clone https://github.com/iamsommyajain/Potato-Disease-Detection.git
cd Potato-Disease-Detection
```
### 2️⃣ Installing Dependencies 
```sh
pip install -r requirements.txt
```
### 3️⃣ Run the Streamlit App
```sh
streamlit run app/main.py
```
### 4️⃣ Run with Docker
```sh
docker build -t potato_disease_app:v1.0 .
docker run -p 80:80 potato_disease_app:v1.0
```
---

## 🤝 Contributing  
Contributions are welcome! If you find a bug or want to improve the model, feel free to open an issue or submit a pull request.  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

## 🔗 Connect  
📧 **Email:** [sommyajain2005@gmail.com](mailto:sommyajain2005@gmail.com)  
🌍 **GitHub:** [@iamsommyajain](https://github.com/iamsommyajain)  
