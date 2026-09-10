"""
Stop words removal methods
    - removing English stop words (NLTK)
    - removing Turkish stop words (NLTK)
    - manually removing stop words pip install nltk
"""

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords") # download the stop words dataset

stop_words_eng = set(stopwords.words("english")) # English stop words list

# Example text
eng_text = "This is just a simple example to show how stop words can be removed from sentences"
eng_text_list = eng_text.split()
print(eng_text_list)

filtered_words_eng = [word for word in eng_text_list if word.lower() not in stop_words_eng]
print(f"Original: {eng_text}")
print(f"Filtered: {filtered_words_eng}")

# Turkish stop words analysis
stop_words_tr = set(stopwords.words("turkish"))
tr_text = "Merhaba, bugün sizler ile birlikte Google NLP eğitimi gerçekleştiriyoruz. Bu eğitim sizler için çok faydalı olacaktır."
tr_text_list = tr_text.split()

# Remove stop words
filtered_words_tr = [word for word in tr_text_list if word.lower() not in stop_words_tr]
print(f"Original: {tr_text}")
print(f"Filtered: {filtered_words_tr}")

# Removing stop words without using a library
custom_tr_stopwords = ["bu","ile","de","da","mi","ki"]
custom_text = "Bu bir denemedir, bunun için amacımız metinlerde ki bazı kelimeleri çıkartmak."
custom_text_list = custom_text.split()
filtered_custom_words_tr = [word for word in custom_text_list if word.lower() not in custom_tr_stopwords]
print(f"Original: {custom_text}")
print(f"Custom stop words çıkartılmış hali: {filtered_custom_words_tr}")

