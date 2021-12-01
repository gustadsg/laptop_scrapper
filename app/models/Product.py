from app import db

class Product(db.Model):
  __tablename__ = 'products'

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(255))
  description = db.Column(db.Text(255))
  price = db.Column(db.Float)
  url = db.Column(db.String(255))
  img_url = db.Column(db.String(255))
  rating = db.Column(db.Float)
  num_reviews = db.Column(db.Integer)
  updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

  def __init__(self, product):
    self.title = product['title']
    self.description = product['description']
    self.price = product['price']
    self.url = product['url']
    self.img_url = product['img_url']
    self.rating = product['rating']
    self.num_reviews = product['num_reviews']

  def to_dict(self):
    return {
      'title': self.title,
      'description': self.description,
      'price': self.price,
      'url': self.url,
      'img_url': self.img_url,
      'rating': self.rating,
      'num_reviews': self.num_reviews
    }

  def __repr__(self):
    return '<Product %r>' % self.title