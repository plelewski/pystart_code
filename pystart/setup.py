from setuptools import setup, find_packages

setup(
    name='pystart',
    version='0.0.1',
    description='some desc',
    long_description='...',
    author='Pek Lel',
    author_email='peklel@wp.pl',
    url='https://pystart.pl',
    packages=find_packages(exclude=['tests'])
)
