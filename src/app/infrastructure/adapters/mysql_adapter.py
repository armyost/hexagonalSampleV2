import os

from sqlalchemy import (
    Column,
    MetaData,
    String, Integer, Float,
    Table,
    Text,
    ForeignKey,
    create_engine,
    select
)

from domain.repositories import RepositoryInterface

metadata = MetaData()

users_table = Table(
    'user', metadata,
    Column('userId', Integer, primary_key=True),
    Column('description', Text, nullable=True),
    Column('userName', String(10), nullable=True),
    Column('deptId', Integer, ForeignKey("department.deptId"), nullable=True)
)

departments_table = Table(
    'department', metadata,
    Column('deptId', Integer, primary_key=True),
    Column('description', Text, nullable=True),
    Column('deptName', String(10), nullable=True)
)

###################### Common Function #####################

class MySqlAdapter(RepositoryInterface):

    def __init__(self, database_uri=None):
        uri = database_uri or os.getenv('DB_URI')
        db_engine = create_engine(uri, convert_unicode=True, echo=True)
        self.__create_tables_if_not_exists(db_engine)
        self.__connection = db_engine.connect()

    def close_db_connection(self, db_connection):
        try:
            db_connection.close()
        except:
            pass

    def __create_tables_if_not_exists(self, db_engine):
        departments_table.create(db_engine, checkfirst=True)
        users_table.create(db_engine, checkfirst=True)
        
        
###################### CRUD Function #####################

    def insertUser(self, user):
        with self.__connection.begin():
            self.__connection.execute(
                users_table.insert(),
                user.as_dict()
            )

    def selectUserWithDeptInfo(self, userId):
        with self.__connection.begin():
            stmt = select([users_table, departments_table]).distinct().select_from(users_table.outerjoin(departments_table, users_table.c.deptId == departments_table.c.deptId)).where(users_table.c.userId == userId)
            row = self.__connection.execute(stmt).fetchone()
            return {
                'userId' : row['userId'],
                'userName' : row['userName'],
                'deptName' : row['deptName']
            } if row else None

            
    def insertDepartment(self, department):
        with self.__connection.begin():
            self.__connection.execute(
                departments_table.insert(),
                department.as_dict()
            )
            
############################################################