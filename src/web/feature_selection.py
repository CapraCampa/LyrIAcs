import streamlit as st
import subprocess

#import os
# THIS LINE CHANGES BASED ON YOUR R VERSION/LOCATION
#os.environ["R_HOME"] = r"C:\Program Files\R\R-4.4.1"
#os.environ["R_LIBS_USER"]= r"C:/Users/desta/AppData/Local/R/win-library/4.4"
#from rpy2.robjects import r, pandas2ri
#from rpy2.robjects.packages import importr
#import rpy2.robjects.packages as rpackages
import warnings
import pandas as pd

# Load R model and functions
r_code = """
#.libPaths("C:/Users/desta/AppData/Local/R/win-library/4.4")
library(tm)
library(SnowballC)
library(randomForest)
library(caret)
model = readRDS("../../artifacts/rf_model.rds")
dtm = readRDS("../../data/processed/DTM.rds")

genre_predict = function(text){
    text_corpus <- Corpus(VectorSource(text))
    text_corpus <- tm_map(text_corpus, content_transformer(tolower))
    text_corpus <- tm_map(text_corpus, removePunctuation)
    text_corpus <- tm_map(text_corpus, removeNumbers)
    text_corpus <- tm_map(text_corpus, removeWords, stopwords("en"))
    text_corpus <- tm_map(text_corpus, stemDocument)
    text_corpus <- tm_map(text_corpus, stripWhitespace)

    new_dtm <- DocumentTermMatrix(text_corpus)
    print(dim(new_dtm)) 

    new_terms <- colnames(new_dtm)
    old_terms <- colnames(dtm)

    common_terms <- intersect(new_terms,old_terms)
    print(common_terms)

    filtered_dtm <- matrix(0, nrow = nrow(new_dtm), ncol = length(old_terms))
    colnames(filtered_dtm) <- old_terms

    common_terms <- intersect(new_terms, old_terms)
    filtered_dtm[, common_terms] <- as.matrix(new_dtm[, common_terms])

    predictions <- predict(model, filtered_dtm, type = "prob")
    predictions <- as.matrix(predictions)
    print(predictions)
    # Sort predictions by probability and get the top 3
    sorted_indices <- order(predictions[1,], decreasing = TRUE)[1:3]
    top_3_genres <- colnames(predictions)[sorted_indices]
    
    print(top_3_genres)
    return(top_3_genres)
}
"""
#r(r_code)  # Executes the R code
#genre_predict = r['genre_predict']  # Access R function

# Title
st.markdown("""
    <h1 style='text-align: center;'>LyrIAcs</h1>
    <p style='text-align: center;'>Select your preferences</p>
""", unsafe_allow_html=True)

if 'user_lyrics' in st.session_state:
    user_lyrics = st.session_state.user_lyrics
else:
    st.warning("No lyrics found. Please go back and input lyrics.")


with st.spinner('Predicting genre...'):
    process1 = subprocess.Popen(["Rscript","r_call.R", user_lyrics], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout,stderr = process1.communicate()
    if process1.returncode != 0:
        st.error(f"Error in R script: {stderr}")
    else:

        result = (stdout.strip().split('\n')[-1]).split()[-3:]
        st.success('Prediction complete!')

with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    options = list(result)
    genres = left.pills("Choose a **genre**:", options, selection_mode="multi")
    genres_random = right.pills("", ["Random "], selection_mode="single")

# Emotions Selection (single selection only)
with st.container(border=True):
    left, right = st.columns(2, vertical_alignment="center")
    options = ["Love", "Sadness", "Rage", "Happiness"]
    emotions = left.pills("Choose a **emotion**:", options, selection_mode="multi")
    emotions_random = right.pills("", ["Random "], selection_mode="single")

cols = st.columns(6, vertical_alignment="center")
if cols[-1].button("Continue"):
    st.switch_page("generate_lyrics.py")
