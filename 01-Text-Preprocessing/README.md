# Text Preprocessing

This folder contains practical implementations of fundamental **Natural Language Processing (NLP) text preprocessing techniques**. The examples were created as part of my learning process to understand how raw textual data can be cleaned, normalized, and prepared for further NLP tasks and machine learning models.

## Topics Covered

### 1. Data Cleaning

`1_data_cleaning.py`

Demonstrates common text cleaning and normalization operations, including:

* Removing extra whitespace
* Converting text to lowercase
* Removing punctuation
* Removing special characters using regular expressions
* Basic spelling correction with TextBlob
* Extracting text from HTML content using BeautifulSoup

### 2. Tokenization

`2_tokenization.py`

Introduces tokenization, one of the fundamental preprocessing steps in NLP.

The examples include:

* Word tokenization
* Sentence tokenization
* Tokenization using NLTK

### 3. Stemming and Lemmatization

`3_stemming_lemmatization.py`

Explores two common text normalization techniques:

* **Stemming:** Reduces words to their approximate root form using `PorterStemmer`.
* **Lemmatization:** Converts words to their dictionary base form using `WordNetLemmatizer`.

These techniques help reduce variations of words before further text analysis.

### 4. Stop Word Removal

`4_stop_words_removal.py`

Demonstrates different approaches to removing frequently occurring words that may carry limited information for certain NLP tasks.

The examples include:

* English stop word removal using NLTK
* Turkish stop word removal using NLTK
* Custom stop word removal using a manually defined list

## Technologies & Libraries

* Python
* NLTK
* TextBlob
* BeautifulSoup
* Regular Expressions (`re`)
* Python `string` module

## Purpose

The purpose of these exercises is to build a strong foundation in NLP preprocessing and understand how raw text can be transformed into cleaner and more structured data before applying techniques such as text representation, machine learning, and deep learning.

This folder is part of my ongoing AI and NLP learning journey and will be expanded as I continue exploring new concepts and techniques.
