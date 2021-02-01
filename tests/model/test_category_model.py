import sys

sys.path.append('.')

from model.category import Category
import pytest


def test_category_validate_name_str():
    with pytest.raises(TypeError):
        Category(10, 'Eletronicos')


def test_category_validate_name_empty():
    with pytest.raises(ValueError):
        Category('', 'Eletronicos')


def test_category_validate_name_len():
    with pytest.raises(ValueError):
        Category('Category' * 100, 'Eletronicos')


def test_category_validate_description_str():
    with pytest.raises(TypeError):
        Category('Category', 10)


def test_category_validate_description_len():
    with pytest.raises(ValueError):
        Category('Category', 'Eletronicos' * 100)


def test_create_valid_category():
    category = Category('Nome', 'Descrição')
    assert isinstance(category, Category)
