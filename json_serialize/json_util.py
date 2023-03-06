from database.db_config import User


class UserJson:
    @classmethod
    def get_dict(cls, obj, exclude=[], include=[]):
        columns = [c.name for c in User.__table__.columns if c.name not in exclude]
        json = dict([(c, getattr(obj, c)) for c in columns])
        return json

    @classmethod
    def get_list(cls, objs, exclude=[], include=[]):
        jsons = [cls.get_dict(obj, exclude, include) for obj in objs]
        return jsons
