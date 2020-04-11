'''
hello_db 内の hello_table に fkubota アクセス権限を与えているという状況を想定。
テーブルへのアクセス権限がないのであれば、psql 側でユーザーにアクセス権限を与えなければならない。
'''

import pandas as pd
import psycopg2

# データベースの接続情報
connection_config = {
    'user': 'fkubota',
    'password': 'ilikemcu7137',
    'host': 'localhost',
    # 'port': 'ポート番号', # なくてもOK
    'database': 'hello_db'
}

# PostgreSQLに接続する
connection = psycopg2.connect(**connection_config)

# 方法1 cursor を使う
cur = connection.cursor()
cur.execute("SELECT * FROM hello_table;")

# 方法2 pandas を使う
df = pd.read_sql(sql='SELECT * FROM hello_table;', con=connection)
print(df)
