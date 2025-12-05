# Customer-Churn-Prediction
Customer Churn Prediction System using Python and Machine Learning (Random Forest). This project predicts whether a customer is likely to churn based on age, contract type, payment method, monthly charges, and internet service. Includes real-time user input prediction and data visualization.

# 📊 Customer Churn Prediction System

A Customer Churn Prediction System built using Python and Machine Learning (Random Forest). This project predicts whether a customer is likely to churn based on age, contract type, payment method, monthly charges, and internet service provider.

---

## 🚀 Features
- Real-time user input through terminal
- Automatic encoding of categorical data
- Machine Learning model using Random Forest
- Model accuracy evaluation
- Churn prediction (Yes / No)
- Data visualization using Matplotlib
- Clean and simple project structure

---

## 🧠 Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Random Forest Algorithm

---

## 📁 Project Structure
Customer-Churn-Prediction  
├── data.csv  
├── churn_prediction.py  
├── README.md  
├── .gitignore  
└── LICENSE  

---

## ⚙️ How the Project Works
1. Loads customer data from `data.csv`
2. Encodes all categorical columns using LabelEncoder
3. Splits the dataset into training (90%) and testing (10%)
4. Trains the model using Random Forest Classifier
5. Takes live input from the user
6. Converts user input using saved encoders
7. Predicts whether the customer will churn or not
8. Displays a scatter plot of Monthly Charges vs Churn Type

---

## ▶️ How to Run the Project

### Step 1: Install Required Libraries
pip install pandas scikit-learn matplotlib


### Step 2: Run the Program
python churn_prediction.py


### Step 3: Enter Customer Details
You will be asked to enter:
- Customer Age  
- Contract Type (Monthly / Yearly)  
- Payment Method  
- Monthly Charges  
- Internet Service Provider  

After entering the details, the model will display whether the customer is likely to churn or not.

---

## 📈 Sample Output
Model Accuracy: 0.8
Prediction for this customer: Not Churn


A scatter plot between Monthly Charges and Churn Type is also displayed.

---

## 🗃️ Dataset Information
The dataset (`data.csv`) should contain the following columns:
- Customer's Age
- Contract Type
- Payment_Method
- Monthly Charges
- Internet Service Type
- Churn Type (Target Column)

---

## 🎯 Project Objective
The main objective of this project is to help businesses:
- Predict customer churn in advance
- Improve customer retention
- Reduce revenue loss
- Take data-driven business decisions

---

## 🛠️ Future Enhancements
- Add a graphical user interface (GUI)
- Deploy as a web application using Streamlit or Flask
- Save and load trained models using Joblib
- Add more customer parameters
- Compare multiple ML models
- Add dashboard for analytics

---

## 👨‍💻 Developer
**NIHAR**  
Computer Science Engineering Student  
Interested in Machine Learning, Data Science & Software Development  

---

## 📜 License
This project is licensed under the MIT License.

---

⭐ If you like this project, don’t forget to give it a star on GitHub!
