from flask import Flask, jsonify
from scrapper.Scrapper import Scrapper

app = Flask(__name__)

@app.route('/')
def scrap():
  scrapper_instance = Scrapper()
  result = scrapper_instance.scrap()
  return jsonify(result)

if __name__ == '__main__':
  app.run()