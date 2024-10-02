import requests
from bs4 import BeautifulSoup

def get_products(url):
    response = requests.get(url)

    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles = soup.find_all('article')
          
        found_articles = []
        
        for article in articles:
            
            current_article = {}
            product_name = article.find(class_='vtex-product-summary-2-x-productBrand')  
            current_article['name'] = product_name.get_text(strip=True).replace('\xa0', ' ')
            
            as_discount = article.find(class_='tiendasjumboqaio-jumbo-minicart-2-x-cencoListPriceWrapper')
            # print("as Discount: " + str(as_discount))
            
            if as_discount is not None:
                
                price = as_discount.find(class_='tiendasjumboqaio-jumbo-minicart-2-x-price')            
                current_article['price'] = price.get_text(strip=True).replace('\xa0', ' ')
                promo_price = article.find(class_='tiendasjumboqaio-jumbo-minicart-2-x-price') 
                current_article['promo_price'] = promo_price.get_text(strip=True).replace('\xa0', ' ')
            
            else:
                price = article.find(class_='tiendasjumboqaio-jumbo-minicart-2-x-price')
                current_article['price'] = price.get_text(strip=True).replace('\xa0', ' ')
                #set promo price to default value if promo price not exists
                current_article['promo_price'] = price.get_text(strip=True).replace('\xa0', ' ')
            
            # print(current_article)
            # print("--------------------")
            found_articles.append(current_article)
        print(found_articles)
        
        return found_articles
    else:
        print(f"Error: {response.status_code}")