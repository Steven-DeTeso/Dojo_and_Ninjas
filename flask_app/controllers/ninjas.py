from flask import render_template, request, redirect, url_for # type: ignore
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
    return redirect(url_for('rd_dojo_show', id = request.form.get('dojo_id')))