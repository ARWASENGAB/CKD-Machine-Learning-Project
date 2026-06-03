
# Chronic Kidney Disease Prediction Using Machine Learning

## Project Overview


This project aims to predict Chronic Kidney Disease (CKD) using machine learning based on patient clinical and laboratory data. The dataset required cleaning because it contained many missing values. After preprocessing, feature engineering, and feature selection, three models were trained: Logistic Regression, Random Forest, and SVM. The SVM model achieved the best performance and was deployed using Streamlit to allow real-time CKD prediction.
Projects links
GitHub Repository
https://github.com/ARWASENGAB/CKD-Machine-Learning-Project/tree/main
Streamlit Prediction App
https://ckd-machine-learning-project-a52urdradniinqdpapplxyi.streamlit.app/
Dataset Source: Kaggle Chronic Kidney Disease
https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease
Key Features

✅ Chronic Kidney Disease prediction using clinical data

✅ Data cleaning and missing value handling

✅ Exploratory Data Analysis (EDA)

✅ Feature engineering

✅ Feature selection using SelectKBest

✅ Multiple machine learning models

✅ Hyperparameter tuning using GridSearchCV

✅ Model evaluation and validation

✅ Streamlit web application deployment

Dataset Information

The dataset was obtained from the UCI Machine Learning Repository and contains clinical and laboratory measurements of patients.

The dataset includes features such as:

Age
Blood Pressure
Albumin
Sugar
Blood Glucose Random
Blood Urea
Serum Creatinine
Hemoglobin
Packed Cell Volume
Hypertension

Target Variable:

CKD
Not CKD

The dataset originally contained missing values that were handled during preprocessing.

Machine Learning Pipeline
Data Preprocessing
Handled missing values using median and mode imputation
Converted categorical variables into numerical format
Checked data consistency and data types
Removed all remaining missing values
Exploratory Data Analysis (EDA)

Visualizations included:

CKD class distribution
Age distribution
Blood pressure distribution
Hemoglobin boxplot
Serum creatinine boxplot
Correlation heatmap
Feature Engineering

A new feature called Anemia_Status was created based on hemoglobin levels to improve model performance and capture clinically relevant information.

Feature Selection

SelectKBest with Chi-Square (χ²) feature selection was used to identify the most informative features.

Top selected features:

age
al
su
bgr
bu
sc
hemo
pcv
rc
htn
Machine Learning Models

The following models were trained and evaluated:

Logistic Regression
Random Forest Classifier
Support Vector Machine (SVM)
Hyperparameter Tuning

GridSearchCV was applied to optimize the Random Forest model.

Best Parameters:

{
 'n_estimators': 50,
 'max_depth': None,
 'min_samples_split': 2
}

Best Cross-Validation Score:

99.06%
Model Evaluation

Models were evaluated using:

Accuracy
Precision
Recall
F1-score
Confusion Matrix
ROC Curve
AUC Score
Results
Model	Accuracy
Logistic Regression	97%
Random Forest	97%
Support Vector Machine (SVM)	99%

The Support Vector Machine achieved the best overall performance and was selected as the final model.

Streamlit Web Application

The final model was deployed using Streamlit.

Users can:

Enter patient clinical measurements
Obtain real-time CKD predictions
Interact with a simple and user-friendly interface
Project Structure
CKD-Machine-Learning-Project/
│
├── app.py
├── ckd_machine_learning_project.py
├── ckd_model.pkl
├── scaler.pkl
├── features.pkl
├── requirements.txt
├── README.md
└── chronic diseases.zip
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Streamlit
Joblib
Dataset Source

UCI Machine Learning Repository

https://archive.ics.uci.edu/dataset/336/chronic+kidney+disease

How to Run Locally
pip install -r requirements.txt
streamlit run app.py
Streamlit Application

Add your deployed Streamlit link here.

https://your-streamlit-app-link.streamlit.app
Future Improvements
Train the model on larger datasets
Explore deep learning approaches
Add explainable AI methods such as SHAP
Integrate prediction confidence scores
Improve clinical decision support features
