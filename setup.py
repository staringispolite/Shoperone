from setuptools import setup
from setuptools import find_packages

setup(
    name='shoperone',
    version='0.1',
    description='Shoperone. A marketplace for people who love shopping. And those who hate it.',
    author='Jonathan Howard',
    author_email='jon@staringinspolite.com',
    url='https://github.com/staringispolite/Shoperone',
    install_requires=[
        'simplejson',
        'Flask',
        'Flask-SQLAlchemy'
    ],
    setup_requires=[],
    packages=find_packages(),
    include_package_data=True
)
