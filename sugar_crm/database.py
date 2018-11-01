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

# У нас только права на чтение, так что нет смысла заморачиваться с commit и
# rollback, потому используем опцию autocommit=True
session_factory_crm = sessionmaker(bind=engine_utm, autocommit=True)
Session_crm = scoped_session(session_factory_crm)
session_crm = Session_crm()