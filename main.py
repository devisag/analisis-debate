import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

# Texto del debate (reemplaza con tu propio texto)
texto_debate = "Aquí va el texto completo del debate..."

# Tokenización
tokens = word_tokenize(texto_debate.lower())  # Convierte a minúsculas

# Eliminación de stopwords
stop_words = set(stopwords.words('spanish'))  # Puedes cambiar 'spanish' por otro idioma
filtered_tokens = [word for word in tokens if word not in stop_words]

# Stemming (opcional)
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

# Conteo de palabras
word_counts = Counter(stemmed_tokens)  # Utiliza stemmed_tokens si aplicaste stemming

# Palabras más mencionadas (por ejemplo, las 10 más mencionadas)
top_words = word_counts.most_common(10)

for word, count in top_words:
    print(f"{word}: {count}")