import io
from setuptools import setup, find_packages

readme_file = io.open('README.rst', encoding='utf-8')

with readme_file:
    long_description = readme_file.read()

setup(
    name="meetthings",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/marcidy/meetthings',
    license="",
    author="Matt Arcidy",
    description="web app for unifying meeting and event entry",
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python 3',
    ],
    keywords="meeting meetings meetup",
)
