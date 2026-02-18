# Student Result Prediction System (ML vs DL Comparison) 🎓📚

As a Final Year Computer Science & AI student, this project was developed to explore how different Machine Learning and Deep Learning models predict academic success based on student behavior and classroom data.

## 🌟 Project Overview
This project analyzes a massive dataset of **1 million student records** to predict a student's `Total Score`. The goal is to move beyond simple regression and compare traditional ML algorithms with Deep Learning architectures.

## 📊 Dataset Features
The dataset includes critical academic indicators:
- **Weekly Self-Study Hours:** Time spent studying outside of class.
- **Attendance Percentage:** Regularity in school/university.
- **Class Participation:** Engagement level during lessons.
- **Total Score (Target):** The predicted exam outcome.

## 🛠️ Tech Stack
- **Languages:** Python (Google Colab)
- **Data Libraries:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn (Linear Regression, Random Forest)
- **Deep Learning:** TensorFlow/Keras (Neural Networks)

## 📈 Methodology & Models
We implemented a multi-model approach to find the most accurate predictor:
1. **Linear Regression:** Baseline model for linear relationships.
2. **Random Forest Regressor:** For handling non-linear patterns and better accuracy.
3. **Neural Networks (Deep Learning):** A multi-layer perceptron (MLP) to explore complex data patterns.

## 🚀 Key Results (Current Progress)
- **Data Cleaning:** 100% processed with zero missing values.
- **Initial Baseline (Linear Regression):** Achieved an **R2 Score of 0.66**.
- **Model Comparison:** Currently training advanced models to push accuracy above 85%.

## 📂 Repository Structure
```text
├── data/                  # Student performance dataset
├── notebooks/             # Google Colab notebooks
├── results/               # Comparative graphs and metrics
└── README.md              # Project documentation
