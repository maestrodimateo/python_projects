from flask import Flask
from itsdangerous import URLSafeTimedSerializer
import bcrypt
import yaml
import pymysql

pymysql.install_as_MySQLdb()

def parse_yaml_data():
    config_file = open('api/config.yaml')
    return yaml.load(config_file, Loader = yaml.FullLoader)

conf = parse_yaml_data()

def set_db_config(app):
    connection_uri = '{0}://{1}:{2}@{3}:{4}/{5}'.format(
        conf['db_connector'], conf['db_user'],
        conf['db_password'], conf['db_host'],
        conf['db_port'], conf['db_name']
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def set_mail_config(app):
    app.config['MAIL_SERVER']   = conf['mail_server']
    app.config['MAIL_USERNAME'] = conf['mail_username']
    app.config['MAIL_PASSWORD'] = conf['mail_password']
    app.config['MAIL_PORT']     = conf['mail_port']
    app.config['MAIL_USE_SSL']  = conf['mail_use_ssl']
    app.config['MAIL_USE_TLS']  = conf['mail_use_tls']

def init_app():
    app = Flask(__name__)
    set_mail_config(app)
    set_db_config(app)
    app.config['SECRET_KEY'] = conf['secret_key']
    return app

def serialise_token(email):
    serial = URLSafeTimedSerializer(conf['secret_key'])
    return serial.dumps(email)

def password_crypt(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def validate_fields(schemas, request, partial = False):
    user_fields = schemas.load(request.get_json(), partial = partial)
    return user_fields