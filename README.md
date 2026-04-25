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
\[
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i
\]
Used to replace missing values by calculating the average of each feature.

---

### 2. Correlation Coefficient (Feature Relationship)
\[
r = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum (x_i - \bar{x})^2 \sum (y_i - \bar{y})^2}}
\]
Measures the strength and direction of the relationship between variables (e.g., BP and cholesterol).

---

### 3. Risk Scoring Function
\[
\text{Risk Score} = w_1 \cdot Age + w_2 \cdot BP + w_3 \cdot Cholesterol + w_4 \cdot HeartRate + w_5 \cdot Exang + w_6 \cdot Oldpeak
\]
A weighted scoring system combining multiple clinical parameters.

---

### 4. Risk Classification Model
\[
\text{Risk} =
\begin{cases}
\text{High}, & \text{if } score \geq 5 \\
\text{Moderate}, & \text{if } 3 \leq score < 5 \\
\text{Low}, & \text{if } score < 3
\end{cases}
\]
Classifies patients into risk categories.

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
