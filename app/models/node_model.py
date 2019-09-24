
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Text
import importlib

conn = importlib.import_module('lib.connection','.')

class NodeModel(conn.Base):
    __tablename__ = 'nodes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    type_ = Column('type',String(32))
    title = Column('title',String(32))
    width = Column('width',Integer)
    height = Column('height',Integer)
    x = Column('x',Integer)
    y = Column('y',Integer)
    color = Column('color',String(32))
    pins = Column('pins',Text)
    edges = Column('edges',Text)
    created_at = Column('created_at',Date)
    
    # resources = Column('resources',JSON)

    def __init__(self,type_=None,title=None,width=None,height=None,x=None,y=None,color=None,pins=None,edges=None,created_at=None):
        
        self.type_ = type_
        self.title = title
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.pins = pins
        self.edges = edges
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
        return session.query(NodeModel).all()
         