from flask import render_template, request, redirect # type: ignore
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask_app import app

@app.route('/')
def r_home():
    return redirect('/dojos')

@app.route('/dojos')
def r_dojos():
    return render_template('dojo.html', dojos = Dojo.get_all())

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    #prints below as immutable dict.
    print(request.form)
    # request.form is the data that is being accepted in the insert_into()
    Dojo.insert_into(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def r_dojo_show(id):
    data = {
        'id': id
    }
    # print(Dojo.get_one_with_ninjas(data))
    return render_template('dojo_show.html', dojos = Dojo.get_one_with_ninjas(data), ninjas = Ninja.get_all())
