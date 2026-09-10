"""
Finding roots and lemmas
    - stemming: Porter Stemmer
    - lemmatization: WordNet Lemmatizer

pip install nltk
"""

import nltk
nltk.download("wordnet") # WordNet database required for finding lemmas
nltk.download("omw-1.4") # additional language support for WordNet

# Stemming
from nltk.stem import PorterStemmer # popular stemming algorithm for English
stemmer = PorterStemmer() # create a Porter Stemmer object
words_stem = ["playing","played","plays","happier","happily","studying","studies"]

stems = [stemmer.stem(w) for w in words_stem]
print(f"Original: {words_stem}")
print(f"Stems: {stems}")


# Lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words_lemma = ["running","ran","gone","better","children"]
lemmas = [lemmatizer.lemmatize(w) for w in words_lemma]
print(f"Original: {words_lemma}")
print(f"Lemmas: {lemmas}")