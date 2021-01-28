import sys
sys.path.append('.')
from model.category import Category


def test_category_validate_name_str():
    try:
        Category(10, 'Eletronicos')
        raise NotImplementedError('Exception not raised!')
    except Exception as e:
        assert isinstance(e, TypeError)
        assert e.args == ("Name must be a string!",)


def test_category_validate_name_empty():
    try:
        Category('', 'Eletronicos')
        raise NotImplementedError('Exception not raised!')
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.args == ("Name can't be null!",)


def test_category_validate_name_len():
    try:
        Category('Category'*100, 'Eletronicos')
        raise NotImplementedError('Exception not raised!')
    except Exception as e:
        assert isinstance(e, ValueError)
        assert e.args == ("Name must be 100 characters or less!",)
