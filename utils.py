import os
import shutil


def delete_directory(path, excludepath):
    if os.path.exists(path):
        for file_name in os.listdir(path):
            file_path = os.path.join(path, file_name)
            if file_path in excludepath:
                print(f"'{file_path}' is in the list.")
                pass
            else:
                print(f"'{file_path}' is not in the list.")
                if os.path.isdir(file_path):
                    if any(is_parent_directory(file_path, i) for i in excludepath):
                        print("当前目录是某个的父")
                        pass
                    else:
                        shutil.rmtree(file_path)
                else:
                    os.remove(file_path)


    else:
        print("目录或文件不存在！")
def is_parent_directory(parent_dir, sub_dir):
    parent_dir = os.path.realpath(parent_dir)
    sub_dir = os.path.realpath(sub_dir)
    return sub_dir.startswith(os.path.join(parent_dir, ''))

if __name__ == '__main__':
    delete_directory("temp", ["temp/ss/sss"])
