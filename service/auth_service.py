from datetime import datetime

from flask import jsonify, abort

from database.db_config import User
from json_serialize.json_util import UserJson, AdminJson
from repository.admin_repository import AdminRepository
from repository.user_repository import UserRepository
from util.random_string import randomString


class AuthService():
    def __init__(self, session):
        self.session = session

    def find_and_process(self, data):
        checkType = data.get("USERTYPE")

        if checkType == "admin":
            admin = AdminRepository(self.session).find_by_email_and_username(data.get("USERNAME"), data.get("PASSWORD"))
            if admin is None:
                # return user
                # return jsonify({"message": "Username is Invalid"})
                return abort(400, 'Username or Password is invalid')
            if admin is not None:
                json_data = AdminJson.get_dict(admin)
                print("admin data :", json_data)
                return jsonify(json_data)

        elif checkType == "user":
            user = UserRepository(self.session).find_by_email_and_username(data.get("USERNAME"), data.get("PASSWORD"))
            if user is None:
                # return user
                # return jsonify({"message": "Username is Invalid"})
                return abort(400, 'Username or Password is invalid')
            if user is not None:
                json_data = UserJson.get_dict(user)
                print("user data :", json_data)
                return jsonify(json_data)
        else:
            return abort(400, 'Type is invalid')
