
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Text
import importlib

conn = importlib.import_module('lib.connection','.')

class ObjectModel(conn.Base):
    __tablename__ = 'objects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(32))
    type_ = Column('type',String(32))
    pid = Column('pid',Integer)
    layers = Column('la',Text)
    created_at = Column('created_at',Date)
    
    # resources = Column('resources',JSON)

    def __init__(self,name=None,type_=None,pid=None,layers=None,created_at=None):
        
        self.name = name 
        self.type_ = type_
        self.pid = pid
        self.layers = layers
        self.created_at = created_at
    
    def create(self):
        conn.Base.metadata.create_all(conn.engine)
        session = conn.Session()
        session.add(self)
        session.commit()
        session.close()

    def readAll(self):
        conn.Base.metadata.create_all(conn.engine)
        session = conn.Session()
        return session.query(ObjectModel).all()
         