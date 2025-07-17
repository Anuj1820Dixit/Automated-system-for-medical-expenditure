# 🩺 Medical Charges Prediction System – ACME Insurance Inc.

This project develops an **automated, explainable system** to estimate **annual medical expenditure** for new customers of ACME Insurance Inc., using demographic and lifestyle data such as:

- Age
- Sex
- BMI
- Number of Children
- Smoking Habit
- Region of Residence

These predictions are used to determine the **customer's insurance premium**, and comply with regulatory requirements for **transparency and interpretability**.

---

## 📊 Dataset

Source: [Medical Charges Dataset](https://github.com/stedy/Machine-Learning-with-R-datasets)  
CSV: [`medical-charges.csv`](https://raw.githubusercontent.com/JovianML/opendatasets/master/data/medical-charges.csv)

Each row contains the following fields:
- `age`: Age of primary beneficiary
- `sex`: Gender
- `bmi`: Body mass index
- `children`: Number of dependents
- `smoker`: Smoking status
- `region`: Residential area in the U.S.
- `charges`: Medical insurance charges billed by the insurance provider

---

## 🧪 Exploratory Data Analysis (EDA)

- Distribution plots of `age`, `bmi`, `charges` using **Plotly** and **Seaborn**
- Analysis of smoking habits, regional differences, and gender-based comparisons
- Correlation matrix to identify key features affecting medical charges

---

## 🧠 Modeling

- Preprocessing includes encoding categorical variables and creating interaction terms (e.g., age * BMI) to capture complex relationships.
- Models implemented include:
  - Linear Regression with interaction terms (for interpretability)
  - Random Forest Regressor (for accuracy comparison)
  - Gradient Boosting Regressor with hyperparameter tuning (for improved performance)
- Standardized feature scaling is applied to improve model convergence.
---

## 🚀 Deployment

The model is deployed as a **Django web application** with a two-step user interface:

1. **Step 1:** Calculate BMI by entering height and weight on the landing page.  
2. **Step 2:** Enter additional details — region, age, number of children, and smoking status — on the next page.  
3. **Prediction:** Based on the inputs, the system predicts the **annual medical charges** for the user and displays the result.

This deployment allows **interactive user input**, making the prediction process accessible and user-friendly for ACME Insurance’s customer onboarding.

---

## ✅ Interpretability

The model prioritizes **transparency**:
- Coefficients clearly reflect how each feature affects the predicted charge
- Suitable for **regulatory audits** and **fairness analysis**

---



