from datetime import datetime

from flask import jsonify

from database.db_config import User
from repository.user_repository import UserRepository
from util.random_string import randomString


class UserService():
    def __init__(self, session):
        self.session = session

    def insert_user(self, data):
        checkEmail = UserRepository(self.session).find_by_email(data.get("EMAIL"))
        if checkEmail is None:
            user = User()
            user.NAME = data.get("NAME")
            user.EMAIL = data.get("EMAIL")
            user.USERNAME = randomString(7)
            user.PASSWORD = randomString(10)
            UserRepository(self.session).insert_user(user)
            # return user
            return jsonify({"message": "User inserted successfully"})
        if checkEmail is not None:
            return jsonify({"message": "UserEmail already Present"})

    def update_user(self, data):
        user = UserRepository(self.session).find_by_email(data.get("EMAIL"))
        if user is not None:
            user.NAME = data.get("NAME")
            # user.USERNAME = data.get("USERNAME")
            # user.PASSWORD = data.get("PASSWORD")
            return jsonify({"message": "User updated successfully"})
        else:
            return jsonify(message="Email is not present")
