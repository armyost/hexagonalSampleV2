from abc import (ABC, abstractmethod)
from typing import Optional, List
from domain.models import (User, Department)

class RepositoryInterface(ABC):

    @abstractmethod
    def insertUser(self, user):
        pass

    @abstractmethod
    def selectUserWithDeptInfo(self, userId) -> List[User]:
        pass
    
    @abstractmethod
    def insertDepartment(self, department):
        pass