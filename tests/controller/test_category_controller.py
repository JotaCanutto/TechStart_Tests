import sys
sys.path.append('.')
import pytest

from controller.base_controller import BaseController
from controller.category_controller import CategoryController
from model.category import Category


@pytest.fixture
def create_instance():
    controller = CategoryController()
    return controller

def test_category_controller_instance(create_instance):

    assert isinstance(create_instance, BaseController)
    assert isinstance(create_instance, CategoryController)


def test_read_all_should_return_list(create_instance):

    result = create_instance.read_all()

    assert isinstance(result, list)


def test_create_category(create_instance):
    name = 'Test Categoria'
    description = 'desc cat'
    cat = Category(name, description)

    result = create_instance.create(cat)
    
    assert result.id_ is not None
    assert result.name == name
    assert result.description == description

    create_instance.delete(result.id_)


def test_update_category(create_instance):
    name = 'Test Categoriagg'
    description = 'desc catggg'
    cat = Category(name, description)
    created = create_instance.create(cat)

    cat_up=create_instance.read_by_id(created.id_)

    cat_up.name = 'Test Categoria2'
    cat_up.description = 'desc cat2'

    result = create_instance.update(cat_up)

    assert result.id_ is not None
    assert result.name == 'Test Categoria2'
    assert result.description == 'desc cat2'

    create_instance.delete(result.id_)


def test_delete_category(create_instance):
    name = 'Test Categoria'
    description = 'desc cat'
    cat = Category(name, description)
    created = create_instance.create(cat)

    create_instance.delete(created.id_)

    with pytest.raises(Exception) as exc:
        create_instance.read_by_id(created.id_)
        assert str(exc.value) == 'Object not found in the database.'


def test_read_by_id_should_return_category(create_instance):
    name = 'Test Categoria'
    description = 'desc cat'
    cat = Category(name, description)
    created = create_instance.create(cat)

    result = create_instance.read_by_id(created.id_)

    assert isinstance(result, Category)
    assert result.name == name
    assert result.description == description

    create_instance.delete(created.id_)


def test_read_by_id_with_invalid_id_should_raise_exception():
    controller = CategoryController()

    with pytest.raises(Exception) as exc:
        controller.read_by_id(71289379)
        assert str(exc.value) == 'Object not found in the database.'

