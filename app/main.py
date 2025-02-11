import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os

working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/trained model/potato_disease_prediction.h5"

model = tf.keras.models.load_model(model_path)

class_names = ['Early blight', 'Healthy', 'Late blight']

def preprocess_image(image) :
    img = Image.open(image).convert('L')  # Convert to grayscale
    img = img.resize((256, 256))  # Resize to 256x256 (as expected by the model)
    img_array = np.array(img)  # Convert to NumPy array
    img_array = img_array.reshape((1, 256, 256, 1))  # Reshape for CNN input
    img_array = img_array / 255.0  # Normalize pixel values (0-1)
    return img_array

st.title("Potato Disease Prediction")

uploaded_image = st.file_uploader("Upload an image", type =['jpg','jpeg','png'])

if uploaded_image is not None :
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)

    with col1 :
        resized_img = image.resize((100,100))
        st.image(resized_img)

    with col2 :
        if st.button('Classify') :
            img_array = preprocess_image(uploaded_image)
            result = model.predict(img_array)

            predicted_class = np.argmax(result)
            prediction = class_names[predicted_class]

            st.success(f"Prediction : {prediction}")

