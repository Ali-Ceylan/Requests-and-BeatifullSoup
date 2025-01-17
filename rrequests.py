import requests
from bs4 import BeautifulSoup
from time import sleep
def get_price(url, selectors):
    """
    Extracts the price from a given URL using a list of CSS selectors.

    Args:
        url: The URL of the webpage.
        selectors: A list of CSS selectors for the price element.

    Returns:
        The price as a string, or an error message if fetching fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        for selector in selectors:
            price_element = soup.select_one(selector)
            if price_element and price_element.text.strip():
                return price_element.text.strip()

        return "Fiyat bilgisi bulunamadı"

    except requests.exceptions.RequestException as e:
        print(f"Hata: {url} fiyatı alınamadı: {e}")
        return "Fiyat alınamadı"
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
        return "Beklenmeyen bir hata"

def main():
    url = "https://www.google.com/finance/quote/USD-TRY"
    url2="https://www.google.com/finance/quote/EUR-TRY"
    selectors = [
        ".YMlKec.fxKbKc", # Google Finance Selector
    ]

    usd_try_price = get_price(url, selectors)
    usd_try_price2 = get_price(url2, selectors)
    print(f"Güncel USD/TRY Fiyatı: {usd_try_price}")
    print(f"Güncel EURO/TRY Fiyatı: {usd_try_price2}")

if __name__ == "__main__":
   while True:
        
        main()
        sleep(3)