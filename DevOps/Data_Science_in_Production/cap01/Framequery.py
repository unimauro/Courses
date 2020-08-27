import framequery as fq
# assign labels to the generated features
features = fq.execute("""
SELECT f.*
,case when g.type = 'P' then 1 else 0 end as label
FROM features f
JOIN game_df g
on f.game_id = g.game_id
""")

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
# create inputs for sklearn
y = features['label']
X = features.drop(['label', 'game_id'], axis=1).fillna(0)
# train a classifier
lr = LogisticRegression()
model = lr.fit(X, y)
# Results
print("Accuracy: " + str(model.score(X, y)))
print("ROC" + str(roc_auc_score(y,model.predict_proba(X)[:,1])))


