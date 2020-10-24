import pandas as pd
# We use the Pandas library to read the contents of the scraped data
# obtained by Scrapy
df = pd.read_csv('reviews.csv', encoding='utf-8')
 
# Now we remove duplicate rows (reviews)
df.drop_duplicates(inplace=True)

# We want to use both the title and content of the review to
# classify, so we merge them both into a new column.
df['full_content'] = df['Title'] + '. ' + df['Description']

df = df[['full_content', 'Rating']]

df.to_csv('reviews_cleaned.csv', header=False, index=False, encoding='utf-8')