from flask import Flask, jsonify, request
from scrapper.Scrapper import Scrapper

app = Flask(__name__)

@app.route('/')
def scrap():
  q = request.args.get('q')
  min_price = request.args.get('min_price')
  max_price = request.args.get('max_price')
  reverse = request.args.get('reverse')
  
  scrapper_instance = Scrapper()
  result = scrapper_instance.scrap(q, min_price, max_price, reverse)
  return jsonify(result)

if __name__ == '__main__':
  app.run()