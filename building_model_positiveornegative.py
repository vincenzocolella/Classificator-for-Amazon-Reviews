import pandas as pd
from monkeylearn import MonkeyLearn


# Si usa pandas per leggere il file appena creato
df = pd.read_csv('model_sd_card.csv', encoding='utf-8')
 
# Si rimuovono le righe duplicate
df.drop_duplicates(inplace=True)

df = df[['Text', 'Tag']]
# si crea il file 'reviews_cleaned.csv', e ci si aggiungono tutte le righe nelle quali il rating è di 1,2,3,4 o 5 stelle.
# In questo modo si evita di inserire eventuali elementi anomali
df.to_csv('new_data_cleaned.csv', header=False, index=False, encoding='utf-8')
lista=[]
for index, row in df.iterrows():
    if row['Tag'] == '1 su 5 stella' or row['Tag'] == '2 su 5 stelle' or row['Tag'] == '3 su 5 stelle':
        row['Tag'] = 'Negative'
    if row['Tag'] == '4 su 5 stelle' or row['Tag'] == '5 su 5 stelle':
        row['Tag'] = 'Positive'

#!!!FORSE STO IF POSSO RIMUOVERLO ...
    if row['Tag'] == 'Positive' or row['Tag'] == 'Negative':
        lista.append({'text':row['Text'],'tags':row['Tag']})

print('i dati sono : ' + str(len(lista)))

