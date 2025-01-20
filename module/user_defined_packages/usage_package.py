import os

import sys

import packages.module1

print(os.getcwd())
print(os.listdir())

for each_path in sys.path:
 print(each_path)

# assing the path
sys.path.insert(0,'packages')

"""
 cureent working directory
        /workspaces/PythonBatchNovDec2024/module/user_defined_packages()

built-in modules        
  /usr/local/python/3.12.1/lib/python312.zip
  /usr/local/python/3.12.1/lib/python3.12
  /usr/local/python/3.12.1/lib/python3.12/lib-dynload

installed modules
  /home/codespace/.local/lib/python3.12/site-packages
  /usr/local/python/3.12.1/lib/python3.12/site-packages
 """
#importing a module--single file
import module1

# importing a packages
import packages
print(packages)
print(dir(packages))

# while doing dir we are not getting values to get those we are creating __init__,py file
print(f"{packages.module1}")
print(packages.module1)
# internal module can be executed.
packages.module1.Hello_World()#
packages.module2.Hello_World()#
packages.module3.Hello_World()#

"""
packages.module2.Hello_World
packages.module3.Hello_World
These n
"""