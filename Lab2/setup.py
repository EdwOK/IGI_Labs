from setuptools import setup, find_packages


setup(
    name='Lab2',
    version='1.0',
    author='Eduard Paprotski',
    author_email='fisheroliver9@gmail.com',
    maintainer='Lab2',
    license='PSF',
    description='My second lab for python',
    url='https://edwok.github.io/me/',
    packages=find_packages(exclude=["unit_tests"])
)