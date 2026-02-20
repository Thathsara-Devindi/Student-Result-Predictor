import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# App  title 
st.title("🎓 Student Success Predictor")
st.write("Enter the details below to predict the student's total score.")

# Model eka load karamu (Oya download karapu .keras file eke nama meeta samana wenna ona)
@st.cache_resource
def load_my_model():
    return tf.keras.models.load_model('neural_network_model.keras', compile=False)

model = load_my_model()

# User input ganna than (Sliders)
hours = st.slider("Weekly Self-Study Hours", 0, 50, 20)
attendance = st.slider("Attendance Percentage", 0, 100, 85)
participation = st.slider("Class Participation (1-10)", 1, 10, 5)

# Predict button
if st.button("Predict Score"):
    # Data tika AI ekata galapena format ekata hadamu
    input_data = np.array([[hours, attendance, participation]])
    
    # Prediction eka gannawa
    prediction = model.predict(input_data)
    final_score = prediction[0][0]
    
    # Result eka pennanawa
    st.success(f"The predicted Total Score is: {final_score:.2f}%")
    
    # Score eka anuwa podi message ekak
    if final_score > 75:
        st.balloons()
        st.write("Excellent! This student is likely to pass with flying colors.")
    elif final_score > 40:
        st.write("This student is on the right track but can improve.")
    else:
        st.warning("This student might need extra support to pass.")