from monkeylearn import MonkeyLearn

#si identifica l'id dell'account e l'id del modello
ml = MonkeyLearn('b9cd35aea191606096c365fdabe323e4015ff8e2')
model_id = 'cl_7YpXVee3'

#nella lista "data" si inseriscono gli elementi da analizzare 
data = ["",""]

result = ml.classifiers.classify(model_id, data)
print(result.body)
