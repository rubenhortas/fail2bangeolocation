from setuptools import setup

from crosscutting import strings

setup(
    name='fail2bangeolocation',
    version='1.0',
    packages=['application', 'application.utils', 'application.handlers', 'crosscutting', 'presentation',
              'presentation.utils'],
    url='https://github.com/rubenhortas/fail2bangeolocation',
    download_url='https://github.com/rubenhortas/fail2bangeolocation',
    license='GPL-3.0',
    author='Rubén Hortas Astariz',
    author_email='ruben.hortas@gmail.com',
    description=f'{strings.DESCRIPTION}',
    long_description=f'{strings.LONG_DESCRIPTION}',
    install_requires=['requests', 'tqdm', 'colorama']
)
