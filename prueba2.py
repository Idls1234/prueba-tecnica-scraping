from playwright.async_api import async_playwright
from bs4 import BeautifulSoup
    
async def get_products_playwright(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=[
            "--no-sandbox",
            # "--disable-setuid-sandbox",
            # "--disable-dev-shm-usage",
            # "--disable-accelerated-2d-canvas",
            # "--disable-gpu",
            "--window-size=1920x1080"
        ])
        page = await browser.new_page()
    
        await page.goto(url)
        
        await page.wait_for_timeout(2000)
        
         # Esperar a que la página cargue completamente
        # await page.wait_for_load_state('networkidle')
        
        # Desplazamiento a la mitad de la página
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight / 4);')
        await page.wait_for_timeout(1000)
        
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight / 3);')
        await page.wait_for_timeout(1000)
        
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight / 2);')
        await page.wait_for_timeout(1000)
        
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight / 1);')
        await page.wait_for_timeout(1000)
        
        # Desplazamiento de la página hasta el final para cargar todos los elementos 
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight);')
        await page.wait_for_timeout(2000)
        # await page.evaluate('window.scrollTo(0, document.body.scrollHeight);')
        # await page.wait_for_timeout(2000)
        # Obtener el contenido HTML de la página
        content = await page.content()
        await browser.close()
        
         # Analizar el contenido HTML con BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        articles = soup.find_all('article')
        print("elementos: " + str(len(articles)))

        found_articles = []

        for article in articles:
            current_article = {}
            product_name = article.select_one('.vtex-product-summary-2-x-productBrand')
            
            if product_name is None:
                continue
            
            current_article['name'] = product_name.get_text(strip=True) if product_name else 'N/A'
            
            as_discount = article.select_one('.tiendasjumboqaio-jumbo-minicart-2-x-cencoListPriceWrapper')
            
            if as_discount is not None:
                price_element = as_discount.select_one('.tiendasjumboqaio-jumbo-minicart-2-x-price')
                if price_element:
                    price_text = price_element.get_text(strip=True).replace('\xa0', ' ')
                    current_article['price'] = price_text
                promo_price_element = article.select_one('.tiendasjumboqaio-jumbo-minicart-2-x-price')
                if promo_price_element:
                    promo_price_text = promo_price_element.get_text(strip=True).replace('\xa0', ' ')
                    current_article['promo_price'] = promo_price_text
            else:
                price_element = article.select_one('.tiendasjumboqaio-jumbo-minicart-2-x-price')
                if price_element:
                    price_text = price_element.get_text(strip=True).replace('\xa0', ' ')
                    current_article['price'] = price_text
                    # Set promo price to default value if promo price does not exist
                    current_article['promo_price'] = price_text

            found_articles.append(current_article)

        return found_articles
        
