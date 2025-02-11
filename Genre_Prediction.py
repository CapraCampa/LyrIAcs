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
#%%
os.chdir('C:/Users/Andrea/Desktop/MLOps')
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
train_df = train_df[train_df["Language"] == "en"].dropna()
test_df = test_df.dropna()
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
train = train_df
test = test_df
#%%
# Model fitting
pipeline.fit(train['Lyrics'], train['Genre'])
#%%
# Calcoliamo e stampiamo l'accuratezza e altre metriche
print(classification_report(test['Genre'], pipeline.predict(test['Lyrics'])))
#%%
# Save
with open('pipeline_logistic.pkl', 'wb') as file:
    pickle.dump(pipeline, file)
#%%
############################### From here Load and Function ###################################################

#Load
with open('pipeline_logistic.pkl', 'rb') as file:
    pipeline_genre = pickle.load(file)

#%%
def predict_genre(text):
    
    predicted_genre = pipeline_genre.predict_proba([text])

    top_three_indices = predicted_genre[0].argsort()[::-1][:3]
    predicted_genre = pipeline_genre.classes_[top_three_indices]

    return predicted_genre
    

# %%
result = predict_genre("yolo etet")
print(result)
# %%
