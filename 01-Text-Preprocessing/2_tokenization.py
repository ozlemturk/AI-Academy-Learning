"""
Let's perform tokenization, one of the basic preprocessing steps in natural language processing.
    - word tokenization
    - sentence tokenization

pip install nltk
"""

import nltk # Natural Language Toolkit
nltk.download("punkt") # required data for word and sentence tokenization

# Define an example text

raw_text = ("Merhaba Google! Bu bir NLP eğitimidir. NLP eğitiminin ilerleyen aşamalarında "
            "LLM konusunu öğrenelim.")

# Word tokenization
word_tokens = nltk.word_tokenize(raw_text)
print(f"Kelime tokens: {word_tokens}")

# Sentence tokenization
sentence_tokens = nltk.sent_tokenize(raw_text)
print(f"Cümle tokens: {sentence_tokens}")