import pandas as pd
from sklearn.linear_model import LogisticRegression
df = pd.read_csv("https://github.com/bgweber/Twitch/
raw/master/Recommendations/games-expand.csv")
x = df.drop(['label'], axis=1)
y = df['label']
model = LogisticRegression()
model.fit(x, y)
