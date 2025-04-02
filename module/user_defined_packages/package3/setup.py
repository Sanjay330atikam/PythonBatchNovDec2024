from setuptools import setup,find_packages

setup (
    name='package3',
    version='0.10',
    description='A breif description of your project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your email@example.com',
    url='https://refactored-fortnight-wrgrwpwrxgg7h9x97.github.dev/',
    packages=find_packages(),
    install_requires=[
        # 'requests>=2.25.1',
        # 'numpy>=1.21.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3'
        'license :: OSI approved :: MIT license'
        'Operating System :: OS Independent'
    ],
    python_requires='>=3.6',
)
# run this commands to get output
#  $ pip install setuptools
# python setup.py sdist bdist_wheel
# package3-0.10.tar.gz:This is a virtual environment file accesed by people from outside by unzipping and using it
# package3-0.10-py3-none-any.whl: I some one has python module they can simple use this 
#Its creating new files
# cd dist/ : Command for going to find tar and wheel file
"""
FINAL PROJECT:
  ├── README.md
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-312.pyc
│   ├── calculator.cpython-312.pyc
│   └── operations.cpython-312.pyc
├── build
│   └── bdist.linux-x86_64
├── calculator.html
├── calculator.py
├── dist
│   ├── package3-0.10-py3-none-any.whl
│   └── package3-0.10.tar.gz
├── operations.py
├── package3.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
├── setup.py
├── usage_calculator.py
└── usage_operations.py

"""

# Passing  the whl file local then it will install
# pip install package3-0.10-py3-none-any.whl
# Processing ./package3-0.10-py3-none-any.whl
# Installing collected packages: package3
# Successfully installed package3-0.10

#After installing the while be a part of our site-packages.