#$ scrapy runspider webscraper_amazon.py -o reviews.csv

#$scrapy runspider webscraper_amazon.py -s USER_AGENT="Mozilla/5.0 (Windows NT 6.1; WOW64)/AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36" /-s ROBOTSTXT_OBEY=False

# Importazione della libreria scrapy
import scrapy
 
# Creazione della classe per l'implementazione dello spider
class AmazonReviewsSpider(scrapy.Spider):
     
    # nome Spider
    name = 'amazon_reviews'
     
    # Domain names to scrape
    allowed_domains = ['amazon.it']
     
    # Base URL - link alla SD Card 
    myBaseUrl = "https://www.amazon.it/product-reviews/B06XFS5657/ref=cm_cr_arp_d_viewopt_sr?pageNumber="
    start_urls=[]
    

    # Si crea una lista di urls aggiungendo il suffisso 'pagina numero ...' al link base
    pagine = 500 #how many pages to scrape
    for i in range(1,pagine):
        start_urls.append(myBaseUrl+str(i)+'&filterByStar=critical')
    
    # Definizione del parser Scrapy
    def parse(self, response):

            # Estrazione della lista di recensioni
            data = response.css('#cm_cr-review_list')
            
            # Estrazione del titolo della recensione
            title = data.css('.review-title')
            
            # Estrazione delle stelle (tag)
            star_rating = data.css('.review-rating')
            
            # Estrazione del testo della recensione
            description = data.css('.review-text')

            count=0

            # unione dei risulati
            for review in star_rating:
                
                    yield{
                      'Title':''.join(title[count].xpath(".//text()").extract()),
                      'Rating': ''.join(review.xpath('.//text()').extract()),
                      'Description': ''.join(description[count].xpath(".//text()").extract())
                     }
                    count= count+1
                