from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

from base_util import config
from database.db_util import get_mysql_connection, camelize_classname, _gen_relationship

MY_DB = "MY_DB"

host, user, password, dbname = config.get(MY_DB, 'host'), \
    config.get(MY_DB, 'user'), \
    config.get(MY_DB, 'password'), \
    config.get(MY_DB, 'db')

Base = automap_base()
engine = get_mysql_connection(host, user, password, dbname)
print(engine)

# reflect the tables
Base.prepare(engine, reflect=True, classname_for_table=camelize_classname, generate_relationship=_gen_relationship)

for c in Base.classes:
    print(c)

User = Base.classes.User
Admin = Base.classes.Admin

Session = sessionmaker()


def create_session():
    con = engine.connect()
    con.execute("SET FOREIGN_KEY_CHECKS = 0;")
    session = Session(bind=con)
    return session, con


def close_session(session, con):
    session.close()
    con.close()
    engine.dispose()
    return ""
