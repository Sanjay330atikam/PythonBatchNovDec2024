'''
Purpose To copy file from one directory to another
'''

# import shutil
# # print(dir(shutil))
# '''
# rmtree_safe_fd', '_rmtree_unsafe', '_samefile', '_stat', '_unpack_tarfile', '_unpack_zipfile', '_use_fd_functions', '_win_path_needs_curdir', '_winapi', 'chown', 'collections', 'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree', 'disk_usage', 'errno', 'fnmatch', 'get_archive_formats', 'get_terminal_size', 'get_unpack_formats', 'ignore_patterns', 'make_archive', 'move', 'nt', 'os', 'posix', 'register_archive_format', 'register_unpack_format', 'rmtree', 'stat', 'sys', 'unpack_archive', 'unregister_archive_format', 'unregister_unpack_format', 'warnings', 'which']
# '''

# '''
# Which : This command where the path is present
# '''
# Python_path=shutil.which('Python')
# print(Python_path)

# ls_path=shutil.which('ls')
# print(ls_path)

"""
Process: To copy a file from one directory to another 
"""

import os
import shutil

def copy_file(src_dir,dest_dir,filename):
    source_path=os.path.join(src_dir,filename)
    dest_path=os.path.join(dest_dir,filename)

    if os.path.exists(dest_path):
        print("File already exists.So deleting")
        os.remove(dest_path)
    os.makedirs(dest_dir)

    shutil.copyfile(source_path,dest_path)

copy_file('test_dir_1',"test_dir_2",'test_file_1.txt')

#Copying File(test_file_1.txt) from test_dir_1(source) to test_dir_2(destination)