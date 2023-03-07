from datetime import datetime

from sqlalchemy import or_, and_

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
        return self.session.query(User).filter(User.EMAIL == EMAIL).first()

    def find_by_email_and_username(self, USERNAME, PASSWORD):
        # return self.session.query(User).filter((or_(User.EMAIL == USERNAME), (User.USERNAME == USERNAME)),
        #                                        (User.PASSWORD == PASSWORD)).first()

        return self.session.query(User).filter((or_((User.EMAIL == USERNAME), (User.USERNAME == USERNAME))),
                                               (User.PASSWORD == PASSWORD)).first()
