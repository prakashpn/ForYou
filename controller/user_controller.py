from flask import jsonify, Blueprint, request

from database.db_config import close_session, create_session
from json_serialize.json_util import UserJson
from repository.user_repository import UserRepository
from service.user_service import UserService

user_app = Blueprint('user', __name__)


@user_app.route('/test', methods=['GET'])
def test():
    return jsonify(message="Rediected to user controller")


@user_app.route('/user-list', methods=['GET'])
def view_user_list():
    """
    :return:It will give you user list present in User Table
    """
    session_con, con = create_session()
    datas = UserRepository(session_con).find_all()
    json_data = UserJson.get_list(datas)
    close_session(session_con, con)
    response = jsonify(json_data)
    return response


@user_app.route('/insert', methods=['POST'])
def insert_user():
    """

    :return: success message or error if found
    :rtype:
    """
    session_con, con = create_session()
    data = request.json
    try:
        data = UserService(session_con).insert_user(data)
        session_con.commit()
        close_session(session_con, con)
        return data
        # return jsonify({"message": "User inserted successfully"})
    except Exception as e:
        return e


@user_app.route('/update', methods=['PUT'])
def update_user():
    """

    :return:success message or error if found
    :rtype:
    """
    session_con, con = create_session()
    data = request.json
    try:
        data = UserService(session_con).update_user(data)
        session_con.commit()
        close_session(session_con, con)
        # return jsonify({"message": "User updated successfully"})
        return data
    except Exception as e:
        return e


@user_app.route('/delete/<USER_ID>', methods=['DELETE'])
def delete_user(USER_ID):
    """

    :param USER_ID:
    :return:
    """
    session_con, con = create_session()
    try:
        UserService(session_con).delete_user(USER_ID)
        session_con.commit()
        close_session(session_con, con)
        return jsonify({"message": "User deleted successfully"})
    except Exception as e:
        return e