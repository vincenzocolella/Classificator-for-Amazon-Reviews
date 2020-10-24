#$ scrapy runspider webscraper_amazon.py -o reviews.csv
#$scrapy runspider webscraper_amazon.py -o reviews.json

# Importing Scrapy Library
import scrapy
 
# Creating a new class to implement Spide
class AmazonReviewsSpider(scrapy.Spider):
     
    # Spider name
    name = 'amazon_reviews'
     
    # Domain names to scrape
    allowed_domains = ['amazon.it']
     
    # Base URL for the World Tech Toys Elite Mini Orion Spy Drone
    myBaseUrl = "https://www.amazon.it/product-reviews/B06XFWPXYD/ref=cm_cr_arp_d_viewopt_sr?pageNumber="
    start_urls=[]
    
    # Creating list of urls to be scraped by appending page number a the end of base url
    pages = 100 #how many pages to scrape
    for i in range(1,pages): #proviamo a scrap abbastanza recensioni di tutti i tipi
        if i<=1/5*pages:
            start_urls.append(myBaseUrl+str(i)+"&filterByStar=one_star")
        elif i>=1/5*pages and i<2/5*pages:
            start_urls.append(myBaseUrl+str(i)+"&filterByStar=two_star")
        elif i>=2/5*pages and i<3/5*pages:
            start_urls.append(myBaseUrl+str(i)+"&filterByStar=three_star")
        elif i>3/5*pages:
            start_urls.append(myBaseUrl+str(i)+"&filterByStar=four_star")
        elif i>3/5*pages:
            start_urls.append(myBaseUrl+str(i)+"&filterByStar=five_star")
    
    # Defining a Scrapy parser
    def parse(self, response):
            #Get the Review List
            data = response.css('#cm_cr-review_list')
            
            #Get the Name
            name = data.css('.a-profile-name')
            
            #Get the Review Title
            title = data.css('.review-title')
            
            # Get the Ratings
            star_rating = data.css('.review-rating')
            
            # Get the users Comments
            description = data.css('.review-text')
            count = 0
             
            # combining the results
            for review in star_rating:
                
                yield{'Name':''.join(name[count].xpath(".//text()").extract()),
                      'Title':''.join(title[count].xpath(".//text()").extract()),
                      'Rating': ''.join(review.xpath('.//text()').extract()),
                      'Description': ''.join(description[count].xpath(".//text()").extract())
                     }
                count=count+1
                