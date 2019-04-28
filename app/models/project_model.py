
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Text
import importlib

conn = importlib.import_module('lib.connection','.')

class ProjectModel(conn.Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column('project_name', String(32))
    oriantation = Column('oriantation',String(32))
    size = Column('size',String(32))
    created_at = Column('created_at',Date)
    project_dir = Column('project_dir',String(32))
    online_status = Column('online_status',String(32))
    scenes = Column('scenes',Text)
    event_sheets = Column('event_sheets',Text)
    scripts = Column('scripts',Text)

    # resources = Column('resources',JSON)

    def __init__(self,name,oriantation,size,created_at,dir):
        self.project_name = name 
        self.oriantation = oriantation
        self.size = size
        self.created_at = created_at
        self.project_dir = dir
        self.online_status = 'up'
    
    def create(self):
        conn.Base.metadata.create_all(conn.engine)
        session = conn.Session()
        session.add(self)
        session.commit()
        session.close()

