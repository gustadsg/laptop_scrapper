from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint

WEBSITE_URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"

class Scrapper:
  
  def __init__(self):
    self.setup_webdriver()    
    self.products = []

  def setup_webdriver(self):
    options = webdriver.FirefoxOptions()
    options.headless = True
    self.driver = webdriver.Firefox(options=options)
    self.driver.get(WEBSITE_URL)
  
  def scrap(self, q=False, min_price=False, max_price=False, reverse=False):
    self.products = self.get_all_products()
    self.apply_filters( q, min_price, max_price)
    if reverse==None: reverse = False
    self.sort_products_by_price(self.products, reverse=reverse)
    return self.products

  def apply_filters(self, q, min_price, max_price):
    if q:
      self.products = self.filter_by_text(q)
    
    if min_price:
      self.products = self.filter_by_min_price(float(min_price))
    if max_price:
      self.products = self.filter_by_max_price(float(max_price))

  def filter_by_text(self, q):
    return [product for product in self.products if q.lower() in product["description"].lower() or q.lower() in product["title"].lower()]
  
  def filter_by_min_price(self, min_price):
    return [product for product in self.products if product["price"] >= min_price]

  def filter_by_max_price(self, min_price):
    return [product for product in self.products if product["price"] <= min_price]

  def get_all_products(self):
    container = self.driver.find_element(By.CSS_SELECTOR ,"div.col-md-9 > div.row")
    products = container.find_elements(By.CLASS_NAME, "col-sm-4")
    
    for product in products:
      title_element = product.find_element(By.CLASS_NAME, "title")
      product_url = title_element.get_attribute("href")
      title = title_element.get_attribute("title")

      description_element = product.find_element(By.CLASS_NAME, "description")
      description = description_element.text

      price_element = product.find_element(By.CLASS_NAME, "price")
      price= self.__parse_price(price_element.text)

      image_element = product.find_element(By.TAG_NAME, "img")
      img_url = image_element.get_attribute("src")

      ratings_element = product.find_element(By.CLASS_NAME, "ratings")
      num_reviews = ratings_element.find_element(By.CLASS_NAME, "pull-right").text
      rating = ratings_element.find_elements(By.TAG_NAME, "p")[1].get_attribute("data-rating")

      product_data = {
        "title": title,
        "price": price, 
        "description": description,
        "url": product_url,
        "img_url": img_url,
        "rating": rating,
        "num_reviews": num_reviews 
      }

      self.products.append(product_data)

    return self.products

  def __parse_price(self, price_str):
    return float(price_str.replace("$", ""))

  def sort_products_by_price(self, list, reverse=False):
    return list.sort(reverse=reverse, key=lambda prod: prod["price"])

  def clear(self):
    self.products = []
    
if __name__ == "__main__":
  scrapper = Scrapper()
  result = scrapper.scrap()
  pprint.pprint(result)