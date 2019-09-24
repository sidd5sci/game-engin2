
from sqlalchemy import Column, String, Integer, Date, ForeignKey, Text
import importlib

conn = importlib.import_module('lib.connection','.')

class ProjectModel(conn.Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    project_name = Column('project_name', String(300))
    oriantation = Column('oriantation',String(300))
    size = Column('size',String(50))
    project_dir = Column('project_dir',String(300))
    online_status = Column('online_status',String(300))
    scenes = Column('scenes',Text)
    event_sheets = Column('event_sheets',Text)
    scripts = Column('scripts',Text)
    created_at = Column('created_at',Date)
    # resources = Column('resources',JSON)

    def __init__(self,name=None,oriantation=None,size=None,script=None,scenes=None,event_sheet=None,created_at=None,dir=None):
        self.project_name = name 
        self.oriantation = oriantation
        self.size = size
        self.scenes = scenes
        self.scripts = script
        self.event_sheets = event_sheet
        self.project_dir = dir
        self.online_status = 'up'
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
        return session.query(ProjectModel).all()
