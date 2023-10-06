import datetime
import os


def get_file_metadata(file_path):
    print(f'获取 {file_path} 信息')
    if os.path.exists(file_path):
        # 获取文件名称
        file_name = os.path.basename(file_path)
        file_type = os.path.splitext(file_name)[1]  # 获取文件扩展名
        # 获取文件大小（以字节为单位）
        file_size = __convert_size(os.path.getsize(file_path))

        # 获取文件创建时间（返回时间戳）
        create_time = os.path.getctime(file_path)

        # 获取文件修改时间（返回时间戳）
        modify_time = os.path.getmtime(file_path)

        # 将时间戳转换为可读的日期时间格式
        create_time_str = str(datetime.datetime.fromtimestamp(create_time))
        modify_time_str = str(datetime.datetime.fromtimestamp(modify_time))

        # 创建包含文件元数据的字典
        metadata = {
            'name': file_name,
            'file_type': file_type,
            'size': file_size,
            'create_time': create_time_str,
            'modify_time': modify_time_str
        }
        return metadata
    else:
        return {}


def __convert_size(size_bytes):
    # 1 KB = 1024 bytes
    # 1 MB = 1024 KB
    # 1 GB = 1024 MB
    # 将字节转换为KB、MB或GB，保留两位小数
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.2f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.2f} GB"
