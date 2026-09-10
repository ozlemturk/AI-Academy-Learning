"""
Purpose:
    Basic data cleaning steps:
        - removing extra whitespace
        - converting uppercase letters to lowercase
        - removing punctuation marks
        - removing special characters
        - correcting spelling mistakes
        - removing HTML tags

pip install textblob beautifulsoup4
"""

# Removing extra whitespace
raw_text = "Python,      Google       NLP        dersi."
print(raw_text.split())

normalized_text1 = " ".join(raw_text.split())
print("Fazla boşlukları temizle: ", normalized_text1)

# Converting uppercase letters to lowercase
raw_text = "PYTHON, GooGle NLP"
normalized_text2 = raw_text.lower()
print(f"Temizlenmiş Veri: {normalized_text2}")

# Removing punctuation marks
import string
raw_text = "AI Natural-Language-Processing!"
normalized_text_3 = raw_text.translate(str.maketrans("","",string.punctuation)) # removes punctuation marks
print("Noktalam işaretleri temizlenmiş: ", normalized_text_3)

# Removing special characters such as %, &, /
import re # regular expression
raw_text = "Natural @ Language % Processing"
normalized_text_4 = re.sub(r"[^A-Za-z0-9\s]","",raw_text)
print(f"Özel karakterlerden kurtul: ", normalized_text_4)


# Correcting spelling mistakes
from textblob import TextBlob
# TextBlob works with English text
raw_text = "It is amazing in 2045"
normalized_text_5 = TextBlob(raw_text).correct()  # corrects spelling mistakes
print("Yazım Hatasız: ", normalized_text_5)

# Extracting plain text from HTML
from bs4 import BeautifulSoup
raw_html = "<div> 2045 Google </div>"
normalized_text_6 =BeautifulSoup(raw_html, "html.parser").get_text()
print(f"Html'den temizlenmiş: ",normalized_text_6)
