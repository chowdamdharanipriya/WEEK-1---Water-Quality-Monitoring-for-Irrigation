# WEEK-1---Water-Quality-Monitoring-for-Irrigation
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
