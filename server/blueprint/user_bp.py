import sqlite3
import random
import string

from flask import Blueprint, request, jsonify

user_management_bp = Blueprint('user_management', __name__)


# 添加用户
@user_management_bp.route('', methods=['POST'])
def add_user():
    try:
        data = request.json
        username = data['username']
        role = data['role']
        permissions = data['permissions']
        status = data['status']
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, role, permissions, status) VALUES (?, ?, ?, ?)",
                       (username, role, permissions, status))
        conn.commit()
        conn.close()
        return jsonify({"message": "User added successfully"}), 201  # 返回201表示成功创建
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # 返回400表示客户端请求错误


# 获取所有用户
@user_management_bp.route('', methods=['GET'])
def get_users():
    try:
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        conn.close()
        user_list = []
        for user in users:
            user_dict = {
                "id": user[0],
                "username": user[1],
                "role": user[2],
                "permissions": user[3],
                "status": user[4]
            }
            user_list.append(user_dict)
        return jsonify(user_list), 200  # 返回200表示成功
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 返回500表示服务器内部错误


# 更新用户信息
@user_management_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        data = request.json
        username = data['username']
        role = data['role']
        permissions = data['permissions']
        status = data['status']
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET username=?, role=?, permissions=?, status=? WHERE id=?",
                       (username, role, permissions, status, user_id))
        conn.commit()
        conn.close()
        return jsonify({"message": "User updated successfully"}), 200  # 返回200表示成功
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 返回500表示服务器内部错误


# 删除用户
@user_management_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
        conn.commit()
        conn.close()
        return jsonify({"message": "User deleted successfully"}), 200  # 返回200表示成功
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # 返回500表示服务器内部错误


# 添加随机用户
@user_management_bp.route('/random', methods=['GET'])
def add_random_user():
    try:
        username, role, permissions, status = __generate_random_user()
        conn = sqlite3.connect('user.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, role, permissions, status) VALUES (?, ?, ?, ?)",
                       (username, role, permissions, status))
        conn.commit()
        conn.close()
        return jsonify({"message": "Random user added successfully"}), 201  # 返回201表示成功创建
    except Exception as e:
        return jsonify({"error": str(e)}), 400  # 返回400表示客户端请求错误


# 生成随机用户
def __generate_random_user():
    username = __generate_random_username()
    role = random.choice(['教授导师', '管家老师', '研三学生', '研二学生', '研一学生'])
    permissions = ','.join(random.sample(['管理员', '操作员', '超级管理员'], random.randint(1, 3)))
    status = random.choice(['active', 'inactive'])
    return username, role, permissions, status


# 生成随机用户名
def __generate_random_username(length=8):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))
