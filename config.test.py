from os import getcwd

PSSQL_NAME = ''
PSSQL_USER = ''
PSSQL_HOST = ''
PSSQL_PORT = ''
PSSQL_PASSWORD = ''

SECRET_KEY = 'flask_secret_key'
FILES_FOLDER = '%s/files' % getcwd()

#link life time is 1 hours
LINK_LIFE_TIME = 60 * 60
ALLOWED_EXTENSIONS = ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']
