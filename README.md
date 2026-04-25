# ❤️ Cardiac Health Risk Analysis System

## 📊 Overview

A data-driven system that analyzes cardiac health indicators to identify potential risk patterns using statistical analysis and visualization techniques.

## 🎯 Objectives

* Analyze patient health data from CSV
* Identify high-risk cardiac patterns
* Provide actionable insights using visual analytics

## ⚙️ Features

* Data preprocessing (cleaning & handling missing values)
* Multi-factor risk scoring system
* Data visualization (scatter plots, heatmaps)
* Automated result generation (CSV output)

## 🛠️ Tech Stack

* Python
* Pandas
* Matplotlib
* Seaborn

## 📁 Dataset

* CSV-based dataset with cardiac health indicators
* Includes features like age, blood pressure, cholesterol, heart rate, etc.

## ▶️ How to Run

```bash
pip install pandas matplotlib seaborn
python main.py
```
## 📐 Mathematical Tools & Formulas

### 1. Mean (Handling Missing Values)
x̄ = (1/n) Σ xi  
Used to replace missing values by calculating the average of each feature.

---

### 2. Correlation Coefficient (Feature Relationship)
r = Σ[(xi - x̄)(yi - ȳ)] / √[Σ(xi - x̄)² Σ(yi - ȳ)²]  
Measures the strength and direction of the relationship between variables.

---

### 3. Risk Scoring Function
Risk Score = w1·Age + w2·BP + w3·Cholesterol + w4·HeartRate + w5·Exang + w6·Oldpeak  
A weighted scoring system combining multiple clinical parameters.

---

### 4. Risk Classification Model

- High Risk → score ≥ 5  
- Moderate Risk → 3 ≤ score < 5  
- Low Risk → score < 3  

Classifies patients into risk categories.

---

## 🧠 Analytical Techniques Used
- Statistical Analysis (Mean, Correlation)
- Rule-Based Risk Scoring
- Data Visualization

---

## 🧠 Analytical Techniques Used
- Statistical Analysis (Mean, Correlation)
- Rule-Based Risk Scoring
- Data Visualization

---

## 📌 Summary
This project applies statistical methods and a rule-based scoring model to analyze cardiac health data. Mathematical concepts such as mean and correlation are used for preprocessing and analysis, while a custom scoring function determines patient risk levels.

⋅
## 📊 Output

* Risk classification (Low / Moderate / High)
* Visual graphs
* Output saved as CSV file

## 📌 Future Improvements

* Add Machine Learning prediction model
* Build GUI dashboard
* Deploy as a web application

## 👨‍💻 Author

Aditya Kumar
