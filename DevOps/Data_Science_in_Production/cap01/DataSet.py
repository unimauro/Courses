from sklearn.datasets import load_boston
import pandas as pd
data, target = load_boston(True)
bostonDF = pd.DataFrame(data, columns=load_boston().feature_names)
bostonDF['label'] = target
bostonDF.head()

gamesDF = pd.read_csv("https://github.com/bgweber/
Twitch/raw/master/Recommendations/games-expand.csv")
gamesDF.head()
