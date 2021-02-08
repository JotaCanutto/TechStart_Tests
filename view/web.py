from flask import Flask, render_template, request
from werkzeug.utils import redirect

from controller.category_controller import CategoryController
from model.category import Category

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/category')
def category_list():
    controller = CategoryController()
    categories_list = controller.read_all()
    return render_template('category.html', categories=categories_list)


@app.route('/category/create')
def category_create_form():
    id_aux = request.args.get('id')
    if id_aux:
        controller = CategoryController()
        category = controller.read_by_id(int(id_aux))
        return render_template('category_create.html', update=True, category=category)

    return render_template('category_create.html')


@app.route('/category', methods=['POST'])
def category_create():
    controller = CategoryController()
    name = request.form.get('name')
    description = request.form.get('description')
    new_category = Category(name, description)
    controller.create(new_category)
    return redirect('/category')


@app.route('/category/update', methods=['POST'])
def category_update():
    controller = CategoryController()
    id_aux = int(request.form.get('id'))
    name = request.form.get('name')
    description = request.form.get('description')
    category = controller.read_by_id(id_aux)
    category.name = name
    category.description = description
    controller.update(category)
    return redirect('/category')


@app.route('/category/delete')
def category_delete():
    controller = CategoryController()
    id_aux = int(request.args.get('id'))
    category = controller.read_by_id(id_aux)
    controller.delete(category.id_)
    return redirect('/category')


app.run(debug=True)
