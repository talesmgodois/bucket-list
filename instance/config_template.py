# /instance/config.py

import os


class Config(object):
    """Parent configuration class."""
    DEBUG = False
    CSRF_ENABLED = True
    SECRET = os.getenv('SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')


class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True


class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""

    TESTING = True
    SQLALCHEMY_DATABASE_URI = DatabaseConfig.get_dev_config().get_uri()
    DEBUG = True


class StagingConfig(Config):
    """Configurations for Staging."""
    DEBUG = True


class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False


class DatabaseConfig:
    host = None
    port = None
    name = None
    password = None

    def __init__(self, host, port, name, user, password):
        self.host = host
        self.port = port
        self.name = name
        self.user = user
        self.password = password

    def get_uri(self):
        return "postgres://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"

    @staticmethod
    def get_dev_config():
        return DatabaseConfig(
            "hhh",
            "ppp",
            "nnn"
            "uuu",
            "ppp"
        )



app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
}
