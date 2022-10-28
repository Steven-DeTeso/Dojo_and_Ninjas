from flask import render_template, request, redirect, url_for #type: ignore
from flask_app.controllers.dojos import r_dojo_show # type: ignore
from flask_app.models.dojo import Dojo
from flask_app.models.dojo import Ninja
from flask_app import app

@app.route('/ninjas') 
def r_ninjas():
    return render_template('ninja.html', dojos= Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.insert_into(request.form)
    return redirect(url_for('r_dojo_show', id = request.form.get('dojo_id')))

@app.route('/edit/ninja/<int:id>')
def edit_ninja(id):
    data = {
        'id': id
    }
    return render_template('ninja_edit.html', ninjas= Ninja.get_one(data))

@app.route('/edit/this/ninja', methods=['POST'])
def edit_one_ninja():
    Ninja.update(request.form)
    return redirect(url_for('r_dojo_show', id = request.form['dojo_id']))

@app.route('/ninja/destroy/<int:id>')
def ninja_destroy(id):
    data = {
        'id': id
    }
    ninja = Ninja.get_one(data)
    Ninja.destroy(data)
    return redirect(url_for('r_dojo_show', id = ninja[0].dojo_id))