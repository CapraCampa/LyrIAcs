#%%
import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
#%%
os.chdir('C:/Users/Andrea/Desktop/MLOps')
df = pd.read_csv("combined_emotion.csv")
df = df.dropna()
#%%
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=10000,
                                lowercase=True,
                                stop_words='english')),
    ('svd', TruncatedSVD(n_components=150)),
    ('clf', LogisticRegression(solver='saga',
                                class_weight='balanced',
                                C = 1,
                                max_iter=1000,
                                n_jobs=-1,
                                verbose = 5))
    ])
#%%
# Backup

X_train, X_test, y_train, y_test = train_test_split(df['sentence'], df['emotion'], test_size=0.2, random_state=42)

#%%
# Model fitting
pipeline.fit(X_train, y_train)
#%%
# Calcoliamo e stampiamo l'accuratezza e altre metriche
print(classification_report(y_test, pipeline.predict(X_test)))
#%%
# Save
with open('pipeline_logistic_emo.pkl', 'wb') as file:
    pickle.dump(pipeline, file)
############################### From here Load and Function ###################################################
#%%
#Load
with open('pipeline_logistic_emo.pkl', 'rb') as file:
    pipeline_emo = pickle.load(file)

#%%
def predict_emo(text):
    
    predicted_emo = pipeline_emo.predict_proba([text])

    top_three_indices = predicted_emo[0].argsort()[::-1][:3]
    predicted_emo = pipeline_emo.classes_[top_three_indices]

    return predicted_emo
    

# %%
result = predict_emo("yolo etet")
print(result)
# %%
