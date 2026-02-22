import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# App  title 
st.title("🎓 Student Success Predictor")
st.write("Enter the details below to predict the student's total score.")

# Model load  
@st.cache_resource
def load_my_model():
    return tf.keras.models.load_model('neural_network_model.keras', compile=False)

model = load_my_model()

# User input(Sliders)
hours = st.slider("Weekly Self-Study Hours", 0, 50, 20)
attendance = st.slider("Attendance Percentage", 0, 100, 85)
participation = st.slider("Class Participation (1-10)", 1, 10, 5)

# Predict button
if st.button("Predict Score"):
    # Data format 
    input_data = np.array([[hours, attendance, participation]])
    
    # Prediction 
    prediction = model.predict(input_data)
    final_score = prediction[0][0]
    
    # Result 
    st.success(f"The predicted Total Score is: {final_score:.2f}%")
    
    # Score  message 
    if final_score > 75:
        st.balloons()
        st.write("Excellent! This student is likely to pass with flying colors.")
    elif final_score > 40:
        st.write("This student is on the right track but can improve.")
    else:
        st.warning("This student might need extra support to pass.")
