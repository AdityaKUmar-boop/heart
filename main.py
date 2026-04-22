# ============================================
# Cardiac Health Risk Analysis System (Final)
# CSV आधारित Professional Version (No ML)
# ============================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# 1. Load Data
# -------------------------------
def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("✅ Data loaded successfully!\n")
        return df
    except Exception as e:
        print("❌ Error loading file:", e)
        return None

# -------------------------------
# 2. Data Cleaning
# -------------------------------
def clean_data(df):
    print("🔧 Cleaning data...")

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values
    df.fillna(df.mean(numeric_only=True), inplace=True)

    print("✅ Data cleaning completed!\n")
    return df

# -------------------------------
# 3. Risk Scoring System
# -------------------------------
def calculate_risk(row):
    score = 0

    # Age
    if row['age'] > 50:
        score += 1

    # Blood Pressure
    if row['trestbps'] > 140:
        score += 2

    # Cholesterol
    if row['chol'] > 240:
        score += 2

    # Heart Rate
    if row['thalach'] < 100:
        score += 1

    # Exercise-induced angina
    if row['exang'] == 1:
        score += 2

    # ST depression
    if row['oldpeak'] > 2:
        score += 2

    # Final classification
    if score >= 5:
        return "High Risk"
    elif score >= 3:
        return "Moderate Risk"
    else:
        return "Low Risk"

# -------------------------------
# 4. Analysis
# -------------------------------
def analyze_data(df):
    print("📊 Performing analysis...")

    df['Risk'] = df.apply(calculate_risk, axis=1)

    print("\n🔍 Risk Summary:")
    print(df['Risk'].value_counts())

    return df

# -------------------------------
# 5. Visualization
# -------------------------------
def visualize(df):

    print("\n📈 Generating graphs...")

    # Scatter Plot
    plt.figure()
    plt.scatter(df['trestbps'], df['chol'])
    plt.xlabel("Blood Pressure")
    plt.ylabel("Cholesterol")
    plt.title("BP vs Cholesterol")
    plt.show()

    # Risk Distribution
    plt.figure()
    sns.countplot(x='Risk', data=df)
    plt.title("Risk Distribution")
    plt.show()

    # Correlation Heatmap
    plt.figure()
    sns.heatmap(df.corr(numeric_only=True), annot=True)
    plt.title("Correlation Matrix")
    plt.show()

# -------------------------------
# 6. Save Output (Professional Touch)
# -------------------------------
def save_results(df):
    df.to_csv("output_results.csv", index=False)
    print("\n💾 Results saved as output_results.csv")

# -------------------------------
# 7. Main Function
# -------------------------------
def main():
    file_path = "heart.csv"

    df = load_data(file_path)

    if df is not None:
        df = clean_data(df)
        df = analyze_data(df)
        visualize(df)
        save_results(df)

        print("\n✅ Project Executed Successfully!")

# Run program
if __name__ == "__main__":
    main()
