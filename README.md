# emial_classifier

A machine learning model that automatically classifies emails into four categories: Spam, Services, Professional, and Personal.
Overview
This project uses Logistic Regression with TF-IDF text vectorization to classify emails based on their content. The model analyzes email text and predicts which category it belongs to.

# Categories

Spam: Unwanted promotional or junk emails
Services: Service-related communications
Professional: Work or business-related emails
Personal: Personal correspondence

# Requirements
python
pandas
numpy
scikit-learn
# Install dependencies
pip install pandas numpy scikit-learn
# Dataset
The model expects a CSV file (email.csv) with the following structure:

text: Email content
label: Category label (0-3 representing the four categories)

# Example Output
recall_score: 0.87
accuracy_score: 89.45%
classification_report: [detailed metrics]

email perpos: This is a promotional offer...
The type of mail: 0



This project is open-source and available for educational purposes.
