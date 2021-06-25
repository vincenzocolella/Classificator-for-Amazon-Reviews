
#documents = [{"id": "1","language": "it", "text": "Medio"},]
import pandas as pd
from monkeylearn import MonkeyLearn
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
key = "0ab1471850784702a8aede4711219fe6"
endpoint = "https://sentiment-recensioni.cognitiveservices.azure.com/"

#autenticazione al client di Microsoft con le chiavi forniteci dalla piattaforma
def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client

client = authenticate_client()

#algoritmo che prende in input il client e un testo da analizzare, e restituisce il sentimento secondo Azure
def sentiment_analysis_azure(client,documents):

    sentiment_azure = ""
    response = client.analyze_sentiment(documents=documents)[0]

    return response.sentiment

#algoritmo che prende in input il client e un testo da analizzare, e restituisce il sentimento secondo MonkeyLearn
def sentiment_analysis_monkeylearn(documents):

    ml = MonkeyLearn('b9cd35aea191606096c365fdabe323e4015ff8e2')
    model_id = 'cl_BBQSQw6i'
    result = ml.classifiers.classify(model_id, [documents[0].get("text")])

    sentiment_monkeylearn = result.body[0].get("classifications")[0].get("tag_name")
    return sentiment_monkeylearn


#si paragonano i risultati ottenuti, incrementando i due contatori in base all'uguaglianza tra i sentiment restituiti
stesso_sentiment = 0
diverso_sentiment = 0

df = pd.read_csv('new_data_cleaned.csv', encoding='utf-8')
for index, row in df.iterrows():
    text = row['Text']

    x = sentiment_analysis_azure(client,[{"id": "1", "language": "it", "text": text}])
    y = sentiment_analysis_monkeylearn([{"id": "1", "language": "it", "text": text}])

    #se il sentiment restituito è equivalente per i due algoritmi
    if x == y:
        stesso_sentiment=stesso_sentiment+1

    #se il sentiment restituito è diverso
    else:
        diverso_sentiment=diverso_sentiment+1

print(stesso_sentiment)
print(diverso_sentiment)
