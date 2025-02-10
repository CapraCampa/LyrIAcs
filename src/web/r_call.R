install.packages("SnowballC", repos = "http://cran.us.r-project.org")
install.packages("tm", repos = "http://cran.us.r-project.org")
install.packages("randomForest", repos = "http://cran.us.r-project.org")
install.packages("caret", repos = "http://cran.us.r-project.org")
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

args <- commandArgs(trailingOnly = TRUE)
text <- args[1]

result <- genre_predict(text)
print(result)