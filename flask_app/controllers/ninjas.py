from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import dojo, ninja

#Create
@app.route('/create_ninja')
def create():
    dojos = dojo.Dojo.get_all()
    return render_template('create_ninja.html', all_dojos= dojos)

@app.route('/create', methods = ['POST'])
def process():
    # data = {
    #     'fname' : request.form['fname'],
    #     'lname' : request.form['lname'],
    #     'location' : request.form['location'],
    #     'age' : request.form['age']
    # }
    ninja.Ninja.save(request.form)  
    return redirect('/')


#Read

#Update


#Delete
@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')