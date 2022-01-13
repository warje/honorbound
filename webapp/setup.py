from setuptools import setup, find_packages


setup(
    name='webapp',
    version='1.0.0',
    packages=find_packages(),
    description=('Test Web App'),
    install_requires=[
        'flask~=2.0.0',
        'sqlalchemy~=1.4.0',
        'psycopg2-binary',
    ],
    include_package_data=True,
)
