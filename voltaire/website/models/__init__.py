from sqlalchemy.dialects.postgresql import UUID
import sqlalchemy
import uuid
from .. import db


class Base(object):
    id = db.Column(UUID, default=lambda: str(uuid.uuid4()), primary_key=True)
    created_at = db.Column(db.DateTime(), default=sqlalchemy.func.now())
    updated_at = db.Column(
        sqlalchemy.DateTime(), default=sqlalchemy.func.now(),
        onupdate=sqlalchemy.func.now())

    __mapper_args__ = {'order_by': sqlalchemy.desc('updated_at')}


from .users import *
