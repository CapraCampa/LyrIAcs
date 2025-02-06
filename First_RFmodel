# Installare e caricare i pacchetti necessari
#install.packages("tm")
#install.packages("SnowballC")
#install.packages("randomForest")
#install.packages("caret")
#install.packages("kagglehub")
library(tm)
library(SnowballC)
library(randomForest)
library(caret)

setwd("C:/Users/Andrea/Desktop/Mlops")

# Caricare e preparare i dati
data <- read.csv("train.csv")
data = data[data$Language=="en",]

# Rimuovere gli NA
data <- na.omit(data)
summary(data)

# Creare un corpus di testo
corpus <- Corpus(VectorSource(data$Lyrics))

# Pulire il testo
corpus <- tm_map(corpus, content_transformer(tolower))
corpus <- tm_map(corpus, removePunctuation)
corpus <- tm_map(corpus, removeNumbers)
corpus <- tm_map(corpus, removeWords, stopwords("en"))
corpus <- tm_map(corpus, stemDocument)
corpus <- tm_map(corpus, stripWhitespace)

# Creare una matrice di termini-documenti
dtm <- DocumentTermMatrix(corpus)

# Rendere factors i generi
trainLabels = as.factor(data$Genre)

# Rimuovere termini rari
dtm <- removeSparseTerms(dtm, 0.99)

#Save and load data
#saveRDS(dtm,"DTM.rds")
#dtm = readRDS("DTM.rds")

# Convertire la matrice in formato compatibile
trainData <- as.matrix(dtm)

# Addestrare il modello Random Forest
model <- randomForest(trainData, as.factor(trainLabels), ntree = 100, do.trace = TRUE)

################## Testing

# Caricare il nuovo dataset
new_data <- read.csv("test.csv")

# Rimuovere gli NA
new_data <- na.omit(new_data)

# Creare un corpus di testo e pulire il testo
new_corpus <- Corpus(VectorSource(new_data$Lyrics))
new_corpus <- tm_map(new_corpus, content_transformer(tolower))
new_corpus <- tm_map(new_corpus, removePunctuation)
new_corpus <- tm_map(new_corpus, removeNumbers)
new_corpus <- tm_map(new_corpus, removeWords, stopwords("en"))
new_corpus <- tm_map(new_corpus, stemDocument)
new_corpus <- tm_map(new_corpus, stripWhitespace)

# Creare la matrice di termini-documenti
new_dtm <- DocumentTermMatrix(new_corpus)

# Convertire la matrice in formato compatibile
testData <- as.matrix(new_dtm)

# Valutare il modello
predictions <- predict(model, testData)
confusionMatrix(predictions, as.factor(new_data$Genre))

#Save and load model
#saveRDS(model, file = "rf_model.rds")
#model = readRDS("rf_model.rds")
