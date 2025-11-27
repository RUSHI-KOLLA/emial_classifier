# emial_classifier
```
A machine learning model that automatically classifies emails into four categories: Spam, Services, Professional, and Personal.
Overview
This project uses Logistic Regression with TF-IDF text vectorization to classify emails based on their content. The model analyzes email text and predicts which category it belongs to.
```
# Categories
```
Spam: Unwanted promotional or junk emails
Services: Service-related communications
Professional: Work or business-related emails
Personal: Personal correspondence
```
# Requirements
```
python
pandas
numpy
scikit-learn
```
# Install dependencies
```
pip install pandas numpy scikit-learn
```
# Dataset
```
The model expects a CSV file (email.csv) with the following structure:

text: Email content
label: Category label (0-3 representing the four categories)
```
# Example Output
```
There is any infinity val:False
recall_score:0.9875
 accuracy_score:98.55%
 classification_report:              precision    recall  f1-score   support

    personal       1.00      1.00      1.00        17
   promotion       1.00      0.95      0.97        20
     service       0.94      1.00      0.97        17
        spam       1.00      1.00      1.00        15

    accuracy                           0.99        69
   macro avg       0.99      0.99      0.99        69
weighted avg       0.99      0.99      0.99        69


email perpos: Dear All,
This is to inform you that TCS is conducting the TCS HackQuest Season 10 contest for all III & IV Year (2026 & 2027 Batch) B...
The type of mail:: promotion
email perpos: This is a promotional offer...
The type of mail: 0
```



