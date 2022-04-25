import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Period(SqlAlchemyBase):
    __tablename__ = 'olympiads'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    olimpiad_id = sqlalchemy.Column(sqlalchemy.Integer)
    olimpiad_name = sqlalchemy.Column(sqlalchemy.String)
    first_tour = sqlalchemy.Column(sqlalchemy.String)
    time_to_remind = sqlalchemy.Column(sqlalchemy.String)
    list_of_users = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f'<Period> {self.olimpiad_id, self.first_tour}'
