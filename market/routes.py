from market import app, db
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm

@app.route('/')
def home_page():
  return render_template('home.html')


@app.route('/market')
def market_page():
  items = Item.query.all()
  return render_template('market.html', items=items)


@app.route('/register', methods=['GET', 'POST'])
def register_page():
  form = RegisterForm()
  if form.validate_on_submit():
    user = User(
      username=form.username.data,
      email=form.email.data,
      password=form.password1.data,
    )

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('market_page'))

  if form.errors != {}:
    for error in form.errors.values():
      flash(error, category='danger')

  return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
  form = LoginForm()
  return render_template('login.html', form=form)
