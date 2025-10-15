 Diabetes Prediction using Machine Learning

 # 🩺 Diabetes Prediction using Machine Learning

This project predicts whether a person is likely to have diabetes based on medical attributes such as glucose level, BMI, age, etc.  
It uses machine learning models trained on real healthcare data to provide accurate predictions.

## 📚 Table of Contents
- [About the Project](#-about-the-project)
- [Tech Stack](#-tech-stack)
- [Features](#-features)
- [Dataset](#-dataset)
- [Installation](#-installation)
- [Usage](#-usage)
- [Model Accuracy](#-model-accuracy)
- [Project Screenshots](#-project-screenshots)
- [Future Improvements](#-future-improvements)
- [License](#-license)

## 💡 About the Project
The Diabetes Prediction system helps users identify potential diabetes risk by analyzing health parameters.  
It is built using Python and popular data science libraries to create an accurate and efficient model for healthcare applications.

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=plotly&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

## ✨ Features
- User-friendly interface for data input  
- Predicts diabetes risk accurately  
- Visualizes data correlations and model performance  
- Machine learning model saved as .pkl for reuse

## 📊 Dataset
The dataset is taken from the PIMA Indians Diabetes Database available on Kaggle.  
It includes parameters like:
- Pregnancies
- Glucose
- Blood Pressure
- BMI
- Age
- Outcome (1 = Diabetic, 0 = Non-Diabetic)

---

### 8️⃣ Usage
Show how to use your project:
`markdown
## 🧠 Usage
- Run the Flask app and open it in a browser  
- Enter the required health parameters  
- Click "Predict" to see the result  
- Model predicts `Diabetic` or `Non-Diabetic`

## 📈 Model Accuracy
- Logistic Regression: 84%
- Random Forest: 88%
- SVM: 86%
Final Model: Random Forest Classifier (88% Accuracy)

## 🖼️ Project Screenshots
![App Interface](screenshots/app_home.png)
![Prediction Result](screenshots/result.png)

## 🚀 Future Improvements
- Add user authentication  
- Deploy on cloud (Heroku / AWS)  
- Add real-time health data input  
- Improve UI using HTML/CSS
