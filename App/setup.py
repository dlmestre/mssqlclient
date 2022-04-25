from setuptools import setup
from mssqlcli import __version__


setup(
    name='yamsqlscli',
    version=__version__,
    description=('Yet Another Microsoft SQL Server Client'),
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
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
],
    entry_points={
    'console_scripts': [
        'yamsqlscli=main:main',
    ],
},
)
