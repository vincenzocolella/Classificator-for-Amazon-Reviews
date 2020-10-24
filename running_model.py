from monkeylearn import MonkeyLearn


ml = MonkeyLearn('9392f02bd5fe5580760e747c435a3e312cdfba90')
#data = input('Cosa analizzare:')
data = ["Pessimo dispositivo consegna veloce."] #qui le cose da analizzare
model_id = 'cl_KmXWgjBD'
result = ml.classifiers.classify(model_id, data)
print(result.body)
