'''
事前にpostgreSQLでpandas_db 内に pandas_table を作成し、fkubotaに権限を与えた。
psycopg2 だと上書きできないらしい。
'''

import pandas as pd
# import psycopg2
from sqlalchemy import create_engine


# データベースの接続情報
connection_config = {
    'user': 'fkubota',
    'password': 'ilikemcu7137',
    'host': 'localhost',
    'port': '5432',
    'database': 'pandas_db'
}

# PostgreSQLに接続する
engine = create_engine('postgresql://{user}:{password}@{host}:{port}/{database}'.format(**connection_config))

# pandas
df = pd.read_sql(sql='SELECT * FROM pandas_table;', con=engine)
name = 'jiro'
age = 9
df_2 = pd.DataFrame([[name, age]], columns=['name', 'age'])
df_concat = pd.concat([df, df_2])
print(df_concat)

df.to_sql('pandas_table', engine, if_exists='replace')
