#-*- coding: utf-8 -*-

from setuptools import setup

setup(name='db2rest-tool',
      version='0.4.9',
      author='oliveirabrunoa',
      author_email='oliveirabrunoa@gmail.com',
      url='https://github.com/oliveirabrunoa/db2rest',

      packages=['DB2Rest'],

      scripts=['scripts/execute_db2rest'],

      install_requires=['Flask==1.0','gunicorn==19.6.0','flask_sqlalchemy==2.1','psycopg2==2.7.1','pytz==2016.10','requests==2.13.0'],

      include_package_data=True,
)
