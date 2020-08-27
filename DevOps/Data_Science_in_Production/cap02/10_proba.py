import pickle
pickle.dump(model, open("logit.pkl", 'wb'))
model = pickle.load(open("logit.pkl", 'rb'))
model.predict_proba(x)
