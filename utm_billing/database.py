from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker, scoped_session

from audit_sugar_utm.settings_private import config_sqlalchemy_utm


engine_utm = engine_from_config(
    config_sqlalchemy_utm,
    prefix='db.',
    echo=True,
    pool_recycle=600,
    pool_pre_ping=True
)

session_factory_utm = sessionmaker(bind=engine_utm)
Session_utm = scoped_session(session_factory_utm)
session_utm = Session_utm()
