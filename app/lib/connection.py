# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# engine = create_engine('sqllite://usr:pass@localhost:5432/sqlalchemy')
# engine = create_engine('oracel://usr:pass@localhost:5432/sqlalchemy')
# engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
engine = create_engine('mysql+pymysql://root:@localhost:3306/pytrack',pool_recycle=3600)

Session = sessionmaker(bind=engine)
 
Base = declarative_base()

connection = engine.connect()
connection = connection.execution_options(
    isolation_level="READ COMMITTED"
)

print ("""\n\n 
    ===========================================
    Database Connection successful 
    ===========================================
    \n\n""")