from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail
from api.utils import init_app

# Initialiser l'application
app = init_app()

# Initialiser la base de données
db = SQLAlchemy(app)

# Initialiser CORS
CORS(app)

# Initialiser le mail
mail = Mail(app)

# routes
import api.routes

# models
import api.models