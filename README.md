# 🚗 ABG Motors Market Expansion Analysis using Machine Learning and Tableau

> End-to-end Machine Learning and Business Analytics project for predicting customer purchasing behavior and identifying potential customers for market expansion.

---

# 📌 Project Overview

This project focuses on analyzing customer purchasing behavior using **Machine Learning** and **Business Analytics** techniques. The primary objective is to help **ABG Motors** identify potential customers in the Indian market by training a predictive classification model using historical customer data from the Japanese market.

A **Logistic Regression Classification Model** was developed using customer demographic and financial attributes such as age, gender, annual income, and vehicle age. The trained model was then applied to the Indian market dataset to estimate potential customers likely to purchase new vehicles.

Additionally, an interactive **Tableau Dashboard** was created to visualize customer demographics, purchasing patterns, income trends, and market expansion opportunities.

---

# 🎯 Business Objectives

- Understand customer purchasing behavior
- Predict customers likely to purchase new vehicles
- Identify high-potential customers in the Indian market
- Analyze demographic and financial factors influencing purchases
- Support business expansion decisions using data-driven insights
- Create interactive visualizations for market trend analysis

---

# 🧠 Machine Learning Objectives

- Perform data preprocessing and feature engineering
- Build a binary classification model
- Evaluate model performance using multiple metrics
- Interpret business meaning of model coefficients
- Predict customer purchase behavior using Logistic Regression

---

# 📂 Dataset Information

## 🇯🇵 Japanese Dataset

The Japanese dataset contains customer details and purchase history used for model training.

### Features Used

| Feature | Description |
|---|---|
| ID | Customer ID |
| CURR_AGE | Current Age |
| GENDER | Gender |
| ANN_INCOME | Annual Income |
| AGE_CAR | Age of Current Vehicle |
| PURCHASE | Purchase Status (0/1) |

### Dataset Size
- Total Records: **40,000**

---

## 🇮🇳 Indian Dataset

The Indian dataset contains customer demographic details used for prediction.

### Features Used

| Feature | Description |
|---|---|
| ID | Customer ID |
| CURR_AGE | Current Age |
| GENDER | Gender |
| ANN_INCOME | Annual Income |
| DT_MAINT | Maintenance Date |

### Dataset Size
- Total Records: **70,000**

---

# ⚙️ Tools & Technologies

## Programming & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Visualization
- Tableau

## Development Environment
- VS Code

---

# 🔄 Project Workflow

```text
Data Collection
        ↓
Data Cleaning & Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Selection
        ↓
Train-Test Split
        ↓
Feature Scaling
        ↓
Logistic Regression Model
        ↓
Model Evaluation
        ↓
Indian Market Prediction
        ↓
Tableau Dashboard Visualization
```

---

# 🧹 Data Preprocessing

The following preprocessing techniques were applied:

✅ Missing Value Analysis  
✅ Gender Encoding  
✅ Feature Scaling using StandardScaler  
✅ Feature Selection  
✅ Data Type Conversion  

### Gender Encoding

| Gender | Encoded Value |
|---|---|
| Male | 1 |
| Female | 0 |

---

# 📊 Exploratory Data Analysis

Several visualizations were created to analyze customer purchasing behavior.

## 📈 Customer Age Distribution
- Customers between 30–60 years contribute significantly to the market.

## 🛒 Purchase Distribution
- Buyers are higher than non-buyers, indicating positive demand.

## 👨‍💼 Gender vs Purchase Analysis
- Both genders show strong purchase activity.
- Male customers demonstrate slightly higher purchases.

## 💰 Income Distribution Analysis
- Higher income groups show stronger purchasing potential.

---

# 🤖 Machine Learning Model

## Logistic Regression Classification Model

A **Logistic Regression** algorithm was used to predict whether a customer is likely to purchase a new vehicle.

### Why Logistic Regression?

✅ Suitable for binary classification  
✅ Fast and efficient  
✅ Easy interpretation of coefficients  
✅ Good performance on structured datasets  

---

# 📏 Model Evaluation Metrics

The model was evaluated using multiple performance metrics.

## 📌 Accuracy Score

```text
Accuracy: 68.41%
```

---

## 📌 Classification Report

| Metric | Class 0 | Class 1 |
|---|---|---|
| Precision | 0.64 | 0.71 |
| Recall | 0.55 | 0.78 |
| F1-Score | 0.59 | 0.74 |

---

## 📌 Confusion Matrix

| Actual / Predicted | 0 | 1 |
|---|---|---|
| 0 | 1833 | 1516 |
| 1 | 1011 | 3640 |

---

# 📈 Business Interpretation of Coefficients

| Feature | Coefficient | Business Interpretation |
|---|---|---|
| CURR_AGE | -0.126194 | Slight negative impact on purchase probability |
| GENDER | 0.108943 | Small positive influence |
| ANN_INCOME | 0.403873 | Higher income increases purchasing likelihood |
| AGE_CAR | 0.846388 | Older vehicle owners are more likely to purchase |

---

# 🇮🇳 Indian Market Prediction

The trained model was applied to the Indian customer dataset.

## Prediction Results

| Category | Count |
|---|---|
| Potential Customers | 54,159 |
| Non-Potential Customers | 15,841 |

### Key Insight
The Indian market demonstrates strong business expansion opportunities for ABG Motors.

---

# 📊 Tableau Dashboard

An interactive Tableau dashboard was developed to visualize:

✅ Customer Age Distribution  
✅ Purchase Distribution  
✅ Gender vs Purchase Analysis  
✅ Income Distribution Analysis  
✅ Indian Market Prediction Analysis  

---

# 📸 Dashboard Visualizations

## 📌 Customer Age Distribution Analysis

![Customer Age Distribution](Screenshots/Customer_Age_Distribution.png)

---

## 📌 Purchase Distribution Analysis

![Purchase Distribution](Screenshots/Purchase_Distribution.png)

---

## 📌 Gender vs Purchase Analysis

![Gender vs Purchase](Screenshots/Gender_vs_Purchase.png)

---

## 📌 Income Distribution Analysis

![Income Distribution](Screenshots/Income_Distribution.png)

---

## 📌 Indian Market Prediction Analysis

![Indian Market Prediction](Screenshots/Indian_Market_Prediction.png)

# 🚀 Key Achievements

✅ Built an end-to-end Machine Learning pipeline  
✅ Applied Logistic Regression for classification  
✅ Performed business analytics and interpretation  
✅ Predicted 54,159 potential customers  
✅ Created professional Tableau dashboards  
✅ Generated business insights for market expansion  

---

# 📌 Future Enhancements

- Implement advanced ML algorithms (Random Forest, XGBoost)
- Improve prediction accuracy
- Add real-time prediction system
- Deploy as a web application
- Integrate cloud-based analytics

---

# 👨‍💻 Author

## Ajay Joseph
B.Tech Computer Science and Engineering  
SRM Institute of Science and Technology

---

# ⭐ Final Conclusion

This project successfully demonstrates the application of **Machine Learning**, **Business Analytics**, and **Data Visualization** techniques for customer purchase prediction and market expansion analysis. The insights generated from the model and Tableau dashboard can help ABG Motors make data-driven business decisions for future growth in the Indian market.
