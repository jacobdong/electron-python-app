import os
import sqlite3


def check_table():
    conn = sqlite3.connect(get_server_db())
    cursor = conn.cursor()

    # 检查表格是否存在
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone()

    if not table_exists:
        cursor.execute('''CREATE TABLE users
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          username TEXT NOT NULL,
                          role TEXT NOT NULL,
                          permissions TEXT NOT NULL,
                          status TEXT NOT NULL)''')
        print('数据库创建成功')
    conn.commit()
    conn.close()


def check_app_dir():
    user_home = os.path.expanduser("~")
    # 指定文件夹路径
    folder_path = "electron-python-app/server"
    app_dir = os.path.join(user_home, folder_path)
    print(f'user_home {user_home}')
    print(f'目标文件夹 {app_dir}')
    # 检查文件夹是否存在
    if not os.path.exists(app_dir):
        # 如果文件夹不存在，创建它
        os.makedirs(app_dir, exist_ok=True)
        print(f"文件夹 '{app_dir}' 创建成功")
    else:
        print(f"文件夹 '{app_dir}' 已存在")
    return app_dir


def get_server_db():
    base_dir = check_app_dir()
    return os.path.join(base_dir, 'server.db')
