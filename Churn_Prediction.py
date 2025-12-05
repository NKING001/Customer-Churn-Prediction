import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as p
def user_input(nihar):
    print("\nWelcome to the Customer Churn Prediction by NIHAR\n")
    customers_age = int(input("Enter the customer's age: "))
    print("Select Contract Type:")
    print("A. Monthly")
    print("B. Yearly")
    ctype = input("Enter A or B: ").upper()
    contract_type = "Monthly" if ctype == "A" else "Yearly"
    print("Select Payment Method:")
    print("A. Online Payment")
    print("B. Bank Transfer")
    print("C. Credit Card")
    ptype = input("Enter A, B or C: ").upper()
    payment_method = {"A": "Online Payment", "B": "Bank Transfer", "C": "Credit Card"}[ptype]
    monthly_charges = int(input("Enter Monthly Charges: "))
    print("Select Internet Service Type:")
    print("A. Jio")
    print("B. Airtel")
    print("C. VI")
    print("D. BSNL")
    itype = input("Enter A, B, C or D: ").upper()
    internet_service = {"A": "Jio", "B": "Airtel", "C": "VI", "D": "BSNL"}[itype]
    df = pd.DataFrame({"Customer's Age":[customers_age],"Contract Type":[contract_type],"Payment_Method":[payment_method],"Monthly Charges":[monthly_charges],"Internet Service Type":[internet_service]})
    for np in nihar:
        if np!="Churn Type":
            df[np]=nihar[np].transform(df[np])
    return df
data = pd.read_csv("data.csv")
nihar={}
for amg in data.select_dtypes(include='object').columns:
    sf=LabelEncoder()
    data[amg]=sf.fit_transform(data[amg])
    nihar[amg]=sf
X=data.drop("Churn Type",axis=1)
y=data["Churn Type"]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=10)
model=RandomForestClassifier(random_state=10)
model.fit(X_train,y_train)
print("Model Accuracy:",model.score(X_test,y_test))
print("\nNow let's predict for new user input...")
user_df=user_input(nihar)
predict=model.predict(user_df)[0]
print(f"\nPrediction for this customer: {'Churn' if predict==1 else 'Not Churn'}")
p.scatter(X["Monthly Charges"],y,alpha=0.9)
p.xlabel("Monthly Charges")
p.ylabel("Churn Type")
p.title("Monthly Charges vs Churn Type")
p.show()
