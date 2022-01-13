from os import environ

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import insert


SQL_CONNECTION = environ.get('SQL_CONNECTION', 'sqlite+pysqlite:///:memory:')

engine = create_engine(SQL_CONNECTION, echo=True, future=True)

metadata_obj = MetaData()

user_table = Table(
    'users',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('email', String(256)),
    Column('full_name', String(50))
)

address_table = Table(
    'addresses',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('users.id'), nullable=False),
    Column('address', String, nullable=False)
)


def new_user(email, full_name):
    with engine.begin() as conn:
        result = conn.execute(insert(user_table), {'email': email, 'full_name': full_name})
        return result.inserted_primary_key.id


def get_user(id_):
    with engine.begin() as conn:
        result = conn.execute(select(user_table).where(user_table.c.id == id_))
        return result.mappings().first()
