from dao.base_dao import BaseDao
from model.base_model import BaseModel



class BaseController:
    def __init__(self, dao: BaseDao) -> None:
        self.__dao = dao
                
    def create(self, model: BaseModel) -> None:
        return self.__dao.save(model)
       
    def read_by_id(self, id: int) -> BaseModel:
        result = self.__dao.read_by_id(id)
        return result

    def read_all(self) -> list:
        result = self.__dao.read_all()
        return result

    def delete(self, id: int) -> None:
        item = self.read_by_id(id)
        self.__dao.delete(item)
        
    def update(self, model: BaseModel) -> None:
        return self.__dao.save(model)
