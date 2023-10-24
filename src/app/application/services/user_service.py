import logging

import inject
from domain.models import User
from domain.repositories import RepositoryInterface

class UserService:
    @inject.autoparams()
    def __init__(self, database: RepositoryInterface):
        self.__database = database

    def addUser(self, id, description, userName, deptId):
        user = User(
            userId = id,
            description = description,
            userName = userName,
            deptId = deptId
        )
        self.__database.insertUser(user)

        return {
            'userId': user.userId,
            'description': user.description,
            'userName': user.userName,
            'deptId': user.deptId
        }

    def detailUser(self, userId):
        userDetailInfo = self.__database.selectUserWithDeptInfo(userId)
        logging.warn("!!! userDetailInfo : !!!" + str(userDetailInfo))
        return userDetailInfo