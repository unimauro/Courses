from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# See Section 1.4 (Boston Hosing data set)
bostonDF = ...
x_train, x_test, y_train, y_test = train_test_split(
bostonDF.drop(['label'],axis=1),bostonDF['label'],test_size=0.3)
model = LinearRegression()
model.fit(x_train, y_train)
print("R^2: " + str(model.score(x_test, y_test)))
print("Mean Error: " + str(sum(
abs(y_test - model.predict(x_test) ))/y_test.count()))


