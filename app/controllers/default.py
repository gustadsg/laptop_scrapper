from operator import or_
from flask import jsonify, request
from app import app, scrapper
from app.models.Product import Product
from app.helpers.database_helper import add_or_update_product
from datetime import datetime
import math

@app.route('/')
def scrap():
  q = request.args.get('q') if request.args.get('q') != None else ''
  min_price = request.args.get('min_price') if request.args.get('min_price') != None else 0
  max_price = request.args.get('max_price') if request.args.get('min_price') != None else 9999999
  reverse = request.args.get('reverse') if request.args.get('reverse') != None else False
  update_tolerance = request.args.get('update_tolerance') if request.args.get('update_tolerance') != None else False

  # apply all filters in database
  result = Product.query.filter(Product.price >= min_price).filter(Product.price <= min_price).filter(or_(Product.title.ilike(f"%{q}%"), Product.description.ilike(f"%{q}%"))).all()

  if result and update_tolerance != None:
    last_updated = result[0].updated_at
    difference = datetime.utcnow() - last_updated

    result = list(map(lambda prod: prod.to_dict(), result))

    if difference.total_seconds() < float(update_tolerance):
      scrapper.clear()
      return jsonify(result)


  result = scrapper.scrap(q, min_price, max_price, bool(reverse))

  for item in result:
    item.update({'updated_at': datetime.now()})
    add_or_update_product(item)

  scrapper.clear()
  return jsonify(result)

if __name__ == '__main__':
  app.run()