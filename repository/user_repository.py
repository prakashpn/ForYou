from datetime import datetime

from database.db_config import User


class UserRepository():

    def __init__(self, session):
        self.session = session

    def find_all(self):
        """
        find all data from database from User table
        :return: list of User
        :rtype: User (sqlalchemy automap object)
        """
        query = self.session.query(User).all()
        return query

    def insert_user(self, user):
        user.GEN_DATE = datetime.now()
        user.STATUS = "Y"
        self.session.add(user)
        self.session.flush()
        self.session.refresh(user)
        return user

    def find_by_email(self, EMAIL):
        return self.session.query(User).filter(User.USER_EMAIL == EMAIL).first()

    def find_by_user_id(self, USER_ID):
        df = self.session.query(User).get(USER_ID)

        return df
