import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import rpy2.robjects.packages as rpackages
import warnings
import pandas as pd

# Too many warnings
warnings.filterwarnings("ignore")

# Funzione per installare un pacchetto R
def install_r_package(package_name):
    utils = rpackages.importr('utils')
    utils.chooseCRANmirror(ind=1)  # Scegli uno specchio CRAN
    utils.install_packages(package_name)

# Installa i pacchetti uno alla volta
install_r_package('tm')
install_r_package('SnowballC')
install_r_package('randomForest')
install_r_package('caret')

# Importa le librerie necessarie
tm = importr('tm')
SnowballC = importr('SnowballC')
randomForest = importr('randomForest')
caret = importr('caret')

# Carica il testo
#text = pd.read_csv("train.csv")

# Definisci la funzione R
r_code = """

model = readRDS("rf_model.rds")
dtm = readRDS("DTM.rds")

# Funzioni di preprocessing

genre_predict = function(text){

  #Create corpus
  text_corpus <- Corpus(VectorSource(text))

  # Clean corpus
  text_corpus <- tm_map(text_corpus, content_transformer(tolower))
  text_corpus <- tm_map(text_corpus, removePunctuation)
  text_corpus <- tm_map(text_corpus, removeNumbers)
  text_corpus <- tm_map(text_corpus, removeWords, stopwords("en"))
  text_corpus <- tm_map(text_corpus, stemDocument)
  text_corpus <- tm_map(text_corpus, stripWhitespace)

  new_dtm <- DocumentTermMatrix(text_corpus)

  # Convertire le matrici in formato compatibile
  new_terms <- colnames(new_dtm)  # Termini presenti nella nuova DTM
  old_terms <- colnames(dtm)      # Termini presenti nella vecchia DTM

  # Creare una nuova DTM vuota con le stesse righe di dtm e colonne di new_dtm
  filtered_dtm <- matrix(0, nrow = nrow(new_dtm), ncol = length(old_terms))
  colnames(filtered_dtm) <- old_terms

  # Aggiornare i valori solo per le colonne presenti in entrambe le matrici
  common_terms <- intersect(new_terms, old_terms)
  filtered_dtm[, common_terms] <- as.matrix(new_dtm[, common_terms])

  # Model evaluation
  predictions <- predict(model, filtered_dtm)

  # Output of prevision
  return(predictions)
}
"""

# Esegui il codice R
robjects.r(r_code)

# Richiama la funzione R da Python
genre_predict = robjects.globalenv['genre_predict']
result = genre_predict('country')
print(result)
