from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from app.forms import RegistrationForm, LoginForm, BlogForm
from app.models import User, Blog

bp = Blueprint('routes', __name__)

@bp.route("/")
@bp.route("/home")
def home():
    blogs = Blog.query.all()
    return render_template('index.html', blogs=blogs)

@bp.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('routes.login'))
    return render_template('register.html', form=form)

@bp.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('routes.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', form=form)

@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('routes.home'))

@bp.route("/blog/new", methods=['GET', 'POST'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(blog)
        db.session.commit()
        flash('Your blog has been created!', 'success')
        return redirect(url_for('routes.home'))
    return render_template('blog.html', form=form)
