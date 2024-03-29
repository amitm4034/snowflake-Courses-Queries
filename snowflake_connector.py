import snowflake.connector as sf
import pandas as pd
import getpass

password = getpass.getpass("Enter your snowflake password: ")

# make changes as per your credentials
user='CODEKONVERGEAI'
account=''
database='DEMO_DB'
warehouse='COMPUTE_WH'
schema='PUBLIC'
role='ACCOUNTADMIN'

conn = sf.connect(user = user,
           password = password,
           account = account,
    )

def run_query(connection,query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
  
sql = f'use warehouse {warehouse}'
run_query(conn, sql)
    
try:
    warehouse_sql = 'use warehouse {}'.format(warehouse)
    run_query(conn, warehouse_sql)
    
    try:
        sql = 'alter warehouse {} resume'.format(warehouse)
        run_query(conn, sql)
    except:
        pass
    
    sql = 'use database {}'.format(database)
    run_query(conn, sql)
    
    sql = 'use role {}'.format(role)
    run_query(conn, sql)
    
    sql = f'use schema {schema}'
    run_query(conn, sql)

except Exception as e:
    print(e)
    

sql = 'select * from healthcare limit 20'
df = pd.read_sql(sql, conn)

df.tail(10)