from setuptools import setup
from mssqlcli import __version__


setup(
    name='mssqlclient',
    version=__version__,
    description=('Python Cliente for Microsoft SQL Server'),
    packages=['mssqlcli'],
    package_dirs={
        'mssqlcli': 'mssqlcli'
    },
    install_requires=[
        'pymssql==2.2.5',
        'PyYAML==5.4.1'
    ],
    classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: System Administrators',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
],
    entry_points={
    'console_scripts': [
        'mssqlclient=main:main',
    ],
},
)
