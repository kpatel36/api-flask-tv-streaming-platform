# connect it to larger flask app so we define it as a blueprint
from flask import Blueprint, render_template, request, redirect, url_for

# define our blueprint/create the auth instance of a flask blueprint
auth = Blueprint('auth', __name__, template_folder='auth_templates', url_prefix='/auth')

from .authforms import SignInForm, RegisterForm

@auth.route('/', methods=['GET', 'POST'])
def signin():
    siform = SignInForm()
    if request.method=="POST":
     #(this means user submitted form)
        if siform.validate_on_submit():            
            return redirect(url_for('home'))
        else:
            # bad form info - tell them to try again
            return redirect(url_for('auth.signin'))
    return render_template('signin.html', siform=siform)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    rform=RegisterForm()
    if request.method=="POST":
     #(this means user submitted form)
        if rform.validate_on_submit():            
            return redirect(url_for('home'))
        else:
            # bad form info - tell them to try again
            flash('Your passwords did not match ')
            return redirect(url_for('auth.register'))
    return render_template('register.html', rform=rform)