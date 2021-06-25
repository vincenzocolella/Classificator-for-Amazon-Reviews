#create model (usare solo una volta)
from monkeylearn import MonkeyLearn

#identificazione del proprio account
ml = MonkeyLearn('b9cd35aea191606096c365fdabe323e4015ff8e2')

#creazione del modello con i rispettivi parametri
response = ml.classifiers.create('model_for_reviews','modello per la classificazione di recensioni amazon in base al loro punteggio',
                                    algorithm='svm', language='it', max_features=10000, ngram_range=(1, 3), use_stemming=True,
                                   preprocess_numbers=True, preprocess_social_media=False,
                                   normalize_weights=True, stopwords=True, whitelist=None,
                                   retry_if_throttled=True)

#aggiunta dei tag per il modello
model_id = 'cl_7YpXVee3'
response = ml.classifiers.tags.create(model_id, '1 su 5 stella')
response = ml.classifiers.tags.create(model_id, '2 su 5 stelle')
response = ml.classifiers.tags.create(model_id, '3 su 5 stelle')
response = ml.classifiers.tags.create(model_id, '4 su 5 stelle')
response = ml.classifiers.tags.create(model_id, '5 su 5 stelle')