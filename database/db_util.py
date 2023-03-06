import re

import inflect
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import generate_relationship
from sqlalchemy.orm import interfaces
from sqlalchemy.pool import NullPool


def get_mysql_connection(host, user, password, dbname):
    """

    :param host:
    :param user:
    :param password:
    :param dbname:
    :return:
    """

    db = create_engine(
        'mysql+pymysql://{user}:{password}@{host}/{db}'.format(user=user, password=password,
                                                               host=host,
                                                               db=dbname),
        poolclass=NullPool)
    return db


def camelize_classname(base, tablename, table):
    """Produce a 'camelized' class name, e.g. """
    "'words_and_underscores' -> 'WordsAndUnderscores'"
    return str(tablename[0].upper() + \
               re.sub(r'_([a-z])', lambda m: m.group(1).upper(), tablename[1:]))


_pluralizer = inflect.engine()


def _gen_relationship(base, direction, return_fn,
                      attrname, local_cls, referred_cls, **kw):
    if direction is interfaces.ONETOMANY:
        kw['cascade'] = 'all, delete-orphan'
        kw['passive_deletes'] = True
    return generate_relationship(base, direction, return_fn,
                                 attrname, local_cls, referred_cls, **kw)
