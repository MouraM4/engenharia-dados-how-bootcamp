from sqlalchemy import create_engine
import pandas as pd


engine = create_engine(
    'postgresql+psycopg2://root:1234@localhost/test_db'
)


query = '''
    select * from vw_artist;
'''

df = pd.read_sql_query(query, engine)
