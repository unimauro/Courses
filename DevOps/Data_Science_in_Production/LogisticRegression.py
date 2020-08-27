from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
import pandas as pd
# Games data set
gamesDF = pd.read_csv("https://github.com/bgweber/Twitch/raw/
master/Recommendations/games-expand.csv")

x_train, x_test, y_train, y_test = train_test_split(
gamesDF.drop(['label'],axis=1),gamesDF['label'],test_size=0.3)
model = LogisticRegression()
model.fit(x_train, y_train)
print("Accuracy: " + str(model.score(x_test, y_test)))
print("ROC: " + str(roc_auc_score(y_test,
model.predict_proba(x_test)[:, 1] )))


