#%%
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
#%%
train_df = pd.read_csv("train.csv")
test_df = pd.read_csv("test.csv")
train_df = train_df[train_df["Language"] == "en"].dropna()
test_df = test_df.dropna()
#%%
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=10000, lowercase=True, stop_words='english')),
    ('svd', TruncatedSVD(n_components=100, random_state=42)),
    ('rf', RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1))
])
#%%
# Backup
train = train_df
test = test_df
print(train_df)
#%%
# Addestriamo il modello sui dati di training
pipeline.fit(train['Lyrics'], train['Genre'])
#%%
# Usiamo il modello per predire il genere sui dati di test
preds = pipeline.predict(test['Lyrics'])
#%%
# Calcoliamo e stampiamo l'accuratezza (o eventuali altre metriche)
acc = accuracy_score(test['Genre'], preds)
print("Accuracy sul test set:", acc)
#%%
# Save
with open('model_genre.pkl', 'wb') as file:
    pickle.dump(pipeline["rf"], file)

with open('vectorizer_genre.pkl', 'wb') as file:
    pickle.dump(pipeline["tfidf"], file)

with open('svd_genre.pkl', 'wb') as file:
    pickle.dump(pipeline["svd"], file)

##################### With embedding ###################
#%%
#Load
with open('model_genre.pkl', 'rb') as file:
    model_genre = pickle.load(file)

with open('vectorizer_genre.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)

with open('svd_genre.pkl', 'rb') as file:
    svd = pickle.load(file)
# Function definition
#%%
def predict_genre(text):
    
    predicted_genre = model_genre.predict_proba(svd.transform(tfidf_vectorizer.transform([text])))
    top_three_indices = predicted_genre[0].argsort()[::-1][:3]
    predicted_genre = model_genre.classes_[top_three_indices]

    return predicted_genre
    

# %%
result = predict_genre("yolo etet")
print(result)
# %%

########################## Without Embedding ####################################
#Load
with open('vectorizer_genre_token_heavy.pkl', 'rb') as file:
    tfidf_vectorizer = pickle.load(file)
    
with open('model_genre_token_heavy.pkl', 'rb') as file:
    model = pickle.load(file)

#%%
def predict_genre_token(text):
    
    predicted_genre = model_genre.predict_proba(tfidf_vectorizer.transform([text]))
    top_three_indices = predicted_genre[0].argsort()[::-1][:3]
    predicted_genre = model_genre.classes_[top_three_indices]

    return predicted_genre
    

# %%
result = predict_genre("yolo etet")
print(result)
