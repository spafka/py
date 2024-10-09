#!/usr/bin/env python
# coding=utf-8
__author__ = 'zhuo'
__date__ = '2017/5/25'
# shutil_demo.py 高级文件操作(拷贝 / 移动 / 压缩 / 解压缩)

import shutil


def shutil_demo():
    # 拷贝文件
    shutil.copy2('file.txt', 'temp.txt')

    # 拷贝目录
    shutil.copytree("root", "temp", symlinks=False, ignore=shutil.ignore_patterns("*.pyc"), copy_function=shutil.copy2, ignore_dangling_symlinks=True)

    # 删除目录
    shutil.rmtree("temp", ignore_errors=True)

    # 移动文件/目录
    shutil.move("root", "temp", copy_function=shutil.copy2)

    # 获取磁盘使用空间
    total, used, free = shutil.disk_usage(".")
    print("当前磁盘共: %iGB, 已使用: %iGB, 剩余: %iGB"%(total / 1073741824, used / 1073741824, free / 1073741824))

    # 压缩文件
    shutil.make_archive('Box', 'zip', 'temp')

    # 解压文件
    shutil.unpack_archive('Box.zip')



def shutil_func():
    # 文件和目录操作
    # shutil.copyfileobj(fsrc, fdst[, length]) // 拷贝文件内容, 将fsrc文件里的内容copy到fdst文件中, length:缓冲区大小
    shutil.copyfileobj(open('file.txt', 'r'), open('temp.txt', 'w'))
    # shutil.copyfile(src, dst, *, follow_symlinks=True) // 拷贝文件内容, 同copyfileobj, 如果dst=src,抛SameFileError异常, dst存在则替换
    dst = shutil.copyfile('file.txt', 'temp.txt')
    # shutil.copymode(src, dst, *, follow_symlinks=True) // 仅拷贝权限, 其他信息不受影响
    shutil.copymode('file.txt', 'temp.txt')
    # shutil.copystat(src, dst, *, follow_symlinks=True) // 拷贝状态(权限 / 最后访问时间 / 上次修改时间 / 标志), 其他不受迎影响
    shutil.copystat('file.txt', 'temp.txt')
    # shutil.copy(src, dst, *, follow_symlinks=True) // 拷贝文件(数据 / 权限)
    dst = shutil.copy('file.txt', 'temp.txt')
    # shutil.copy2(src, dst, *, follow_symlinks=True) // 拷贝文件(尝试保留所有元数据) (不能拷贝创建时间,该时间可通过修改系统时间再创建文件来实现)
    dst = shutil.copy2('file.txt', 'temp.txt')
    # shutil.ignore_patterns(*patterns)
    # symlinks:True(复制链接) / False(复制文件), ignore=ignore_patterns("") // 忽略的文件, copy_function=自定义复制函数, ignore_dangling_symlinks:True(忽略文件不存在异常) / False(错误列表中添加异常)
    # shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False) // 递归的复制根目录下的整个目录树
    dst = shutil.copytree("root", "temp", symlinks=False, ignore=shutil.ignore_patterns("*.pyc"), copy_function=shutil.copy2, ignore_dangling_symlinks=True)
    # shutil.rmtree(path, ignore_errors=False, onerror=None) // 删除整个目录树, ignore_errors:是否忽略删除失败错误, onerror=def error(func, path, excinfo)
    shutil.rmtree("temp", ignore_errors=True)
    # shutil.move(src, dst, copy_function=copy2) // 递归移动文件/目录, 目录存在则移动目录, 文件存在则覆盖
    dst = shutil.move("root", "temp", copy_function=shutil.copy2)
    total, used, free = shutil.disk_usage(".") # 给定路径的磁盘使用情况统计信息
    # shutil.chown(path, user=None, group=None) // 修改用户和组 (Unix可用)
    # shutil.which(cmd, mode=os.F_OK | os.X_OK, path=None) // 可执行文件路径, path:要查找的路径,未指定使用os.environ的结果
    path_str = shutil.which("python")


    # 异常
    try: pass
    except shutil.SameFileError: pass # copyfile()时,源和目录是同一个文件时,抛此异常
    except shutil.Error: pass # copytree()时, 多文件操作时引发的异常, 异常包含(srcname, dstname, excinfo)



    # 压缩文件操作 (封装了zipfile / tarfile)
    # 创建归档文件 base_name:压缩包文件名, format:格式 zip / tar / bztar / xztar / gztar, root_dir:被归档的根目录(默认当前目录)
    # base_dir:保存归档文件的目录(默认当前目录) verbose:已弃用 dry_run:True(不创建归档,但记录日志), owner:用户, group:用户组, logger:日志
    # shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])
    dst = shutil.make_archive('Box', 'zip', 'temp') # 注意:root_dir / base_dir至少写一个,不然会造成压缩包再次被打包的情况
    # 分拆归档, filename:文件名, extract_dir:解压到目录(默认当前目录), format:格式 (未提供,根据扩展名查找,未找到引发ValueError)
    # shutil.unpack_archive(filename[, extract_dir[, format]])
    shutil.unpack_archive('Box.zip')

    lists = shutil.get_archive_formats() # 返回支持的归档格式列表[(format, info)]
    lists = shutil.get_unpack_formats() # 返回所有注册格式的列表[(name, extensions, description)]

    # 注册压缩格式, name:格式名, function:def func(base_name, base_dir, owner, group, dry_run, logger), extra_args:额外参数, description:说明信息
    # shutil.register_archive_format(name, function[, extra_args[, description]])
    # shutil.unregister_archive_format(name) // 注销压缩格式
    # 注册解压格式 name:格式名, extensions:扩展名列表, function:实现函数 def unpack(filename, extract_dir), extra_args:额外参数(name, value), description:说明
    # shutil.register_unpack_format(name, extensions, function[, extra_args[, description]])
    # shutil.unregister_unpack_format(name) // 注销解压格式



    # 终端
    # shutil.get_terminal_size(fallback=(columns, lines))
    columns, lines = shutil.get_terminal_size() # 查询终端大小(宽, 高), 无法查询返回默认大小(80, 24)



if __name__ == "__main__":
    shutil_demo()

    # shutil_func()
