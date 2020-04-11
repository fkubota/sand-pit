import psycopg2
import pandas as pd

connector = psycopg2.connect(
    host='localhost',
    port=5432,
    # port=5435,
    # database='apr_db',
    dbname='apr_db',
    user='apr_user',
    password='ilikemcu7137',
)
cursor = connector.cursor()
# print(dir(connector))
result = pd.read_sql("SELECT * FROM apr_table", connector)
print(result)
