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
  
  def scrap(self, q, minPrice=False, maxPrice=False, reverse=False):
    self.products = self.get_all_products()
    self.apply_filters( q, minPrice, maxPrice)

    self.sort_products_by_price(self.products, reverse=reverse)
    return self.products

  def apply_filters(self, q, minPrice, maxPrice):
    if q:
      filtered_by_description = self.filter_by_description(q)
      filtered_by_title = self.filter_by_title(q)
      filtered = filtered_by_description + filtered_by_title
      self.products = filtered
    
    if minPrice:
      self.products = self.filter_by_min_price(minPrice)
    if maxPrice:
      self.products = self.filter_by_min_price(minPrice)

  def filter_by_description(self, description):
    return [product for product in self.products if description.lower() in product["description"].lower()]
  
  def filter_by_title(self, title):
    return [product for product in self.products if title in product["title"]]
  
  def filter_by_min_price(self, minPrice):
    return [product for product in self.products if product["price"] >= minPrice]

  def get_all_products(self):
    container = self.driver.find_element(By.CSS_SELECTOR ,"div.col-md-9 > div.row")
    products = container.find_elements(By.CLASS_NAME, "col-sm-4")
    
    for product in products:
      title_element = product.find_element(By.CLASS_NAME, "title")
      product_url = title_element.get_attribute("href")
      title = title_element.text

      description_element = product.find_element(By.CLASS_NAME, "description")
      description = description_element.text

      price_element = product.find_element(By.CLASS_NAME, "price")
      price= self.__parse_price(price_element.text)

      image_element = product.find_element(By.TAG_NAME, "img")
      image_url = image_element.get_attribute("src")

      product_data = {
        "title": title,
        "price": price,
        "description": description,
        "url": product_url,
        "img_url": image_url,
      }

      self.products.append(product_data)

    return self.products

  def __parse_price(self, price_str):
    return float(price_str.replace("$", ""))

  def sort_products_by_price(self, list, reverse=False):
    return list.sort(reverse=reverse, key=lambda prod: prod["price"])



if __name__ == "__main__":
  scrapper = Scrapper()
  result = scrapper.scrap("lenovo")
  pprint.pprint(result)