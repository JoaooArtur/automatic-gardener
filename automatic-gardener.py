import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

pd.reset_option('display.max_colwidth')
pd.reset_option('display.max_rows')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-extensions')

wd = webdriver.Chrome(options=chrome_options)

url = "https://apps.apple.com/nz/app/trade-me-property-shop-sell/id392567559?see-all=reviews"

wd.get(url)

avaliacoes = []

reviews = wd.find_elements(By.CLASS_NAME, 'we-customer-review')
for review in reviews:
    avaliacao = review.find_element(By.CLASS_NAME, 'we-clamp')
    avaliacoes.append(avaliacao.find_element(By.TAG_NAME, 'p').text)

wd.quit()

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocessamento(texto):
    tokens = word_tokenize(texto.lower())
    return ' '.join([token for token in tokens if token not in stop_words and token.isalpha()])

avaliacoes_preprocessadas = [preprocessamento(avaliacao) for avaliacao in avaliacoes]

palavras_negativas = set(['annoying', 'problem', 'fix', 'fixes', 'frustrating', 'bad','hate'])
palavras_positivas = set(['love', 'great','good','liked'])

def extrair_features(avaliacao):
    palavras = word_tokenize(avaliacao.lower())
    features = {}
    for palavra in palavras:
        features[palavra] = True
    return features

dados = [(extrair_features(preprocessamento(avaliacao)), categorizar_cluster(avaliacao)) for avaliacao in avaliacoes]

tamanho_treinamento = int(len(dados) * 0.50)
dados_treinamento = dados[:tamanho_treinamento]
dados_teste = dados[tamanho_treinamento:]

classificador = nltk.NaiveBayesClassifier.train(dados_treinamento)

df = pd.DataFrame({'Texto': avaliacoes, 'Categoria': [classificador.classify(extrair_features(preprocessamento(avaliacao))) for avaliacao in avaliacoes]})

print("Acurácia do classificador:",nltk.classify.accuracy(classificador, dados))
print(df)