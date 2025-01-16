__all__ = ['module1','module2']
# in this we are exposing only module1,2 only

"""
We cant import module1 and 2 beacuse there directory is a part of packages
So, we cant import them directly
.
├── packages
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   └── module1.cpython-312.pyc
│   ├── module1.py
│   ├── module2.py
│   └── module3.py
└── usage_package.py
import module1
import module2

"""
# breakpoint()
# import module1
# import module2

from packages import module1,module2,module3
