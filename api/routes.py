from api import app
from .resources.users import user

app.register_blueprint(user)