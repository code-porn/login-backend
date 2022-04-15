import os
DB_PATH=os.environ.get('DB','')
sql_local_base='sqlite:///' +DB_PATH+'/accendero_user_auth.db'
class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = sql_local_base


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' +DB_PATH  + '/accendero_user_auth_test.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = sql_local_base