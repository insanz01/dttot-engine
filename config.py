import os

host = os.environ.get('APP_HOST', 'localhost')
port = os.environ.get('APP_PORT', 5000)

db_name = os.environ.get('DB_NAME', 'dttot-engine')
db_user = os.environ.get('DB_USER', 'root')
db_password = os.environ.get('DB_PASSWORD', 'password')


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'XXXXX'  # todo: should be changed for production
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@database:5432/{}".format(db_user, db_password, db_name)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECURITY_URL_PREFIX = ""
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "YYYYYYY"  # todo: should be changed for production

    REDIS_URL = "redis://:@localhost:6379/0"


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


configs = {"dev": DevelopmentConfig, "prod": ProductionConfig}
config = configs[os.environ.get('ENV', 'dev')]
