from flask import jsonify, Blueprint, request

from database.db_config import close_session, create_session
from json_serialize.json_util import AdminJson
from repository.admin_repository import AdminRepository
from service.admin_service import AdminService

admin_app = Blueprint('admin', __name__)


@admin_app.route('/admin-list', methods=['GET'])
def view_admin_list():
    """
    :return:It will give you admin list present in Admin Table
    """
    session_con, con = create_session()
    datas = AdminRepository(session_con).find_all()
    json_data = AdminJson.get_list(datas)
    close_session(session_con, con)
    response = jsonify(json_data)
    return response


@admin_app.route('/insert', methods=['POST'])
def insert_admin():
    """

    :return: success message or error if found
    :rtype:
    """
    session_con, con = create_session()
    data = request.json
    try:
        data = AdminService(session_con).insert_admin(data)
        session_con.commit()
        close_session(session_con, con)
        return data
        # return jsonify({"message": "Admin inserted successfully"})
    except Exception as e:
        return e


@admin_app.route('/update', methods=['PUT'])
def update_admin():
    """

    :return:success message or error if found
    :rtype:
    """
    session_con, con = create_session()
    data = request.json
    try:
        data = AdminService(session_con).update_admin(data)
        session_con.commit()
        close_session(session_con, con)
        # return jsonify({"message": "Admin updated successfully"})
        return data
    except Exception as e:
        return e


@admin_app.route('/delete/<ADMIN_ID>', methods=['DELETE'])
def delete_admin(ADMIN_ID):
    """

    :param ADMIN_ID:
    :return:
    """
    session_con, con = create_session()
    try:
        AdminService(session_con).delete_admin(ADMIN_ID)
        session_con.commit()
        close_session(session_con, con)
        return jsonify({"message": "Admin deleted successfully"})
    except Exception as e:
        return e
