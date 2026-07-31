# 🩸 Give Life: Predict Blood Donations Dashboard

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://usebondedblood-donation-dashboard.streamlit.app/)

## Overview
The **Predict Blood Donations Dashboard** is an interactive, data-driven web application built with Python and Streamlit. It utilizes a machine learning classification model to predict the likelihood of an individual donating blood based on their historical donation data. 

This project serves as a practical implementation of machine learning concepts, data visualization, and web deployment, showcasing end-to-end development in Artificial Intelligence and Machine Learning (AIML).

## 🚀 Live Demo
**Test the live application here:** [Blood Donation Dashboard](https://usebondedblood-donation-dashboard.streamlit.app/)

## ✨ Key Features
*   **Live Machine Learning Predictions:** Uses a trained Logistic Regression model to instantly predict donation likelihood.
*   **Interactive User Interface:** Features a sidebar with adjustable sliders for Recency, Frequency, Monetary, and Time values to test different donor scenarios.
*   **Real-Time Analytics:** Displays core metrics such as model accuracy, total sampled donors, and average donation frequency.
*   **Data Visualization:** Includes dynamic charts mapping out the distribution of donor frequency and recency.

## 🛠️ Technology Stack
*   **Language:** Python
*   **Frontend Framework:** Streamlit
*   **Data Manipulation:** Pandas
*   **Machine Learning:** Scikit-Learn (Logistic Regression)

## 📊 Dataset Context
This model is trained on the Blood Transfusion Service Center Data Set (`transfusion.data`). The dataset utilizes the RFM (Recency, Frequency, Monetary) model, a common method for analyzing customer/donor value:
*   **R (Recency):** Months since last donation.
*   **F (Frequency):** Total number of donations.
*   **M (Monetary):** Total blood donated in c.c.
*   **T (Time):** Months since first donation.

## 💻 How to Run Locally

If you wish to run this dashboard on your own machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Usebonded/blood-donation-dashboard-.git](https://github.com/Usebonded/blood-donation-dashboard-.git)
   cd blood-donation-dashboard-
