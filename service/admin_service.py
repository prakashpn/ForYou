from datetime import datetime

from flask import jsonify

from database.db_config import Admin
from repository.admin_repository import AdminRepository
from util.random_string import randomString


class AdminService():
    def __init__(self, session):
        self.session = session

    def insert_admin(self, data):
        checkEmail = AdminRepository(self.session).find_by_email(data.get("EMAIL"))
        if checkEmail is None:
            admin = Admin()
            admin.FIRST_NAME = data.get("FIRST_NAME")
            admin.LAST_NAME = data.get("LAST_NAME")
            admin.EMAIL = data.get("EMAIL")
            admin.USERNAME = randomString(7)
            admin.PASSWORD = randomString(10)
            AdminRepository(self.session).insert_admin(admin)
            # return admin
            return jsonify({"message": "Admin inserted successfully"})
        if checkEmail is not None:
            return jsonify({"message": "AdminEmail already Present"})

    def update_admin(self, data):
        admin = AdminRepository(self.session).find_by_email(data.get("EMAIL"))
        if admin is not None:
            admin.FIRST_NAME = data.get("FIRST_NAME")
            admin.LAST_NAME = data.get("LAST_NAME")
            admin.GEN_DATE = datetime.now()
            return jsonify({"message": "Admin updated successfully"})
        else:
            return jsonify(message="Email is not present")

    def delete_admin(self, ADMIN_ID):
        # admin.STATUS = "N"
        admin = AdminRepository(self.session).find_by_admin_id(ADMIN_ID)
        self.session.delete(admin)
