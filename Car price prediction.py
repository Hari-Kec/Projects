import pandas as pd
from google.colab import files
uploaded=files.upload()
dataset=pd.read_csv('table.csv')
print(dataset)
x=dataset.iloc[:,:-1].values
x
y=dataset.iloc[:,-1].values
y
pip install scikit-learn
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
print(x_train)
from sklearn.linear_model import LogisticRegression
model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
from sklearn.metrics import accuracy_score
print("Accuracy of the model: {0}%".format(accuracy_score(y_test,y_pred)*100))
age=int(input("Enter New customer age: "))
sal=int(input("Enter New customer salary: "))
newCust=[[age,sal]]
result=model.predict(sc.transform(newCust))
print(result)
if result==1:
  print("Customer will buy")
else:
  print("Customer won't buy")
