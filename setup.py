# Note: To upload this project, you must:

'''
python setup.py sdist
pip install dist/wireless-control-0.1.0.tar.gz
python setup.py bdist_wheel
pip install twine
twine upload dist/*
'''

import os.path
from setuptools import setup


# What packages are required for this module to be executed?
requires = [
    'cerium>=1.2.0',
    'prompt_toolkit>=1.0.15',
]

# Import the README and use it as the long-description.
cwd = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(cwd, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Where the magic happens:
setup(
    name='wireless-control',
    py_modules=['wireless_control'],
    version='0.1.0',
    license='BSD',
    author='White Turing',
    author_email='fujiawei@stu.hznu.edu.cn',
    description='A command line wireless control tool for Android.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/fjwCode/wireless-control',
    keywords=['android', 'control', 'automation', 'testing', 'cerium'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6.0',
    install_requires=requires,
    platforms='Windows',
)
