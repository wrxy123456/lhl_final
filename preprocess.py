import re

def cleanhtml(raw_html):
    # remove html tags like <br> and &quot
    cleanr = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')
    cleantext = re.sub(cleanr, '', raw_html)
    # remove hyper links
    cleantext = re.sub(r'http\S+', '', cleantext)
    
    return cleantext


# Lemmatize the documents
from nltk.stem.wordnet import WordNetLemmatizer
def lemmatize(doc):
    lemmatizer = WordNetLemmatizer()
    doc = [lemmatizer.lemmatize(token) for token in doc]
    return doc


# Preprocess the documents.
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
stop_words.add('game')
stop_words.add('new')

def preprocess(doc):
    tokenizer = RegexpTokenizer(r'\w+')
    doc = doc.lower() # Convert to lowercase.
    doc = cleanhtml(doc) # clean html
    doc = tokenizer.tokenize(doc) # Split into words
    
    # Remove numbers, but not words that contain numbers.
    doc = [token for token in doc if not token.isnumeric()]
    
    # Remove stopwords
    doc = [token for token in doc if not token in stop_words]
    
    # Remove words that are only one character.
    doc = [token for token in doc if len(token) > 1]
    
    # Lemmatize the documents
    doc = lemmatize(doc)
    
    return doc