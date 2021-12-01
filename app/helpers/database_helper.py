from app import db
from app.models.Product import Product

def add_or_update_product(product):
  product_exists = Product.query.filter_by(
    title=product['title'],
    description=product['description'],
    price=product['price'],
    url=product['url'],
    img_url=product['img_url'],
    rating=product['rating'],
    num_reviews=product['num_reviews']
    ).first()

  if(product_exists):
    print('Product already exists', product['title'])
    product_exists = Product(product)
    db.session.commit()
  
  else:
    prod = Product(product)
    db.session.add(prod)
    db.session.commit()