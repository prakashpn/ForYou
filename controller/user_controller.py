'''
DOC:            07/03/2023
Created By:     Prakash
Purpose:        get all ,Insert and update user if admin email is valid
'''

from flask import jsonify, Blueprint, request
from database.db_config import close_session, create_session
from json_serialize.json_util import UserJson
from repository.user_repository import UserRepository
from service.user_service import UserService
from repository.admin_repository import AdminRepository

user_app = Blueprint('user', __name__)

'''
Name:       view_user_list()
DOC:        07/03/2023
Method:     GET
Parameters: 
Purpose:    Used to get all user from user table
Return:     [List]  response of success/Failure
'''


@user_app.route('/user-list', methods=['GET'])
def view_user_list():
    """
    return:    It will give you user list present in User Table
    """
    try:
        session_con, con = create_session()
        datas = UserRepository(session_con).find_all()
        json_data = UserJson.get_list(datas)
        close_session(session_con, con)
        response = jsonify(json_data)
        return response

    except Exception as e:
        return e


'''
Name:       insert_user()
DOC:        07/03/2023
Method:     POST
Parameters: admin email and user details in the body
Purpose:    Used to create/insert new record in the user table
Return:     message:  response of success/Failure
'''


@user_app.route('/insert', methods=['POST'])
def insert_user():
    """

    :return: success message or error if found
    :rtype:
    """
    session_con, con = create_session()
    data = request.json
    # print("data :", data)
    try:
        adminEmail = data.get("admin").get("EMAIL")
        userData = data.get("user")
        checkEmail = AdminRepository(session_con).find_by_email(adminEmail)
        if checkEmail:
            # print("Admin is Present")
            data = UserService(session_con).insert_user(userData)
            session_con.commit()
            close_session(session_con, con)
            return data
        else:
            return jsonify({"message": "Invalid Admin"})
    except Exception as e:
        return e


'''
Name:       update_user()
DOC:        07/03/2023
Method:     PUT
Parameters: admin email and user details in the body
Purpose:    Used to update the record according to the avail user email in the user table
Return:     message:  response of success/Failure
'''


@user_app.route('/update', methods=['PUT'])
def update_user():
    """

    :return:success message or error if found
    :rtype:
    """
    session_con, con = create_session()
    data = request.json
    # print("data :", data)
    try:
        adminEmail = data.get("admin").get("EMAIL")
        userData = data.get("user")
        checkEmail = AdminRepository(session_con).find_by_email(adminEmail)
        if checkEmail:
            # print("Admin is Present")
            data = UserService(session_con).update_user(userData)
            session_con.commit()
            close_session(session_con, con)
            return data
        else:
            return jsonify({"message": "Invalid Admin"})
    except Exception as e:
        return e
