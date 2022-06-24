from setuptools import setup

setup(
    name='fail2bangeolocation',
    version='1.0',
    packages=['domain', 'application', 'application.utils', 'application.handlers', 'crosscutting', 'presentation',
              'presentation.utils'],
    url='https://github.com/rubenhortas/fail2bangeolocation',
    download_url='https://github.com/rubenhortas/fail2bangeolocation',
    license='GPL-3.0',
    author='Rubén Hortas Astariz',
    author_email='ruben.hortas@gmail.com',
    description='Identify the geographical locations of failed attempts to log into your system',
    long_description='Identify the geographical locations of failed attempts to log in to your system',
    install_requires=['requests', 'tqdm', 'colorama']
)
