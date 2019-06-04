
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Text
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import importlib

conn = importlib.import_module('lib.connection','.')


class LayerModel(conn.Base):
    __tablename__ = 'layers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    scene_id = Column('scene_id', Integer)
    name = Column('name', String(300))
    code = Column('code',Integer)
    tiles = Column('tiles',Text)
    background = Column('background',String(300))
    created_at = Column('created_at',Date)

    def __init__(self,scene_id=None,name=None,code=None,tiles=None,background=None,created_at=None):
        
        self.scene_id = scene_id
        self.name = name 
        self.code = code
        self.tiles = tiles
        self.background = background
        self.created_at = created_at
    
    def create(self):
        conn.Base.metadata.create_all(conn.engine)
        session = conn.Session()
        session.add(self)
        session.commit()
        session.close()

    def update(self,scene_id=None,name=None,code=None,tiles=None,background=None,created_at=None):
        
        conn.Base.metadata.create_all(conn.engine)
        session = conn.Session()
        for l in session.query(LayerModel).all():
            if l.scene_id == scene_id:
                session.query(LayerModel).update({LayerModel.tiles: tiles})
            else:
                self.scene_id = scene_id
                self.name = name
                self.code = code
                self.tiles = tiles
                self.background = background
                self.created_at = created_at
                self.create()
        session.commit()
        session.close()

    def readAll(self,sid):
        conn.Base.metadata.create_all(conn.engine)
        session = conn.Session()
        return session.query(LayerModel).filter(LayerModel.scene_id== sid).all()
    
    def read(self,sid):
        conn.Base.metadata.create_all(conn.engine)
        session = conn.Session()
        try:
            return session.query(LayerModel).filter(LayerModel.scene_id== sid)
            # print result
        except NoResultFound:
            print ('No result was found')
        
         