import numpy as numpy
import matplotlib.pyplot as mtp  
import pandas as pd
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
regressor= LinearRegression()  


dataset = pd.read_csv('salary.csv')
x = dataset.iloc[:, :-1].values   # x is a independent variable
y= dataset.iloc[:, 1].values     # y is a dependent variabe


x_train, x_test, y_train, y_test= train_test_split(x, y, test_size= 1/3, random_state=0)  

regressor.fit(x_train, y_train)  


y_pred= regressor.predict(x_test)  
x_pred= regressor.predict(x_train)  


y_pred= regressor.predict(x_test)  
x_pred= regressor.predict(x_train)  

mtp.scatter(x_train, y_train, color="green")   
mtp.plot(x_train, x_pred, color="red")    
mtp.title("Salary vs Experience (Training Dataset)")  
mtp.xlabel("Years of Experience")  
mtp.ylabel("Salary(In Rupees)")  
mtp.show()   