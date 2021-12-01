from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config.from_envvar("DOTENV_FILE")