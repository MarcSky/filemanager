import peewee
from config import PSSQL_NAME, PSSQL_HOST, PSSQL_PASSWORD, PSSQL_PORT, PSSQL_USER


def database_setting():
    return peewee.PostgresqlDatabase(
        PSSQL_NAME,
        host=PSSQL_HOST,
        port=PSSQL_PORT,
        user=PSSQL_USER,
        password=PSSQL_PASSWORD
    )
