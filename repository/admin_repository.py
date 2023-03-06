from datetime import datetime

from database.db_config import Admin


class AdminRepository():

    def __init__(self, session):
        self.session = session

    def find_all(self):
        """
        find all data from database from Admin table
        :return: list of Admin
        :rtype: Admin (sqlalchemy automap object)
        """
        query = self.session.query(Admin).all()
        return query

    def insert_admin(self, admin):
        admin.GEN_DATE = datetime.now()
        admin.STATUS = "Y"
        self.session.add(admin)
        self.session.flush()
        self.session.refresh(admin)
        return admin

    def find_by_email(self, EMAIL):
        return self.session.query(Admin).filter(Admin.EMAIL == EMAIL).first()

    def find_by_admin_id(self, ADMIN_ID):
        df = self.session.query(Admin).get(ADMIN_ID)

        return df
