# Student Result Prediction System (ML vs DL Comparison) 🎓📚

As a Final Year Computer Science & AI student, this project was developed to explore how different Machine Learning and Deep Learning models predict academic success based on student behavior and classroom data.

## 🌟 Project Overview
This project analyzes a massive dataset of **1 million student records** to predict a student's `Total Score`. The goal is to move beyond simple regression and compare traditional ML algorithms with Deep Learning architectures.

## 🚀 Live Demo
[https://student-result-predictor-gkm4gx4fqbsdwu6pnsmxvb.streamlit.app/]

## 📊 Dataset Features
The dataset includes critical academic indicators:
- **Weekly Self-Study Hours:** Time spent studying outside of class.
- **Attendance Percentage:** Regularity in school/university.
- **Class Participation:** Engagement level during lessons.
- **Total Score (Target):** The predicted exam outcome.

## 🛠️ Tech Stack & Architecture
- **Environment:** Google Colab / Python 3.x
- **Data Science:** Pandas, NumPy, Scikit-learn
- **Visualization:** Seaborn, Matplotlib
- **Deep Learning:** TensorFlow & Keras
- **Model Deployment:** Streamlit Web Dashboard

## 📈 Performance Comparison
After training on 800,000 records, the models achieved the following R2 Scores (Accuracy):

| Model | Algorithm Type | R2 Score |
| :--- | :--- | :--- |
| **Linear Regression** | Simple ML | 0.66 |
| **Random Forest** | Advanced Ensemble ML | 0.67 |
| **Neural Network** | **Deep Learning (ANN)** | **0.71** |

> **Finding:** The Deep Learning model outperformed traditional ML methods, effectively capturing non-linear patterns in student data.

## 📂 Repository Structure
```text
├── models/
│   ├── linear_model.pkl          # Saved Linear Regression
│   ├── random_forest_model.pkl   # Saved Random Forest
│   └── neural_network_model.keras # Saved Deep Learning Model
├── notebooks/
│   └── student_analysis.ipynb    # Main development notebook
├── data/
│   └── student_performance.csv   # Dataset (1M Records)
└── README.md
