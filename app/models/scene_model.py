
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Text
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import importlib

conn = importlib.import_module('lib.connection','.')



class SceneModel(conn.Base):
    __tablename__ = 'scenes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(32))
    type_ = Column('type',String(32))
    pid = Column('pid',Integer)
    layers = Column('layers',Text)
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
        return session.query(SceneModel).all()
    
    def read(self,pid):
        conn.Base.metadata.create_all(conn.engine)
        session = conn.Session()
        try:
            return session.query(SceneModel).filter(SceneModel.pid== pid).one()
            # print result
        except NoResultFound:
            print ('No result was found')
        except MultipleResultsFound:
            print ('Multiple results were found')
         