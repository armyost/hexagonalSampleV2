import logging

import inject
from domain.models import Department
from domain.repositories import RepositoryInterface

class DepartmentService:
    @inject.autoparams()
    def __init__(self, database: RepositoryInterface):
        self.__database = database

    def addDepartment(self, deptId, description, deptName):
        department = Department(
            deptId = deptId,
            description = description,
            deptName = deptName
        )
        self.__database.insertDepartment(department)

        return {
            'deptId': department.deptId,
            'description': department.description,
            'deptName': department.deptName
        }