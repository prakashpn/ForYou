'''
DOC:            07/03/2023
Created By:     Prakash
Purpose:        login and logout
'''

from flask import Blueprint, request
from flask_login import logout_user

from database.db_config import close_session, create_session
from service.auth_service import AuthService

auth_app = Blueprint('auth', __name__)

'''
Name:       auth_login()
DOC:        07/03/2023
Method:     POST
Parameters: 
Purpose:    Login user/admin if username password valid as per db
Return:     message:  response of success/Failure
'''


@auth_app.route('/login', methods=['POST'])
def auth_login():
    """
    return:    It will give you user list present in User Table
    """
    session_con, con = create_session()
    data = request.json
    try:
        response = AuthService(session_con).find_and_process(data)
        close_session(session_con, con)
        return response

    except Exception as e:
        return e


'''
Name:       auth_logout()
DOC:        07/03/2023
Method:     POST
Parameters: admin email and user details in the body
Purpose:    Used to create/insert new record in the user table
Return:     message:  response of success/Failure
'''


@auth_app.route('/logout', methods=['POST'])
def auth_logout():
    """

    :return: success message or error if found
    :rtype:
    """
    # logout_user()
    return {"message": "Logout successfully"}
