from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import dojo

@app.route('/')
def home():
    return redirect('/all_dojos')

#Create 
@app.route('/create_dojo', methods = ['POST'])
def create_dojo():
    data = {
        'name' : request.form['name']
    }
    dojo.Dojo.save(data)
    return redirect('/all_dojos')


#Read 
@app.route('/all_dojos')
def view_all():
    dojos = dojo.Dojo.get_all()
    return render_template('index.html', all_dojos = dojos)

@app.route('/view/<int:id>')
def view(id):
    dojos_ninjas = dojo.Dojo.get_dojo_with_ninjas(id)
    return render_template('result.html', dojos_ninjas = dojos_ninjas)

#Update 



#Delete 