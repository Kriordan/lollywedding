import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'lollywedding.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

DATABASE_PATH = os.path.join(basedir, DATABASE)
