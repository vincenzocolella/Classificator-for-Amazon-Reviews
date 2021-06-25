import pandas as pd
from monkeylearn import MonkeyLearn


# Si usa pandas per leggere il file appena creato
df = pd.read_csv('reviews.csv', encoding='utf-8')
 
# Si rimuovono le righe duplicate
df.drop_duplicates(inplace=True)

# Si uniscono le due colonne titolo e descrizione in una sola colonna 'full_content'
df['full_content'] = df['Title'] + '. ' + df['Description']

# il file viene modificato per contenere solo queste due colonne
df = df[['full_content', 'Rating']]

# si crea il file 'reviews_cleaned.csv', e ci si aggiungono tutte le righe nelle quali il rating è di 1,2,3,4 o 5 stelle.
# In questo modo si evita di inserire eventuali elementi anomali
df.to_csv('reviews_cleaned.csv', header=False, index=False, encoding='utf-8')
lista=[]
for index, row in df.iterrows():
    if row['Rating'] == '1,0 su 5 stelle':
        row['Rating'] = '1 su 5 stella'
    if row['Rating'] == '2,0 su 5 stelle':
        row['Rating'] = '2 su 5 stelle'
    if row['Rating'] == '3,0 su 5 stelle':
        row['Rating'] = '3 su 5 stelle'
    if row['Rating'] == '4,0 su 5 stelle':
        row['Rating'] = '4 su 5 stelle'
    if row['Rating'] == '5,0 su 5 stelle':
        row['Rating'] = '5 su 5 stelle'

#!!!FORSE STO IF POSSO RIMUOVERLO ...
    if row['Rating'] == '1 su 5 stella' or row['Rating'] == '2 su 5 stelle' or row['Rating'] == '3 su 5 stelle' or row['Rating'] == '4 su 5 stelle' or row['Rating'] == '5 su 5 stelle':
        lista.append({'text':row['full_content'],'tags':row['Rating']})

print('i dati sono : ' + str(len(lista)))


# Si danno finalmente i dati puliti in pasto al classificatore, dopo aver identificato sia l'account
# che l'id del modello 


ml = MonkeyLearn('b9cd35aea191606096c365fdabe323e4015ff8e2')
model_id = 'cl_7YpXVee3'
ml.classifiers.train(model_id, retry_if_throttled=True)
ml.classifiers.upload_data(model_id,lista)
print("Tutti i dati sono stati mandati in pasto al modello.")