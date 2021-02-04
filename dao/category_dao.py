from model.category import Category
from dao.base_dao import BaseDao

class CategoryDao(BaseDao):
    def __init__(self):
        super().__init__(Category)
