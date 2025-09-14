# WEEK-1,2---Water-Quality-Monitoring-for-Irrigation
Water Quality Monitoring for Irrigation: This project uses machine learning to predict water quality parameters like pH, salinity, and turbidity, helping farmers make informed irrigation decisions. It promotes sustainable agriculture by preventing soil degradation and optimizing water use.

Project Title:

Water Quality Monitoring for Irrigation

#Project Description:

Water quality is one of the most critical factors in sustainable agriculture, as it directly impacts soil health, crop productivity, and the long-term viability of farming practices. Contaminated or imbalanced irrigation water—due to high salinity, inappropriate pH levels, or turbidity—can cause soil degradation, reduce crop yield, and negatively affect the surrounding environment. To address these challenges, this project aims to develop a machine learning-based system to monitor and predict key water quality parameters, specifically pH, salinity, and turbidity, enabling farmers to make informed irrigation decisions.

The project focuses on collecting and processing water quality data from public datasets, IoT sensor readings, or simulated sources. After preprocessing, exploratory data analysis (EDA) is performed to identify patterns, trends, and correlations among different water parameters and environmental factors, such as seasonal changes and rainfall. These insights help in understanding the underlying factors affecting water quality and its suitability for irrigation.

Machine learning models, including regression and ensemble algorithms, are then trained to predict water quality parameters for future periods or conditions. By forecasting these values, farmers can plan irrigation schedules, choose suitable crops, and implement water treatment measures when necessary. For example, if predicted salinity levels are high, crops sensitive to salt can be avoided, or water can be treated before use. This approach not only improves crop yield but also minimizes the risk of long-term soil damage, contributing to sustainable farming practices.

The uniqueness of this project lies in its integration of environmental monitoring with agriculture, going beyond typical crop-focused prediction systems. By providing actionable insights based on water quality data, the system supports precision irrigation, reduces resource wastage, and promotes soil conservation.

In conclusion, this project demonstrates how machine learning can enhance sustainable agriculture by ensuring that irrigation practices are both effective and environmentally responsible. It equips farmers with predictive tools to make data-driven decisions, fostering long-term agricultural productivity and ecological balance.

#Project Explanation

This project focuses on predicting water potability using machine learning techniques. Access to safe and clean water is essential for both human health and agricultural practices. Poor water quality can cause health issues, reduce crop productivity, and degrade soil quality. Therefore, the ability to automatically classify water as potable (safe to drink) or non-potable (unsafe) has great significance in sustainable development.

The dataset used in this project contains important water quality indicators such as pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity. The target variable is Potability, which is labeled as 1 for safe water and 0 for unsafe water.

The raw dataset was first cleaned and preprocessed by handling missing values, removing duplicates, and scaling the features to ensure uniformity. Since the dataset was imbalanced (more unsafe than safe samples), we applied SMOTE (Synthetic Minority Oversampling Technique) and used balanced class weights to improve prediction fairness.

A Logistic Regression model was trained on 80% of the data and tested on the remaining 20%. The model’s performance was evaluated using accuracy, confusion matrix, precision, recall, F1-score, and ROC-AUC. The results show that machine learning can effectively support decision-making in water quality monitoring, ensuring safe water usage in agriculture and public health.



💧 Water Quality Monitoring for Irrigation
📌 Project Overview

Water quality plays a critical role in agriculture and irrigation practices. Poor-quality irrigation water can degrade soil health, reduce crop productivity, and harm the ecosystem. This project applies machine learning to analyze and predict water potability (whether water is safe or unsafe), based on multiple chemical and physical parameters such as pH, hardness, solids, chloramines, sulfate, conductivity, organic carbon, trihalomethanes, and turbidity.

The goal is to build a predictive system that helps farmers and environmentalists make informed decisions regarding irrigation water usage, promoting sustainable agriculture.

🎯 Objectives

Clean and preprocess raw water quality data.

Handle missing values, duplicates, and scaling of features.

Apply class balancing techniques (SMOTE, class weights) to address dataset imbalance.

Train and compare Logistic Regression and Random Forest Classifier.

Evaluate models with metrics like Accuracy, Confusion Matrix, Classification Report, ROC AUC.

Visualize results (ROC Curve, Feature Importance).

📂 Dataset

Source: Water Potability Dataset (public dataset).

Features include:

ph, Hardness, Solids, Chloramines, Sulfate,
Conductivity, Organic_carbon, Trihalomethanes, Turbidity

Target:

Potability → 1 (Potable / Safe) or 0 (Non-Potable / Unsafe).

🛠️ Data Preprocessing

Steps performed:

Duplicate Removal – Removed duplicate records.

Constant Feature Removal – Dropped columns with no variance.

Missing Values – Imputed using median strategy.

Correlation Analysis – Dropped highly correlated features (>0.9).

Scaling – Applied StandardScaler so each feature has mean=0 and std=1.

Target Retention – Reattached Potability column after cleaning.

Saved final cleaned dataset as:

water_potability_cleaned.csv

water_potability_cleaned.xlsx

🤖 Models Implemented
1️⃣ Logistic Regression

Balanced with class_weight="balanced" and SMOTE.

Accuracy: ~53%

ROC AUC Score: 0.55

📌 Observation: Logistic Regression struggled with this dataset due to non-linear relationships among water parameters.

2️⃣ Random Forest Classifier 🌳

Parameters:

n_estimators=200

max_depth=10

class_weight="balanced"

Accuracy: ~66%

ROC AUC Score: 0.68

Stronger performance compared to Logistic Regression.

Feature Importance identified which water quality indicators influenced predictions most.

📌 Observation: Random Forest handled feature interactions better and achieved higher recall & precision.

📊 Results Summary
Model	Accuracy	Precision (Safe)	Recall (Safe)	ROC AUC
Logistic Regression	~0.53	0.42	0.54	0.55
Random Forest	~0.66	0.57	0.52	0.68

✅ Random Forest is the better choice for this project.

📈 Visualizations

ROC Curves for both models.

Feature Importance chart (Random Forest).

🚀 How to Run

Create virtual environment & install dependencies:

python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt


Run Jupyter Notebook:

jupyter notebook


Open and run:

data_cleaning.ipynb → Cleaning process.

Sustainable_Agriculture_project.ipynb → Logistic Regression & Random Forest.

🌱 Impact

This project demonstrates how machine learning can be applied in agriculture and water management to:

Detect unsafe water early.

Prevent soil degradation.

Improve irrigation planning.

Support sustainable farming practices.

📝 Conclusion

Logistic Regression provides baseline performance.

Random Forest achieved better predictive power, making it the preferred model.

The system can be extended by adding IoT sensor data or integrating into a Streamlit dashboard for real-time monitoring.
