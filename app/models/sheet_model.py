
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Text
import importlib

conn = importlib.import_module('lib.connection','.')

class ObjectModel(conn.Base):
    __tablename__ = 'objects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(32))
    type_ = Column('type',String(32))
    pid = Column('cat_id',Integer)
    layers = Column('resources',Text)
    created_at = Column('created_at',Date)
    
    # resources = Column('resources',JSON)

    def __init__(self,name=None,type_=None,cat_id=None,resources=None,status=None,frames=None,frame_width=None,frame_height=None,parent=None,created_at=None):
        
        self.name = name 
        self.type_ = type_
        self.cat_id = cat_id
        self.resources = resources
        self.status = status
        self.frames = frames
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.parent = parent
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
         