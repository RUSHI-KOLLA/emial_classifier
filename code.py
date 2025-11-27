import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import recall_score,classification_report,accuracy_score
df = pd.read_csv(r'C:\\Users\\kolla\\OneDrive\\Documents\\Desktop\\email.csv')
#print(df.info())

x = df['text']
y = df['label']

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state= 42)

vec = TfidfVectorizer() # convert text into numeric
x_train = vec.fit_transform(x_train)
x_test = vec.transform(x_test)
print(x_train)
print(df.info())
print(f"There is any infinity val:{np.isinf(x_train.data).any()}")

model = LogisticRegression()

model.fit(x_train,y_train)

pre = model.predict(x_test)

recall = recall_score(y_test,pre,average='macro')
accuracy = accuracy_score(y_test,pre)
clre = classification_report(y_test,pre)

print(f'recall_score:{recall}\n accuracy_score:{accuracy*100:.2f}% \n classification_report:{clre}\n')

with open(r"C:\\Users\\kolla\\OneDrive\Documents\\promotion.txt",encoding='utf-8')as file:
    col = file.read()

def sumu(col:str):
    sam = col.split(".")
    if len(sam) > 1:
        return sam[0].strip()+'...'
    else:
        return col[:140].strip()+'...'

sum = sumu(col)
print('email perpos:',sum)
    
col = vec.transform([col])
fr = model.predict(col)
print(f"The type of mail:: {np.max(fr)}")